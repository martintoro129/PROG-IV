# portfolio/components/projects.py

import reflex as rx
from portfolio.styles import STYLE_DICT

def project_card(title: str, description: str, tags: list) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Título con color acentuado
            rx.heading(title, size="5", color=STYLE_DICT["accent_color"], margin_bottom="0.5rem"),
            
            # Descripción
            rx.text(description, color=STYLE_DICT["text_main"], size="2", line_height="1.5"),
            
            rx.spacer(),
            
            # Badges de tecnologías (Tags)
            rx.hstack(
                *[rx.badge(tag, variant="outline", color_scheme="sky") for tag in tags],
                wrap="wrap",
                spacing="2",
                margin_top="1rem",
            ),
            align_items="start",
            height="100%",
        ),
        # ESTILO GLASSMORPHISM
        background="rgba(30, 41, 59, 0.5)", # Fondo semi-transparente
        backdrop_filter="blur(12px)",      # Desenfoque de fondo
        border=f"1px solid rgba(56, 189, 248, 0.2)", # Borde muy fino y sutil
        padding="2rem",
        border_radius="20px",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-10px)",
            "border": f"1px solid {STYLE_DICT['accent_color']}",
            "box_shadow": f"0 20px 40px rgba(0, 0, 0, 0.4)",
        },
        width="100%",
        height="280px",
    )

def projects_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Proyectos Recientes", size="8", margin_bottom="3rem"),
        rx.grid(
            project_card(
                "Dashboard Administrativo",
                "Sistema de gestión con autenticación avanzada, roles de usuario y reportes dinámicos usando PHP y MySQL.",
                ["PHP", "MySQL", "AdminLTE"]
            ),
            project_card(
                "E-commerce Tech",
                "Plataforma de ventas con carrito de compras, pasarela de pagos simulada y diseño responsivo.",
                ["React", "Node.js", "Tailwind"]
            ),
            project_card(
                "Gestión Académica",
                "Software para el control de notas, asistencia y comunicación entre profesores y alumnos.",
                ["Python", "Reflex", "SQLite"]
            ),
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="6",
            width="100%",
        ),
        padding="5rem 10%",
        id="projects",
        width="100%",
    )