import reflex as rx

config = rx.Config(
    app_name="applogin",
    db_url="mysql+pymysql://root:@localhost/reflex_app", # Ajusta tus credenciales
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)