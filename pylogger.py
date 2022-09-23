from cgitb import text
from colors import colors
from datetime import datetime
from enum import Enum
import pytz
import pylogger_settings


class Log:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.modes = pylogger_settings.modes
        self.settings = pylogger_settings.config
        self._setup()

    def _log(self, text, mode):
        """This should only be called directly with custom modes - coming soon"""
        if self.settings.get(mode, {}).get("active", True):
            text = colors.color_text(
                text,
                fg_color=self.settings.get(mode).get(
                    "text_color", self.settings.get("text_color", "")
                ),
            )
            print(
                self.settings.get("output_format", "{prefix}|{text}").format(
                    prefix=self._build_prefix(mode), text=text
                )
            )

    def _get_timestamp(self, mode):
        return (
            datetime.now(tz=self.settings.get("timezone", pytz.utc))
            .time()
            .strftime(self.settings.get(mode).get("time_format", "%H:%M"))
        )

    def _build_prefix(self, mode):
        time_text_color = self.settings.get(mode).get(
            "time_text_color", self.settings.get("time_text_color", "")
        )
        time_bg_color = self.settings.get(mode).get(
            "time_bg_color", self.settings.get("time_bg_color", "")
        )
        timestamp = colors.color_text(
            text=self._get_timestamp(mode),
            fg_color=time_text_color,
            bg_color=time_bg_color,
        )

        identifier_text_color = self.settings.get(mode).get(
            "identifier_text_color", self.settings.get("identifier_text_color", "")
        )
        identifier_bg_color = self.settings.get(mode).get(
            "identifier_bg_color", self.settings.get("identifier_bg_color", "")
        )
        identifier = colors.color_text(
            text=self.identifier,
            fg_color=identifier_text_color,
            bg_color=identifier_bg_color,
        )
        return self.settings.get(
            "output_prefix_format", "{timestamp}|{identifier}"
        ).format(identifier=identifier, timestamp=timestamp)

    def __logger_factory(self, mode):
        def f(self, text):
            self._log(text=text, mode=mode)

        return f

    def _setup(self):
        for mode in self.modes:
            name = str(mode).split(".")[-1].lower()
            new_func = self.__logger_factory(mode)
            if not self.settings.get(mode, False):
                self.settings[mode] = {"active": True}
            setattr(self.__class__, name, new_func)


if __name__ == "__main__":
    logger = Log("KINC")
    logger.info("info!")
    logger.warn(f"warning!")
    logger.verbose("Verbose text")
    logger.error("Error")
    logger.fatal("FATAL")
