# Python Standard Library
from datetime import date
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Local application/library specific imports
from system.layouts.pages.info.logbook_handler import LogBook_Handler

lg_handler = LogBook_Handler()

logbook_page = html.Div(lg_handler.consume_data("2021-06-04"), id="logbook-div")