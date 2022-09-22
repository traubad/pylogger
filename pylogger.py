from colors import colors
from datetime import datetime
from enum import Enum
import pytz

class Log():
    def __init__(self, identifier:str):
        self.identifier = identifier
        self.modes = Enum('Mode', 'INFO VERBOSE WARN ERROR FATAL')
        self.settings = {
            self.modes.INFO: {
                'active': True,
                'text_color' : colors.fg.green,
            },
            self.modes.VERBOSE: {
                'active':True,
                'text_color' : colors.fg.purple,
            },
            self.modes.WARN: {
                'active':True,
                'text_color' : colors.fg.yellow,
            },
            self.modes.ERROR: {
                'active':True,
                'text_color' : colors.fg.red,
            },
            self.modes.FATAL: {
                'active':True,
                'identifier_text_color': colors.fg.red,
                'text_color' : colors.fg.red,
                'time_text_color': colors.fg.red,
            },
            'identifier_text_color': colors.fg.blue,
            'output_prefix_format': '[{timestamp}][{identifier}]',
            'output_format': '{prefix} {text}',
            'timezeone': pytz.timezone("US/Eastern"),
            'time_format':'%H:%M',
            'time_text_color': colors.fg.red,
            'text_color': colors.fg.darkgrey,
        }

    def log(self, text, mode):
        """This should only be called directly with custom modes - coming soon"""
        if self.settings.get(mode).get('active',False):
            text = colors.color_text(text, fg_color=self.settings.get(mode).get('text_color',self.settings.get('text_color', '')))
            print(self.settings.get('output_format','{prefix}|{text}').format(prefix=self._build_prefix(mode),text=text))

    def _get_timestamp(self, mode):
        return datetime.now(tz=self.settings.get('timezone', pytz.utc)).time().strftime(self.settings.get(mode).get('time_format', '%H:%M'))

    def _build_prefix(self, mode):
        time_text_color = self.settings.get(mode).get('time_text_color',self.settings.get('time_text_color',''))
        time_bg_color = self.settings.get(mode).get('time_bg_color',self.settings.get('time_bg_color',''))
        timestamp = colors.color_text(text=self._get_timestamp(mode), fg_color=time_text_color, bg_color=time_bg_color)

        identifier_text_color = self.settings.get(mode).get('identifier_text_color',self.settings.get('identifier_text_color',''))
        identifier_bg_color = self.settings.get(mode).get('identifier_bg_color',self.settings.get('identifier_bg_color',''))
        identifier = colors.color_text(text=self.identifier, fg_color=identifier_text_color, bg_color=identifier_bg_color)
        return self.settings.get('output_prefix_format','{timestamp}|{identifier}').format(identifier=identifier,timestamp=timestamp)

    def info(self, text):
        self.log(text=text, mode=self.modes.INFO)

    def warn(self, text):
        self.log(text=text, mode=self.modes.WARN)

    def verbose(self, text):
        self.log(text=text, mode=self.modes.VERBOSE)

    def error(self, text):
        self.log(text=text, mode=self.modes.ERROR)

    def fatal(self, text):
        self.log(text=text, mode=self.modes.FATAL)

logger = Log('KINC')
logger.info('info!')
x=5
logger.warn(f"warning: formatted Strings x={x}")
logger.verbose("Verbose text")
logger.error('Error')
logger.fatal("RUN FOR YOUR LIVES!")