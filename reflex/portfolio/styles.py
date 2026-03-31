import reflex as rx

STYLE_DICT = {
    "bg_color": "#0f172a",
    "card_bg": "#1e293b",
    "accent_color": "#38bdf8",
    "text_main": "#f8fafc",
    "text_dim": "#94a3b8",
}

# Definimos la animación de fondo
# Esto crea un gradiente que se desplaza suavemente
BASE_STYLE = {
    "background": f"linear-gradient(-45deg, #0f172a, #1e293b, #0f172a, #334155)",
    "background_size": "400% 400%",
    "animation": "gradient 15s ease infinite",
    "@keyframes gradient": {
        "0%": {"background-position": "0% 50%"},
        "50%": {"background-position": "100% 50%"},
        "100%": {"background-position": "0% 50%"},
    },
}

# Estilo para las tarjetas de habilidades
skill_card_style = {
    "background": STYLE_DICT["card_bg"],
    "padding": "2rem",
    "border_radius": "10px",
    "border_bottom": f"3px solid {STYLE_DICT['accent_color']}",
    "transition": "transform 0.3s ease",
    "_hover": {"transform": "translateY(-5px)"}
}