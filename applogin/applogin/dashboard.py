def dashboard_page():
    return admin_layout(
        rx.vstack(
            rx.heading(f"Bienvenido, {AuthState.user.username} ({AuthState.user.role})"),
            
            rx.grid(
                # Tarjetas de estadísticas (Widgets AdminLTE)
                rx.box(rx.text("Ventas"), background="white", padding="20px", border_top="4px solid #007bff"),
                rx.box(rx.text("Usuarios"), background="white", padding="20px", border_top="4px solid #28a745"),
                columns="3", spacing="4", width="100%"
            ),

            rx.cond(
                AuthState.can_edit,
                rx.button("Nueva Entrada (Editor/Admin)", color_scheme="blue"),
                rx.text("Modo lectura (Guest)", color="red")
            ),
            
            rx.cond(
                AuthState.is_admin,
                rx.vstack(
                    rx.heading("Panel de Control Maestro", size="4"),
                    rx.text("Solo tú puedes ver esto."),
                    background="white", padding="20px", width="100%"
                )
            )
        )
    )