import reflex as rx
from .models import User

class AuthState(rx.State):
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
                return rx.redirect("/dashboard")
            return rx.window_alert("Credenciales incorrectas")

    def logout(self):
        self.user = None
        return rx.redirect("/login")

    @rx.var
    def is_admin(self) -> bool:
        return self.user is not None and self.user.role == "Admin"

    @rx.var
    def can_edit(self) -> bool:
        return self.user is not None and self.user.role in ["Admin", "Editor"]