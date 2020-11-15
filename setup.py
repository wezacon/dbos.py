from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = 'DBOS.py',
    version = '0.0.8',
    url = 'https://github.com/wezacon/dbos.py',
    download_url = 'https://github.com/wezacon/dbos.py/tarball/master',
    license = 'MIT',
    author = 'Slimakoi',
    author_email = 'slimeytoficial@gmail.com',
    description = 'API wrapper for DBOS',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = [
        'dbos',
        'dbos-py',
        'wezacon',
        'slimakoi'
        'official'
    ],
    install_requires = [
        'setuptools',
        'requests',
        'six',
        'ujson'
    ],
    setup_requires = [
        'wheel'
    ],
    packages = find_packages()
)
