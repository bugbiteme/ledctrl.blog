try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Control RaspPi GPIO LEDs via a web interface',
    'author': 'Leon Levy',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'leon.s.levy@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ledctrl'],
    'scripts': [],
    'name': 'ledctrl'
}

setup(**config)
