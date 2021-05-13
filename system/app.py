
# Third party imports
from dash import Dash
import dash_bootstrap_components as dbc

# Local application/library specific imports
from system.register.layout import register_layout

external_stylesheets = [dbc.themes.LUX]

app = Dash(
    __name__,
    external_stylesheets = external_stylesheets,
)

app.config['suppress_callback_exceptions'] = True

register_layout(app)

