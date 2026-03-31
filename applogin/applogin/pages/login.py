import reflex as rx
from applogin.state import AuthState
from applogin.styles import COLORS  # Asegúrate de tener definidos los colores

def login_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Logo / Título estilo AdminLTE
            rx.heading("APP", color="#495057", size="8", font_weight="300"),
            rx.heading("LOGIN", color="#495057", size="8", font_weight="700", margin_bottom="1rem"),
            
            # Caja del Formulario (Card)
            rx.box(
                rx.vstack(
                    rx.text("Ingresa tus credenciales", color="#666", margin_bottom="1rem", text_align="center"),
                    
                    rx.form(
                        rx.vstack(
                            # Campo Usuario
                            rx.hstack(
                                rx.input(
                                    placeholder="Usuario", 
                                    name="username", 
                                    type="text",
                                    border_radius="0",
                                    border_right="none",
                                    width="100%"
                                ),
                                rx.center(
                                    rx.icon(tag="user", color="#adb5bd"),
                                    border="1px solid #ced4da",
                                    border_left="none",
                                    padding_x="10px",
                                ),
                                width="100%",
                                spacing="0",
                            ),
                            
                            # Campo Password
                            rx.hstack(
                                rx.input(
                                    placeholder="Contraseña", 
                                    name="password", 
                                    type="password",
                                    border_radius="0",
                                    border_right="none",
                                    width="100%"
                                ),
                                rx.center(
                                    rx.icon(tag="lock", color="#adb5bd"),
                                    border="1px solid #ced4da",
                                    border_left="none",
                                    padding_x="10px",
                                ),
                                width="100%",
                                spacing="0",
                            ),
                            
                            # Botón de Ingreso
                            rx.button(
                                "Iniciar Sesión", 
                                type="submit",
                                width="100%",
                                background_color="#007bff",
                                color="white",
                                _hover={"background_color": "#0069d9"},
                                border_radius="4px",
                                margin_top="1rem"
                            ),
                            spacing="4",
                        ),
                        on_submit=AuthState.login,
                        width="100%",
                    ),
                    spacing="2",
                ),
                # Estilo de la "Card" de AdminLTE
                background_color="white",
                padding="2rem",
                border_radius="2px",
                box_shadow="0 0 1px rgba(0,0,0,.125), 0 1px 3px rgba(0,0,0,.2)",
                width="360px",
            ),
            align="center",
            spacing="0",
        ),
        # Fondo gris azulado típico de AdminLTE Login
        background_color="#e9ecef",
        height="100vh",
        width="100%",
    )