import reflex as rx

config = rx.Config(
    app_name="base",
    #app_name="portfolio",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)