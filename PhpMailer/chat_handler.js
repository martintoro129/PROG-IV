/**
 * Senior Chat Handler
 * Gestiona la carga, envío y scroll del chat interno
 */
// chat_handler.js
$(document).ready(function() {
    console.log("Chat Handler Cargado y jQuery listo.");

    $(document).on('submit', '#form-enviar-chat', function(e) {
        e.preventDefault();
        
        const receptor = $('#receptor_id').val();
        if (!receptor) {
            Swal.fire('Atención', 'Selecciona un contacto primero', 'warning');
            return;
        }

        // FormData captura todos los 'name' del formulario automáticamente
        let datos = new FormData(this);

        $.ajax({
            url: 'enviar_mensaje_chat.php',
            type: 'POST',
            data: datos,
            contentType: false,
            processData: false,
            beforeSend: function() {
                $('button[type="submit"]').prop('disabled', true);
            },
            success: function(res) {
                if (res.trim() === "ok") {
                    $('#input-mensaje').val('');
                    $('#adjunto_chat').val('');
                    // Recargar la caja de texto
                    cargarConversacion(receptor, $('#chat-header').text());
                } else {
                    console.error("Respuesta del servidor:", res);
                    Swal.fire('Error', 'No se pudo guardar: ' + res, 'error');
                }
            },
            complete: function() {
                $('button[type="submit"]').prop('disabled', false);
            }
        });
    });
});

function cargarConversacion(id, nombre) {
    // 1. Seteamos el receptor de forma segura
    const receptorInput = $('#receptor_id');
    if (receptorInput.length) {
        receptorInput.val(id);
    }

    // 2. Actualizamos la cabecera
    $('#chat-header').html(`<i class="fas fa-user-circle me-2"></i> <strong>${nombre}</strong>`);
    
    // 3. Feedback visual de carga
    $('#chat-box').html('<div class="text-center mt-5"><i class="fas fa-spinner fa-spin fa-2x text-muted"></i></div>');

    // 4. Petición AJAX
    $.post('get_mensajes_chat.php', { id_receptor: id }, function(html) {
        $('#chat-box').html(html);
        
        // Ejecutamos el scroll con un pequeño timeout para asegurar el renderizado
        setTimeout(scrollChatBottom, 100);
    }).fail(function() {
        $('#chat-box').html('<div class="alert alert-danger m-3">Error al conectar con el servidor.</div>');
    });
}

function enviarMensaje() {
    const input = $('#input-mensaje');
    const idReceptor = $('#receptor_id').val();
    
    if (input.val().trim() === "" && !$('#adjunto_chat')[0].files.length) return;
    if (!idReceptor) return Swal.fire('Error', 'Selecciona un contacto primero', 'error');

    // Usamos FormData para soportar los archivos adjuntos que configuramos
    let formData = new FormData($('#form-enviar-chat')[0]);

    $.ajax({
        url: 'enviar_mensaje_chat.php',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(res) {
            if (res.trim() === "ok") {
                input.val(''); // Limpiar texto
                $('#adjunto_chat').val(''); // Limpiar archivo
                cancelFile(); // Ocultar preview si la tenías
                
                // Recargar la conversación para ver el nuevo mensaje
                const nombreActual = $('#chat-header').text().replace(" Chat con: ", "");
                cargarConversacion(idReceptor, nombreActual);
            }
        }
    });
}

/**
 * Función de Scroll Crítica (Donde estaba el error)
 * Implementada con chequeo de existencia de objeto (Defensiva)
 */
function scrollChatBottom() {
    const chatBox = $("#chat-box");
    if (chatBox.length > 0) {
        const scrollHeight = chatBox.prop("scrollHeight");
        chatBox.stop().animate({ scrollTop: scrollHeight }, 500);
    }
}

setInterval(function() {
    const idReceptor = $('#receptor_id').val();
    if (idReceptor) {
        // Recargamos silenciosamente el contenido
        $.post('get_mensajes_chat.php', { id_receptor: idReceptor }, function(html) {
            // Solo actualizamos si el contenido cambió para no parpadear
            if ($('#chat-box').html() !== html) {
                $('#chat-box').html(html);
                scrollChatBottom();
            }
        });
    }
}, 5000);

function actualizarListaCompaneros(idMateria) {
    if(!idMateria) {
        $('#lista-contactos').html('<p class="text-center p-3 small text-muted">Selecciona una materia</p>');
        return;
    }

    $.get('get_companeros_materia.php', { id_materia: idMateria }, function(html) {
        $('#lista-contactos').html(html);
    });
}