def sidebar_item(text: str, icon: str, url: str, active: bool = False):
    return rx.link(
        rx.hstack(
            rx.icon(tag=icon, size=18),
            rx.text(text, size="2"),
            padding="10px 20px",
            color="white" if active else "#c2c7d0",
            background_color="#343a40" if not active else "#007bff",
            border_radius="5px",
            _hover={"background_color": "rgba(255,255,255,0.1)"},
            width="100%",
        ),
        href=url,
        width="100%",
    )

def admin_layout(content: rx.Component):
    return rx.hstack(
        # Sidebar estilo AdminLTE
        rx.vstack(
            rx.heading("AdminLTE RX12", size="5", color="white", padding="20px"),
            sidebar_item("Dashboard", "layout_dashboard", "/dashboard", active=True),
            sidebar_item("Usuarios", "users", "/usuarios"),
            rx.cond(
                AuthState.is_admin,
                sidebar_item("Configuración", "settings", "/config"),
            ),
            rx.spacer(),
            rx.button("Cerrar Sesión", on_click=AuthState.logout, color_scheme="red", width="90%"),
            width="250px",
            height="100vh",
            background_color="#343a40",
            spacing="1",
            padding="10px",
        ),
        # Área de Contenido
        rx.vstack(
            rx.box(content, width="100%", padding="2rem"),
            width="100%",
            height="100vh",
            background_color="#f4f6f9",
            overflow_y="auto",
        ),
        spacing="0",
        width="100%",
    )