# Local application/library specific imports
from .hero import hero_page
from .home import home_page
from .library import library_page
from .logbook import logbook_page
from .writing import writing_page
from .about import about_page

pages = {
    "HER": hero_page,
    "HOM": home_page,
    "LIB": library_page,
    "LOG": logbook_page,
    "WRT": writing_page,
    "ABT": about_page
}