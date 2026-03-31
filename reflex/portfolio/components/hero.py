import reflex as rx
from ..styles import STYLE_DICT

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Desarrollador Full Stack", size="9", margin_bottom="1rem", text_align="center"),
            rx.text("Nombre: Martin Toro", font_size="1.25rem", color=STYLE_DICT["text_dim"]),
            rx.text("Email: martintoro129@gmail.com", font_size="1.25rem", color=STYLE_DICT["text_dim"]),
            rx.text(
                "Especializado en soluciones escalables con PHP, MySQL y diseño de interfaces modernas.",
                max_width="600px",
                text_align="center",
                color=STYLE_DICT["text_dim"]
            ),
            rx.link(
                "Ver Proyectos",
                href="#projects",
                padding="0.8rem 2rem",
                background_color=STYLE_DICT["accent_color"],
                color=STYLE_DICT["bg_color"],
                border_radius="5px",
                font_weight="bold",
                text_decoration="none",
                _hover={"opacity": "0.8", "transform": "translateY(-3px)"},
                margin_top="2rem",
            ),
            align="center",
            spacing="5",
        ),
        id="home",
        height="100vh",
        background=f"radial-gradient(circle, {STYLE_DICT['card_bg']} 0%, {STYLE_DICT['bg_color']} 100%)",
        width="100%",
    )