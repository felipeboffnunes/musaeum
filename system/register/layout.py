
# Third party imports
import dash_core_components as dcc
import dash_html_components as html

# Local application/library specific imports
from system.layouts.menu import sidebar

def register_layout(app):
        content = html.Div(id="page-content")
        app.layout = html.Div([dcc.Location(id="url"), sidebar, content], id="layout")
