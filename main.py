from src.core.config import settings
from src.core.settings._0_gunicorn.gunicorn_app_options import get_app_options
from src.core.settings._0_gunicorn.gunicorn_app import Application
from src.api import app


def main():
    Application(
        application=app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            timeout=settings.gunicorn.timeout,
            workers=settings.gunicorn.workers,
            log_level=settings.logging.log_level,
        ),
    ).run()


if __name__ == "__main__":
    main()
