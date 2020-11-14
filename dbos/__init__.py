__title__ = 'DBOS.py'
__author__ = 'Slimakoi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2020 Wezacon'
__version__ = '0.0.1'

from .client import Client
from .lib.util import objects
from requests import get
from json import loads

__newest__ = loads(get("https://pypi.python.org/pypi/dbos.py/json").text)["info"]["version"]


class LibraryUpdateAvailable(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)


if __version__ != __newest__:
    raise LibraryUpdateAvailable(f"New version available: '{__newest__}'")
