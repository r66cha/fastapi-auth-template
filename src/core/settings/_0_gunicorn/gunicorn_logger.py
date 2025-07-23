from logging import Formatter
from gunicorn.glogging import Logger
from src.core.config import settings


class GunicornLogger(Logger):
    def setup(self, cfg):
        super().setup(cfg)

        self._set_handler(
            log=self.access_log,
            output=cfg.accesslog,
            fmt=Formatter(fmt=settings.logging.log_format),
        )

        self._set_handler(
            log=self.access_log,
            output=cfg.errorlog,
            fmt=Formatter(fmt=settings.logging.log_format),
        )
