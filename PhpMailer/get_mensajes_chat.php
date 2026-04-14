<?php
include 'conexion.php';
session_start();

// 1. VALIDACIÓN DE SESIÓN Y PARÁMETROS
if (!isset($_SESSION['user_id'])) {
    exit("<p class='text-center text-danger'>Sesión expirada.</p>");
}

$mi_id = $_SESSION['user_id'];
$id_receptor = $_POST['id_receptor'] ?? null;

if (!$id_receptor) {
    exit("<p class='text-center text-muted'>Selecciona una conversación para comenzar.</p>");
}

try {
    // 2. MARCAR MENSAJES COMO LEÍDOS (Lógica de Negocio)
    // Cuando abro el chat, los mensajes que me envió el receptor pasan a ser 'leídos'
    $stmtRead = $pdo->prepare("UPDATE chat_mensajes SET leido = 1 WHERE id_emisor = ? AND id_receptor = ? AND leido = 0");
    $stmtRead->execute([$id_receptor, $mi_id]);

    // 3. CONSULTA OPTIMIZADA
    // Traemos solo lo necesario y ordenamos por fecha
    $sql = "SELECT id_emisor, mensaje, archivo, tipo_archivo, fecha_envio 
            FROM chat_mensajes 
            WHERE (id_emisor = :yo AND id_receptor = :otro) 
               OR (id_emisor = :otro AND id_receptor = :yo) 
            ORDER BY fecha_envio ASC";
    
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['yo' => $mi_id, 'otro' => $id_receptor]);
    $mensajes = $stmt->fetchAll(PDO::FETCH_ASSOC);

    if (empty($mensajes)) {
        echo "<div class='text-center mt-5 text-muted'>
                <i class='fas fa-comments fa-3x mb-3'></i>
                <p>No hay mensajes previos. ¡Sé el primero en escribir!</p>
              </div>";
        exit;
    }

    // 4. RENDERIZADO CON UX DIFERENCIADA
    foreach ($mensajes as $m) {
        $es_mio = ($m['id_emisor'] == $mi_id);
        $clase_burbuja = $es_mio ? 'ms-auto bg-primary text-white' : 'me-auto bg-white text-dark shadow-sm';
        $alineacion = $es_mio ? 'justify-content-end' : 'justify-content-start';
        $hora = date('H:i', strtotime($m['fecha_envio']));
        
        echo "<div class='d-flex $alineacion mb-3'>";
        echo "  <div class='p-3 rounded-3' style='max-width: 75%; $clase_burbuja'>";
        
        // Manejo de Texto
        if (!empty($m['mensaje'])) {
            echo "<div class='message-text'>" . htmlspecialchars($m['mensaje']) . "</div>";
        }

        // Manejo de Adjuntos (Lógica Senior: Verificación de tipo)
        if ($m['archivo']) {
            echo "<div class='mt-2 border-top pt-2' style='border-color: rgba(255,255,255,0.2) !important;'>";
            
            if ($m['tipo_archivo'] === 'imagen') {
                echo "<a href='{$m['archivo']}' target='_blank'>
                        <img src='{$m['archivo']}' class='img-fluid rounded' style='max-height: 200px; cursor: pointer;'>
                      </a>";
            } else if ($m['tipo_archivo'] === 'pdf') {
                $btn_class = $es_mio ? 'btn-light' : 'btn-outline-danger';
                echo "<a href='{$m['archivo']}' target='_blank' class='btn btn-sm $btn_class w-100'>
                        <i class='fas fa-file-pdf me-1'></i> Ver Documento PDF
                      </a>";
            }
            echo "</div>";
        }

        echo "    <div class='text-end mt-1' style='font-size: 0.75rem; opacity: 0.8;'>
                    $hora " . ($es_mio ? "<i class='fas fa-check-double ms-1'></i>" : "") . "
                  </div>";
        echo "  </div>";
        echo "</div>";
    }

} catch (PDOException $e) {
    error_log("Error en chat: " . $e->getMessage());
    echo "<p class='text-center text-danger'>Error al cargar la conversación.</p>";
}
?>