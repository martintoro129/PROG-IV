<?php
include 'conexion.php';
session_start();
// ... validación de sesión ...

// Obtener lista de usuarios excepto yo mismo
$stmt = $pdo->prepare("SELECT id, nombre, foto, rol FROM usuarios WHERE id != ?");
$stmt->execute([$_SESSION['user_id']]);
$contactos = $stmt->fetchAll();
?>
<head>
        <meta charset="UTF-8">
        <title>Panel Administrativo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

        <!--- datatables.y.bootstrap.buttons -->
        <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css">
        <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.4.1/css/buttons.bootstrap5.min.css">

        <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

        <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />

        <link rel="stylesheet" href="estilos.css">

        <style>

        </style>
</head>
     <?php
    require_once('sidebar.php');
    #echo "<pre>";
    #print_r($_SESSION);
    #echo "</pre>";
    ?>
<!-- <div class="p-3 bg-dark text-white">
    <label class="small d-block mb-1">Filtrar por Materia:</label>
    <select id="select_materia" class="form-select form-select-sm bg-secondary text-white border-0" onchange="actualizarListaCompaneros(this.value)">
        <option value="">Seleccione...</option>
        <?php
        // Obtenemos las materias donde el usuario logueado está inscrito
        #$stmtMat = $pdo->prepare("
        #    SELECT m.id, m.nombre_materia 
        #    FROM materias m
        #    JOIN alumnos a ON m.id = a.id_materia
        #    JOIN usuarios u ON a.id_alumno = u.id_alumno
        #    WHERE u.id = ?
        #");
        #$stmtMat->execute([$_SESSION['user_id']]);
        #while($m = $stmtMat->fetch()) {
        #    echo "<option value='{$m['id']}'>{$m['nombre_materia']}</option>";
        #}
        ?>
    </select>
</div> -->

<div id="lista-contactos" class="list-group list-group-flush overflow-auto" style="max-height: 60vh;">
</div>
<div class="container-fluid mt-3">
    <div class="row" style="height: 80vh;">
        <div class="col-md-4 border-end bg-white p-0">
            <div class="p-3 bg-dark text-white"><h5>Contactos</h5></div>
            <div class="list-group list-group-flush overflow-auto" style="max-height: 70vh;">
                <?php foreach($contactos as $c): ?>
                    <a href="#" class="list-group-item list-group-item-action contact-item" 
                       data-id="<?= $c['id'] ?>" onclick="cargarConversacion(<?= $c['id'] ?>, '<?= $c['nombre'] ?>')">
                        <div class="d-flex align-items-center">
                            <!-- <img src="dist/img/<?= $c['foto'] ?>" class="rounded-circle me-2" width="40"> -->
                            <div>
                                <div class="fw-bold"><?= $c['nombre'] ?></div>
                                <small class="text-muted"><?= $c['rol'] ?></small>
                            </div>
                        </div>
                    </a>
                <?php endforeach; ?>
            </div>
        </div>

        <div class="col-md-8 d-flex flex-column bg-light">
            <div id="chat-header" class="p-3 bg-white border-bottom fw-bold">Seleccione un contacto</div>
            <!-- <div id="chat-box" class="flex-grow-1 p-3 overflow-auto" style="background-image: url('dist/img/chat-bg.png');"> -->
            <div id="chat-box" class="flex-grow-1 p-3 overflow-auto" style="background-color: #f8f9fa;">
                </div>
            <div class="p-3 bg-white border-top">
                <!-- <form id="form-enviar-chat" class="d-flex">
                    <input type="hidden" id="receptor_id" name="id_receptor">
                    <input type="text" name="mensaje" class="form-control me-2" placeholder="Escribe un mensaje..." required id="input-mensaje">
                    <button type="submit" class="btn btn-primary"><i class="fas fa-paper-plane"></i></button>
                </form> -->
                <form id="form-enviar-chat" enctype="multipart/form-data" class="d-flex align-items-center">
                    <input type="hidden" id="receptor_id" name="id_receptor">
                    
                    <label for="adjunto_chat" class="btn btn-outline-secondary me-2 mb-0">
                        <i class="fas fa-paperclip"></i>
                    </label>
                    <input type="file" id="adjunto_chat" name="adjunto" class="d-none" onchange="previewFile()">
                    
                    <input type="text" name="mensaje" id="input-mensaje" class="form-control me-2" placeholder="Escribe un mensaje o adjunta un archivo...">
                    
                    <button type="submit" class="btn btn-primary"><i class="fas fa-paper-plane"></i></button>
                </form>

                <div id="file-preview" class="small text-muted d-none mt-1">
                    <i class="fas fa-file-alt"></i> <span id="file-name"></span>
                    <button type="button" class="btn-close btn-sm" onclick="cancelFile()"></button>
                </div>
            </div>
        </div>
    </div>
</div>

<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

<script src="chat_handler.js"></script>
<script>

</script>