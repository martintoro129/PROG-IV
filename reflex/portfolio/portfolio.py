# portfolio/portfolio.py

import reflex as rx
from portfolio.styles import BASE_STYLE, STYLE_DICT
from portfolio.components.navbar import navbar
from portfolio.components.hero import hero
from portfolio.components.about import about_section
from portfolio.components.services import services_section
from portfolio.components.skills import skills_section
from portfolio.components.projects import projects_section

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            hero(),
            about_section(),
            services_section(),
            skills_section(),
            projects_section(),
            # Footer
            rx.center(
                rx.text("© 2026 | Martin Toro", color=STYLE_DICT["text_dim"]),
                padding="4rem",
            ),
            width="100%",
            spacing="0",
        ),
        # Aplicamos el gradiente animado a todo el contenedor
        style=BASE_STYLE,
        min_height="100vh",
        width="100%",
    )

app = rx.App(style=BASE_STYLE) # También puedes aplicarlo a nivel de App
app.add_page(index)