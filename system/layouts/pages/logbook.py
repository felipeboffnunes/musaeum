import dash_html_components as html

from system.layouts.pages.info.logbook_handler import LogBook_Handler

lg_handler = LogBook_Handler()

logbook_page = html.Div(lg_handler.consume_data("2021-06-04"), id="logbook-div")