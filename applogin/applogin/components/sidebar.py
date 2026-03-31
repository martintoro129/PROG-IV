import reflex as rx

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.heading("SISTEMA", color="white", size="6", padding="1.5rem"),
        rx.vstack(
            rx.link("Dashboard", href="/dashboard", color="white", padding="0.75rem"),
            rx.link("Usuarios", href="/users", color="#3b82f6", padding="0.75rem", font_weight="bold"),
            width="100%",
            align_items="start",
            padding="1rem",
        ),
        width="250px",
        height="100vh",
        bg="#1e293b",
        position="fixed", # Cambiado a fixed para asegurar visibilidad
        left="0",
        top="0",
        z_index="100",
    )