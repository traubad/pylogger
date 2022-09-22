from colors import colors
from enum import Enum
import pytz

modes = Enum("Mode", "INFO VERBOSE WARN ERROR FATAL")

config = {
    modes.INFO: {
        "active": True,
        "text_color": colors.fg.green,
    },
    modes.VERBOSE: {
        "active": True,
        "text_color": colors.fg.purple,
    },
    modes.WARN: {
        "active": True,
        "text_color": colors.fg.yellow,
    },
    modes.ERROR: {
        "active": True,
        "text_color": colors.fg.red,
    },
    modes.FATAL: {
        "active": True,
        "identifier_text_color": colors.fg.red,
        "text_color": colors.fg.red,
        "time_text_color": colors.fg.red,
    },
    "identifier_text_color": colors.fg.blue,
    "output_prefix_format": "[{timestamp}][{identifier}]",
    "output_format": "{prefix} {text}",
    "timezeone": pytz.timezone("US/Eastern"),
    "time_format": "%H:%M",
    "time_text_color": colors.fg.red,
    "text_color": colors.fg.darkgrey,
}
