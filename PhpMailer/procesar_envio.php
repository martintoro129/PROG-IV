<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

# myaccount.google.com/apppasswords para habilitar acceso a emails desde 3ros programas (como PHPMailer) 
# si usas Gmail. Crea una contraseña específica para esta app y úsala en lugar de tu contraseña normal. 
# Esto mejora la seguridad al no compartir tu contraseña principal.kfwo jpye zrbi kdvp / mxke cdic agkb xvzj
# Recuerda mantener esa contraseña segura y no compartirla con nadie. 

require 'vendor/autoload.php'; // Asegúrate de tener PHPMailer instalado
include 'conexion.php';

$id_materia = $_POST['id_materia'];
$asunto     = $_POST['asunto'];
$mensaje    = $_POST['mensaje'];
$alumnos_ids = $_POST['destinatarios'] ?? [];

if(empty($alumnos_ids)) { echo "No seleccionaste alumnos."; exit; }

// Manejo de Archivo
$ruta_adjunto = null;
if(!empty($_FILES['adjunto']['name'])) {
    $ruta_adjunto = 'uploads/' . time() . '_' . $_FILES['adjunto']['name'];
    move_uploaded_file($_FILES['adjunto']['tmp_name'], $ruta_adjunto);
}

// 1. Registrar en historial
$stmt = $pdo->prepare("INSERT INTO comunicados_historial (id_materia, asunto, mensaje, archivo_adjunto) VALUES (?,?,?,?)");
$stmt->execute([$id_materia, $asunto, $mensaje, $ruta_adjunto]);
$id_comunicado = $pdo->lastInsertId();

$enviados = 0;
$errores = 0;



foreach($alumnos_ids as $id_al) {
    // Obtener correo del alumno
    $stmtAl = $pdo->prepare("SELECT nombre_alumno, email FROM alumnos WHERE id = ?");
    $stmtAl->execute([$id_al]);
    $alumno = $stmtAl->fetch();
    $cuerpo_profesional = "
        <div style='border: 1px solid #ddd; padding: 20px; font-family: Arial;'>
            <h2 style='color: #007bff;'>Información de Interes</h2>
            <hr>
            <div>$mensaje</div>
            <hr>
            <p style='font-size: 10px; color: #777;'>Este es un correo automático, por favor no responda.</p>
        </div>";
    

    if($alumno['email']) {
        $mail = new PHPMailer(true);

        try {
            // Configuración SMTP (Usa Gmail o tu hosting)
            $mail->isSMTP();

            #$mail->SMTPDebug = 2; 
            #$mail->Debugoutput = 'html'; // Para que sea legible en el navegador

            $mail->Host       = 'smtp.gmail.com';
            $mail->SMTPAuth   = true;
            $mail->Username   = 'sbtecnove@gmail.com';
            $mail->Password   = '';  //AQUI EL PASSWORD DE APLICACION DE GOOGLE
            $mail->SMTPSecure = 'ssl';
            #$mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
            #$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port       = 465;
            #$mail->Port       = 587; #tcp 587 para STARTTLS, tcp 465 para SSL

            $mail->setFrom('sbtecnove@gmail.com', 'Prof Martin Toro - Comunicado');
            $mail->addAddress($alumno['email'], $alumno['nombre_alumno']);
            
            if($ruta_adjunto) $mail->addAttachment($ruta_adjunto);

            $mail->isHTML(true);
            $mail->Subject = $asunto;
            //$mail->Body    = nl2br($mensaje);
            //$mail->Body    = $mensaje;
            $mail->Body = $cuerpo_profesional;
            

            $mail->send();
            
            // Registrar destinatario
            $pdo->prepare("INSERT INTO comunicado_destinatarios VALUES (?,?)")->execute([$id_comunicado, $id_al]);
            $enviados++;
        } catch (Exception $e) { $errores++; }
    }
}

echo "Proceso finalizado. Enviados: $enviados. Fallidos: $errores";
