import reflex as rx
from applogin.models import User
from applogin.state import AuthState
from ..components.layout import admin_layout # Importamos el layout

class UsersState(rx.State):
    users: list[User] = []
    # Control de Modales
    is_register_open: bool = False
    is_edit_open: bool = False
    
    # Objeto temporal para edición
    user_to_edit: User = User()

    def get_all_users(self):
        with rx.session() as session:
            self.users = session.exec(User.select()).all()

    # --- MODAL REGISTRO ---
    def toggle_register_modal(self):
        self.is_register_open = not self.is_register_open

    def add_user(self, form_data: dict):
        new_user = User(**form_data)
        with rx.session() as session:
            session.add(new_user)
            session.commit()
        self.is_register_open = False # CIERRE EXPLÍCITO
        return self.get_all_users()

    # --- MODAL EDICIÓN ---
    def prepare_edit(self, user: User):
        """Carga los datos del usuario en el modal de edición"""
        self.user_to_edit = user
        self.is_edit_open = True

    def toggle_edit(self):
        self.is_edit_open = not self.is_edit_open

    def update_user(self, form_data: dict):
        """Actualiza el registro en MySQL"""
        with rx.session() as session:
            user = session.exec(User.select().where(User.id == self.user_to_edit.id)).first()
            if user:
                user.username = form_data["username"]
                user.email = form_data["email"]
                user.role = form_data["role"]
                session.add(user)
                session.commit()
        self.is_edit_open = False # CIERRE EXPLÍCITO
        return self.get_all_users()
    
    # --- CRUD: ELIMINAR ---
    def delete_user(self, id: int):
        with rx.session() as session:
            user = session.exec(User.select().where(User.id == id)).first()
            if user:
                session.delete(user)
                session.commit()
        return self.get_all_users()


# --- COMPONENTE: FILA DE LA TABLA ---
def render_user_row(user: User):
    """Esta es la función que faltaba definir"""
    return rx.table.row(
        rx.table.cell(user.id),
        rx.table.cell(user.username),
        rx.table.cell(user.email),
        rx.table.cell(
            rx.badge(
                user.role, 
                color_scheme=rx.cond(user.role == "Admin", "red", "blue"),
                variant="surface"
            )
        ),
        rx.table.cell(
            rx.hstack(
                # BOTÓN EDITAR
                rx.button(
                    rx.icon(tag="pencil"), 
                    on_click=lambda: UsersState.prepare_edit(user),
                    color_scheme="yellow", size="1"
                ),
                # BOTÓN ELIMINAR
                rx.button(
                    rx.icon(tag="trash", size=16), 
                    on_click=lambda: UsersState.delete_user(user.id),
                    size="1", 
                    color_scheme="red",
                    variant="soft"
                ),
                spacing="2"
            )
        ),
    )

def create_user_form() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Registrar Nuevo Usuario", size="3", margin_bottom="1rem"),
            rx.form(
                rx.flex(
                    # Quitamos 'variant' y cualquier argumento extra que pueda causar conflicto
                    rx.input(placeholder="Username", name="username"),
                    rx.input(placeholder="Password", name="password", type="password"),
                    rx.input(placeholder="Email", name="email"),
                    rx.select(
                        ["Admin", "Editor", "Guest"],
                        name="role",
                        default_value="Guest",
                    ),
                    rx.button(
                        "Guardar", # Texto simple para evitar errores de hstack/icon internos
                        type="submit",
                        color_scheme="blue",
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                ),
                on_submit=UsersState.add_user,
            ),
        ),
        background_color="white",
        padding="1.5rem",
        border_radius="8px",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)",
        margin_bottom="2rem",
        width="100%",
    )
def edit_user_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(f"Editar Usuario: {UsersState.user_to_edit.username}"),
            rx.form(
                rx.vstack(
                    rx.text("Nombre de Usuario"),
                    rx.input(name="username", default_value=UsersState.user_to_edit.username, width="100%"),
                    rx.text("Email"),
                    rx.input(name="email", default_value=UsersState.user_to_edit.email, width="100%"),
                    rx.text("Rol"),
                    rx.select(["Admin", "Editor", "Guest"], name="role", default_value=UsersState.user_to_edit.role, width="100%"),
                    rx.hstack(
                        rx.button("Cancelar", on_click=UsersState.toggle_edit, variant="soft"),
                        rx.button("Actualizar", type="submit", color_scheme="blue"),
                        justify="end", width="100%", margin_top="1rem"
                    ),
                    spacing="3", align_items="start"
                ),
                on_submit=UsersState.update_user,
            ),
        ),
        open=UsersState.is_edit_open,
        on_open_change=UsersState.toggle_edit,
    )
def register_user_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon(tag="plus"), 
                rx.text("Nuevo Usuario"),
                color_scheme="green",
                on_click=UsersState.toggle_register_modal
            ),
        ),
        rx.dialog.content(
            rx.dialog.title("Crear Nuevo Registro"),
            rx.dialog.description("Introduce los datos para el nuevo acceso al sistema."),
            rx.form(
                rx.vstack(
                    rx.text("Nombre de Usuario", font_weight="bold"),
                    rx.input(name="username", placeholder="Ej: mtoro", width="100%"),
                    
                    rx.text("Contraseña", font_weight="bold"),
                    rx.input(name="password", type="password", placeholder="********", width="100%"),
                    
                    rx.text("Correo Electrónico", font_weight="bold"),
                    rx.input(name="email", placeholder="correo@ejemplo.com", width="100%"),
                    
                    rx.text("Rol de Usuario", font_weight="bold"),
                    rx.select(
                        ["Admin", "Editor", "Guest"],
                        name="role",
                        default_value="Guest",
                        width="100%",
                    ),
                    
                    rx.hstack(
                        rx.dialog.close(
                            rx.button("Cancelar", 
                                      on_click=UsersState.toggle_register_modal, 
                                      variant="soft", 
                                      color_scheme="gray",
                                      type="button"
                                      )
                        ),
                        rx.button("Guardar Usuario", type="submit", color_scheme="blue"),
                        width="100%",
                        justify="end",
                        margin_top="1rem",
                    ),
                    align_items="start",
                    spacing="3",
                ),
                on_submit=UsersState.add_user,
            ),
            style={"max_width": "450px"},
        ),
        # ESTO VINCULA LA VENTANA AL ESTADO DE PYTHON
        open=UsersState.is_register_open,
        #on_open_change=UsersState.toggle_register_modal,
    )


# --- PÁGINA PRINCIPAL DE USUARIOS ---
@rx.page(route="/users", title="Users")
def users_page() -> rx.Component:
    return admin_layout(
        rx.vstack(
            # CABECERA DE LA PÁGINA
            rx.flex(
                rx.heading("Gestión de Usuarios", size="8"),
                rx.spacer(),
                rx.hstack(
                    # BOTÓN PARA VOLVER AL DASHBOARD
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.icon(tag="layout-dashboard", size=18),
                                rx.text("Dashboard")
                            ),
                            color_scheme="gray",
                            variant="soft",
                        ),
                        href="/dashboard", # Asegúrate de que esta sea la ruta en app.add_page
                    ),
                    # BOTÓN PARA NUEVO USUARIO (El modal que ya definimos)
                    register_user_modal(),
                    spacing="3",
                ),
                width="100%",
                align_items="center",
                margin_bottom="2rem",
            ),
            # Tabla de Datos
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("ID"),
                            rx.table.column_header_cell("Usuario"),
                            rx.table.column_header_cell("Email"),
                            rx.table.column_header_cell("Rol"),
                            rx.table.column_header_cell("Acciones"),
                        ),
                    ),
                    rx.table.body(
                        rx.foreach(UsersState.users, render_user_row)
                    ),
                    width="100%",
                    variant="surface",
                    color="black",
                ),
                background_color="lightgray",
                padding="1rem",
                border_radius="8px",
                width="100%",
            ),
            # Modal de Edición
            edit_user_modal(),
            padding="2rem",
            bg="lightgray",
        ),
        on_mount=UsersState.get_all_users,
    )

