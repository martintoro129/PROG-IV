<?php
include 'conexion.php';
session_start();

$id_materia = $_GET['id_materia'] ?? null;
$mi_id = $_SESSION['user_id'];

if (!$id_materia) exit();

// Consulta Senior: Filtramos usuarios que son alumnos en la misma materia
$sql = "SELECT u.id, u.nombre, u.foto 
        FROM usuarios u
        JOIN alumnos a ON u.id_alumno = a.id
        WHERE a.id_materia = :materia AND u.id != :mi_id";

$stmt = $pdo->prepare($sql);
$stmt->execute(['materia' => $id_materia, 'mi_id' => $mi_id]);
$companeros = $stmt->fetchAll();

foreach($companeros as $c): ?>
    <a href="javascript:void(0)" class="list-group-item list-group-item-action border-0 mb-1 rounded" 
       onclick="cargarConversacion(<?= $c['id'] ?>, '<?= htmlspecialchars($c['nombre']) ?>')">
        <div class="d-flex align-items-center">
            <img src="dist/img/<?= $c['foto'] ?>" class="rounded-circle me-2" width="35" height="35">
            <span class="small fw-bold"><?= htmlspecialchars($c['nombre']) ?></span>
        </div>
    </a>
<?php endforeach; ?>