<?php
include 'conexion.php';
session_start();

// 1. Debugging Senior: Ver qué está llegando (revisa tu error_log de PHP)
error_log("POST: " . print_r($_POST, true));
error_log("FILES: " . print_r($_FILES, true));

if (!isset($_SESSION['user_id']) || empty($_POST['id_receptor'])) {
    die("error_datos_incompletos");
}

$id_emisor = $_SESSION['user_id'];
$id_receptor = $_POST['id_receptor'];
$mensaje = $_POST['mensaje'] ?? '';
$archivo_ruta = null;
$tipo_archivo = 'texto';

// 2. Procesar Adjunto
if (!empty($_FILES['adjunto']['name'])) {
    $dir = "uploads/chat/";
    if (!is_dir($dir)) mkdir($dir, 0777, true);
    
    $ext = pathinfo($_FILES['adjunto']['name'], PATHINFO_EXTENSION);
    $nombre_archivo = uniqid("IMG_", true) . "." . $ext;
    $destino = $dir . $nombre_archivo;

    if (move_uploaded_file($_FILES['adjunto']['tmp_name'], $destino)) {
        $archivo_ruta = $destino;
        $tipo_archivo = in_array(strtolower($ext), ['jpg', 'png', 'jpeg']) ? 'imagen' : 'pdf';
    }
}

// 3. Inserción con Manejo de Excepciones
try {
    // IMPORTANTE: Verifica que los nombres de las columnas coincidan con tu tabla
    $sql = "INSERT INTO chat_mensajes (id_emisor, id_receptor, mensaje, archivo, tipo_archivo, fecha_envio, leido) 
            VALUES (?, ?, ?, ?, ?, NOW(), 0)";
    
    $stmt = $pdo->prepare($sql);
    if ($stmt->execute([$id_emisor, $id_receptor, $mensaje, $archivo_ruta, $tipo_archivo])) {
        echo "ok";
    } else {
        echo "error_db_execute";
    }
} catch (PDOException $e) {
    // Si hay un error de SQL (ej. columna inexistente), aparecerá aquí
    error_log("Error SQL Chat: " . $e->getMessage());
    echo "error_sql_exception: " . $e->getMessage();
}