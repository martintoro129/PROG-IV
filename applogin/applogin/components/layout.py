import reflex as rx
from .sidebar import sidebar  # Importa tu componente sidebar existente

def admin_layout(child: rx.Component, **kwargs) -> rx.Component:
    return rx.box(  # Cambiamos hstack por box, ya que el sidebar es 'fixed'
        sidebar(),
        rx.box(
            child,
            padding="2rem",
            margin_left="250px",  # Margen para dejar espacio al sidebar
            color="#333",
            width="calc(100% - 250px)", # Ancho ajustado
            **kwargs 
        ),
        width="100%",

    )