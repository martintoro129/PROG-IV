# portfolio/components/about.py

import reflex as rx
from portfolio.styles import STYLE_DICT

def about_section() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.heading("Perfil Profesional", size="7", color=STYLE_DICT["accent_color"]),
                
                # Usamos hstack para alinear la etiqueta y el valor
                rx.hstack(
                    rx.text("Ubicación: ", font_weight="bold", color=STYLE_DICT["text_main"]),
                    rx.text("Guatire, Miranda, Venezuela", color=STYLE_DICT["text_main"]),
                    spacing="2", # Ahora sí funciona porque hstack sí acepta spacing
                ),
                
                rx.hstack(
                    rx.text("Nivel Académico: ", font_weight="bold", color=STYLE_DICT["text_main"]),
                    rx.text("Estudiante de 4to Año de Bachillerato", color=STYLE_DICT["text_main"]),
                    spacing="2",
                ),

                rx.text(
                    "Desarrollador Full Stack en formación y artista multidisciplinario. "
                    "Combino habilidades técnicas en programación backend con una sólida "
                    "experiencia en diseño digital y restauración de arte sacro.",
                    color=STYLE_DICT["text_dim"],
                    margin_top="1rem",
                ),
                align_items="start",
                flex="2",
            ),
            
            # Columna de contacto corregida
            rx.vstack(
                rx.box(
                    rx.heading("Datos de Contacto", size="4", color=STYLE_DICT["accent_color"], margin_bottom="1rem"),
                    rx.vstack(
                        rx.hstack(rx.text("Teléfono: ", font_weight="bold"), rx.text("0414-277-32-41")),
                        rx.hstack(rx.text("Idiomas: ", font_weight="bold"), rx.text("Español, Inglés")),
                        rx.text("Traducción: PL, RU, SK, RO, JP", size="1", color=STYLE_DICT["text_dim"]),
                        align_items="start",
                        spacing="1",
                    ),
                    background=STYLE_DICT["bg_color"],
                    padding="25px",
                    border_radius="12px",
                    border_left=f"4px solid {STYLE_DICT['accent_color']}",
                    width="100%",
                ),
                flex="1",
                width="100%",
            ),
            spacing="8",
            flex_direction=["column", "column", "row"], 
        ),
        padding="5rem 10%",
        background_color=STYLE_DICT["card_bg"], 
        id="about",
        width="100%",
    )