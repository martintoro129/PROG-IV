# portfolio/components/services.py

import reflex as rx
from portfolio.styles import STYLE_DICT

def service_item(title: str, description: str, image_url: str, is_reverse: bool = False) -> rx.Component:
    # Definimos el botón de WhatsApp como un componente reutilizable
    whatsapp_button = rx.link(
        rx.button(
            rx.icon(tag="message_circle", size=18), # Icono de conversación (Lucide)
            "Contactar por WhatsApp",
            variant="solid",
            cursor="pointer",
            background_color="#25D366",
            color="white",
            _hover={
                "background_color": "#128C7E", 
                "transform": "scale(1.05)",
                "transition": "all 0.2s ease"
            },
        ),
        href="https://wa.me/584142773241",
        is_external=True,
    )

    content = [
        # Contenedor de Imagen
        rx.box(
            rx.image(
                src=image_url,
                border_radius="15px",
                border=f"2px solid {STYLE_DICT['accent_color']}",
                box_shadow=f"0 10px 30px rgba(0,0,0,0.5)",
                width="100%",
                transition="transform 0.3s ease",
                _hover={"transform": "scale(1.02)"}
            ),
            flex="1",
        ),
        # Contenedor de Texto
        rx.vstack(
            rx.heading(title, size="6", color=STYLE_DICT["accent_color"]),
            rx.text(description, color=STYLE_DICT["text_dim"], line_height="1.6"),
            whatsapp_button,
            flex="1",
            align_items="start",
            spacing="4",
        ),
    ]
    
    return rx.flex(
        *(reversed(content) if is_reverse else content),
        spacing="9",
        align="center",
        margin_bottom="6rem",
        flex_direction=rx.breakpoints(initial="column", md="row"),
        width="100%",
    )

def services_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Habilidades y Servicios", size="8", margin_bottom="4rem"),
        
        service_item(
            "Desarrollo Full Stack",
            "Especialista en el ciclo completo de desarrollo, desde la arquitectura de bases de datos en MySQL hasta la lógica de servidor en PHP (Laravel) y Python (Reflex).",
            "https://via.placeholder.com/500x350/1e293b/38bdf8?text=Full+Stack+Dev",
        ),
        service_item(
            "Diseño e Ilustración Digital",
            "Creativo visual con experiencia en la creación de piezas gráficas personalizadas, logotipos y composiciones digitales para marcas modernas.",
            "https://via.placeholder.com/500x350/1e293b/38bdf8?text=Digital+Design",
            is_reverse=True,
        ),
        service_item(
            "Sublimación y Restauración",
            "Técnicas avanzadas de personalización mediante sublimación y procesos meticulosos de restauración de piezas artísticas y sacras.",
            "https://via.placeholder.com/500x350/1e293b/38bdf8?text=Art+Restoration",
        ),
        
        padding="5rem 10%",
        id="habilidades",
        width="100%",
    )