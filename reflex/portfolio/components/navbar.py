import reflex as rx
from ..styles import STYLE_DICT

def navbar() -> rx.Component:
    return rx.hstack(
        # Logo: Combinando dos textos en un Box
        rx.box(
            rx.text("Dev", font_weight="bold", font_size="1.5rem", display="inline"),
            rx.text("Stack", color=STYLE_DICT["accent_color"], font_weight="bold", font_size="1.5rem", display="inline"),
        ),
        rx.spacer(),
        # Enlaces
        rx.hstack(
            rx.link("Inicio", href="#home", color=STYLE_DICT["text_main"], text_decoration="none", _hover={"color": STYLE_DICT["accent_color"]}),
            rx.link("Habilidades", href="#skills", color=STYLE_DICT["text_main"], text_decoration="none", _hover={"color": STYLE_DICT["accent_color"]}),
            rx.link("Proyectos", href="#projects", color=STYLE_DICT["text_main"], text_decoration="none", _hover={"color": STYLE_DICT["accent_color"]}),
            spacing="7", # Reflex 0.4.x+ usa valores de escala (1-9) o strings con unidades
        ),
        position="fixed",
        width="100%",
        top="0",
        z_index="1000",
        padding_x="10%",
        padding_y="1.5rem",
        background_color="rgba(15, 23, 42, 0.9)",
        backdrop_filter="blur(10px)",
        align="center",
    )