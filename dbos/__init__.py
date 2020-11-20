__title__ = 'DBOS.py'
__author__ = 'Slimakoi'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020-2020 Wezacon'
__version__ = '0.1.1'

from .client import Client
from .lib.util import objects, exceptions
from requests import get
from json import loads

__newest__ = loads(get("https://pypi.python.org/pypi/dbos.py/json").text)["info"]["version"]

if __version__ != __newest__:
    print(exceptions.LibraryUpdateAvailable(f"New version available: '{__newest__}' (Using: '{__version__}')\nGet latest here: https://pypi.python.org/pypi/dbos.py"))
