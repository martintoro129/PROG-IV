<?php 
include 'conexion.php'; 
session_start();
if (!isset($_SESSION['user_id'])|| $_SESSION['rol'] !== 'Admin') {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Comunicados Masivos | Senior Dev</title>
    
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
     <link href="https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.20/summernote-lite.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!--- datatables.y.bootstrap.buttons -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.4.1/css/buttons.bootstrap5.min.css">

    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

    <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />

    <link rel="stylesheet" href="estilos.css">


    
    

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    
</head>
        <?php
    require_once('sidebar.php');
    ?>
<body class="bg-light">
<div class="container mt-5">
    <form id="form_envio" enctype="multipart/form-data">
        <div class="card shadow border-0">
            <div class="card-header bg-dark text-white">
                <h4 class="mb-0"><i class="fas fa-paper-plane me-2"></i> Centro de Comunicaciones</h4>
            </div>
            <div class="card-body">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label class="form-label fw-bold">1. Seleccionar Materia</label>
                        <select name="id_materia" id="sel_materia" class="form-select" required>
                            <option value="">Seleccione...</option>
                            <?php 
                            $mats = $pdo->query("SELECT * FROM materias");
                            while($m = $mats->fetch()) echo "<option value='{$m['id']}'>{$m['nombre_materia']}</option>";
                            ?>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label fw-bold">2. Asunto del Correo</label>
                        <input type="text" name="asunto" class="form-control" placeholder="Ej: Guía de estudio para el examen" required>
                    </div>
                </div>

                <!-- <div class="mb-3">
                    <label class="form-label fw-bold">3. Mensaje / Cuerpo del Email</label>
                    <textarea name="mensaje" class="form-control" rows="4" placeholder="Escriba el contenido aquí..." required></textarea>
                </div> -->
                <div class="mb-3">
                    <label class="form-label fw-bold">3. Mensaje / Cuerpo del Email</label>
                    <textarea name="mensaje" id="editor_mensaje" class="form-control" required></textarea>
                </div>

                <div class="mb-4">
                    <label class="form-label fw-bold">4. Adjuntar Archivo (Opcional)</label>
                    <input type="file" name="adjunto" class="form-control">
                </div>

                <div class="table-responsive bg-white p-3 border rounded">
                    <label class="form-label fw-bold text-primary">5. Seleccionar Destinatarios</label>
                    <table class="table table-sm">
                        <thead>
                            <tr>
                                <th width="50"><input type="checkbox" id="checkAll"></th>
                                <th>Alumno</th>
                                <th>Correo</th>
                            </tr>
                        </thead>
                        <tbody id="lista_destinatarios">
                            </tbody>
                    </table>
                </div>
            </div>
            <div class="card-footer text-end">
                <div id="progreso_envio" class="mb-3 d-none">
                    <div class="d-flex justify-content-between mb-1">
                        <span class="fw-bold">Procesando envíos...</span>
                        <span id="porcentaje_texto">0%</span>
                    </div>
                    <div class="progress" style="height: 20px;">
                        <div id="barra_progreso" class="progress-bar progress-bar-striped progress-bar-animated bg-success" 
                            role="progressbar" style="width: 0%"></div>
                    </div>
                    <small id="status_envio" class="text-muted mt-1 d-block text-center">Iniciando motor de mensajería...</small>
                </div>
                <button type="submit" class="btn btn-primary px-5 shadow" id="btnEnviar">
                    <i class="fas fa-envelope-open-text me-2"></i> ENVIAR AHORA
                </button>
            </div>
        </div>
    </form>
</div>

<script src="https://code.jquery.com/jquery-3.7.0.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.20/summernote-lite.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.20/lang/summernote-es-ES.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
    //*** NOTA IMPORTANTE: el código JavaScript se ha colocado al final del body para asegurar que el DOM 
    // esté completamente cargado antes de ejecutar cualquier script. 
    // Esto es crucial para evitar errores relacionados con elementos no encontrados, 
    // especialmente al inicializar plugins como Summernote o al manipular el DOM con jQuery. 
    // Si se colocara en el head sin la debida espera, podría generar errores críticos 
    // que afectarían la funcionalidad de la página. ***

//     var $j = jQuery.noConflict();

// $j(document).ready(function() {
//     console.log("Iniciando verificación de Summernote...");
    
//     if ($j.fn.summernote) {
//         $j('#editor_mensaje').summernote({
//             placeholder: 'Escriba aquí...',
//             height: 300,
//             lang: 'es-ES',
//             toolbar: [
//                 ['style', ['bold', 'italic', 'underline', 'clear']],
//                 ['font', ['strikethrough']],
//                 ['para', ['ul', 'ol', 'paragraph']],
//                 ['insert', ['link', 'hr']],
//                 ['view', ['fullscreen', 'codeview']]
//             ]
//         });
//         console.log("¡Summernote cargado exitosamente!");
//     } else {
//         console.error("Error crítico: La librería Summernote no se encuentra en el objeto jQuery.");
//         alert("Error: No se pudo cargar el editor. Revisa la consola (F12).");
//     }
// }); 
    
    
$(document).ready(function() {
    // Intentar inicializar con reintento si falla
    function inicializarEditor() {
        if (typeof $.fn.summernote !== 'undefined') {
            $('#editor_mensaje').summernote({
                placeholder: 'Escriba su mensaje profesional aquí...',
                tabsize: 2,
                height: 300,
                lang: 'es-ES',
                toolbar: [
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['insert', ['link', 'hr']],
                    ['view', ['fullscreen', 'codeview']]
                ]
            });
            console.log("Summernote cargado con éxito.");
        } else {
            console.error("Summernote aún no está disponible, reintentando...");
            setTimeout(inicializarEditor, 500); // Reintenta en medio segundo
        }
    }

    inicializarEditor();
});

$('#sel_materia').on('change', function() {
    let id = $(this).val();
    let lista = $('#lista_destinatarios');
    
    if(id) {
        lista.html('<tr><td colspan="3" class="text-center"><i class="fas fa-spinner fa-spin"></i> Cargando alumnos...</td></tr>');
        
        $.post('get_alumnos_correo.php', { id_materia: id })
        .done(function(data) {
            // Si el servidor devolvió un error estructurado
            if(data.error) {
                Swal.fire('Error de Servidor', data.error, 'error');
                return;
            }

            let html = '';
            if(data.length === 0) {
                html = '<tr><td colspan="3" class="text-center">No hay alumnos inscritos en esta materia.</td></tr>';
            } else {
                data.forEach(al => {
                    let sinCorreo = !al.email || al.email === '';
                    html += `
                    <tr class="${sinCorreo ? 'table-warning' : ''}">
                        <td>
                            <input type="checkbox" name="destinatarios[]" value="${al.id}" ${sinCorreo ? 'disabled' : 'checked'}>
                        </td>
                        <td>
                            ${al.nombre_alumno} 
                            ${sinCorreo ? '<span class="badge bg-danger">Falta Email</span>' : ''}
                        </td>
                        <td>${al.email || '<em class="text-muted">No asignado</em>'}</td>
                    </tr>`;
                });
            }
            lista.html(html);
        })
        .fail(function(jqXHR, textStatus, errorThrown) {
            console.error("Error en AJAX:", textStatus, errorThrown);
            Swal.fire('Error Crítico', 'No se pudo conectar con el servidor: ' + textStatus, 'error');
        });
    } else {
        lista.html('<tr><td colspan="3" class="text-center text-muted">Seleccione una materia para cargar alumnos</td></tr>');
    }
});

// Selección masiva
$('#checkAll').click(function() {
    $('input:checkbox').not(this).prop('checked', this.checked);
});

$('#form_envio').submit(function(e) {
    e.preventDefault();
     let formData = new FormData(this);
    /**
     * AQUI SUCEDE LA MAGIA: el formulario se envía a procesar_envio.php, donde se maneja toda la lógica de envío masivo.
     * El proceso incluye validaciones, manejo de adjuntos, iteración sobre destinatarios y actualización del progreso en tiempo real.
     * Es crucial que procesar_envio.php esté bien optimizado para manejar grandes volúmenes de correos.
     */
     $.ajax({
         url: 'procesar_envio.php',
         type: 'POST',
         data: formData,
         contentType: false,
         processData: false,
         success: function(response) {
             Swal.fire('¡Envío Exitoso!', response, 'success');
             $('#form_envio')[0].reset();
             $('#lista_destinatarios').html('');
             $('#editor_mensaje').summernote('reset');
         },
         error: function(jqXHR, textStatus, errorThrown) {
             console.error("Error en AJAX:", textStatus, errorThrown);
             Swal.fire('Error Crítico', 'No se pudo enviar el comunicado: ' + textStatus, 'error');
         }
     });
    
});
</script>
</body>
</html>