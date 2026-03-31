import reflex as rx
from ..state import AuthState
from ..styles import COLORS, CARD_STYLE

def sidebar_item(text, icon, url, protected=False):
    # Si es protegida y no es admin, no se renderiza
    return rx.cond(
        protected & ~AuthState.is_admin,
        rx.fragment(),
        rx.link(
            rx.hstack(
                rx.icon(tag=icon, size=18),
                rx.text(text),
                color=COLORS["text_muted"],
                _hover={"color": "white", "background": "rgba(255,255,255,0.1)"},
                padding="10px",
                border_radius="5px",
            ),
            href=url,
            text_decoration="none",
            width="100%",
        )
    )

def dashboard_page():
    return rx.hstack(
        # SIDEBAR
        rx.vstack(
            rx.heading("AdminLTE RX", color="white", size="5", margin_bottom="2rem"),
            sidebar_item("Dashboard", "layout_dashboard", "/dashboard"),
            sidebar_item("Usuarios (Solo Admin)", "users", "/users", protected=True),
            rx.spacer(),
            rx.button("Cerrar Sesión", on_click=AuthState.logout, color_scheme="red", width="100%"),
            width="250px",
            height="100vh",
            bg=COLORS["sidebar_bg"],
            padding="1rem",
        ),
        # CONTENIDO
        rx.vstack(
            rx.heading(f"Bienvenido, {AuthState.user.username}"),
            rx.text(f"Rol: {AuthState.user.role}"),
            rx.divider(),
            rx.grid(
                rx.box(rx.text("Órdenes"), bg=COLORS["info"], style=CARD_STYLE),
                rx.box(rx.text("Ventas"), bg=COLORS["success"], style=CARD_STYLE),
                rx.box(rx.text("Usuarios"), bg=COLORS["primary"], style=CARD_STYLE),
                columns="3", spacing="4", width="100%"
            ),
            # Lógica Editor
            rx.cond(
                AuthState.can_edit,
                rx.button("Crear Nuevo Registro", color_scheme="blue", margin_top="2rem"),
                rx.callout("Modo Lectura: No tienes permisos para editar.", icon="info_circulo", color_scheme="gray")
            ),
            width="100%",
            bg=COLORS["content_bg"],
            height="100vh",
            padding="2rem",
        ),
        spacing="0",
    )