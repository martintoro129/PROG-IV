import reflex as rx
from applogin.state import AuthState
from applogin.models import User
# Importamos las vistas de las páginas
from applogin.pages.login import login_page
from applogin.pages.dashboard import dashboard_page
from applogin.pages.users import users_page

def index() -> rx.Component:
    # Lógica de acceso: Si no hay usuario, muestra Login. Si hay, redirige.
    return rx.cond(
        AuthState.user,
        rx.fragment(), # El evento on_mount se encarga de redirigir
        login_page(),
    )

app = rx.App()

# REGISTRO DE RUTAS (Punto Crítico)
app.add_page(login_page, route="/login")
app.add_page(index, route="/")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(users_page, route="/users")