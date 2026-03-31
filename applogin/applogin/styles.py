import reflex as rx
from applogin.models import User
from typing import Optional

# Colores Oficiales AdminLTE
COLORS = {
    "sidebar_bg": "#343a40",
    "content_bg": "#78879d",
    "primary": "#007bff",
    "info": "#17a2b8",
    "success": "#28a745",
    "text_muted": "#777f8f",
}

# Estilo de tarjeta (Small Box)
CARD_STYLE = {
    "padding": "1.5rem",
    "border_radius": "0.25rem",
    "box_shadow": "0 0 1px rgba(0,0,0,.125), 0 1px 3px rgba(0,0,0,.2)",
    "color": "white",
}
import reflex as rx
from applogin.models import User
from typing import Optional

class AuthState(rx.State):
    # Usamos rx.LocalStorage o rx.Cookie para que la sesión no se pierda al recargar
    user: Optional[User] = None 

    def login(self, form_data: dict):
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    (User.username == form_data["username"]) & 
                    (User.password == form_data["password"])
                )
            ).first()
            if user:
                self.user = user
                return rx.redirect("/dashboard") # Redirige al éxito
            return rx.window_alert("Error de acceso")

    def logout(self):
        self.user = None
        return rx.redirect("/")