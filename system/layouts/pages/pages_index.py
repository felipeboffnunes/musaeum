# Local application/library specific imports
from .hero import hero_page
from .home import home_page
from .library import library_page
from .logbook import logbook_page


pages = {
    "HER": hero_page,
    "HOM": home_page,
    "LIB": library_page,
    "LOG": logbook_page,
}