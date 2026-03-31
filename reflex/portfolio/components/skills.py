import reflex as rx
from ..styles import skill_card_style, STYLE_DICT

def skill_card(title: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="4", color=STYLE_DICT["accent_color"]), # Size 1-9 en Reflex moderno
        rx.text(description, color=STYLE_DICT["text_dim"], size="2"),
        style=skill_card_style,
        align="center",
    )

def skills_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Mis Habilidades", size="8", margin_bottom="2rem"),
        rx.grid(
            skill_card("Frontend", "HTML5, CSS3, Bootstrap 5, Diseño UI/UX"),
            skill_card("Backend", "PHP, Manejo de APIs, Lógica de Servidor"),
            skill_card("Database", "MySQL, Optimización de Consultas"),
            # Importante: columns debe ser un dict o lista para responsividad
            columns=rx.breakpoints(initial="1", sm="2", lg="3"), 
            spacing="6", # Valor de escala 1-9
            width="100%",
        ),
        padding="5rem 10%",
        id="skills",
        width="100%",
        align="center",
    )