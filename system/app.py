
# Third party imports
from dash import Dash
import dash_bootstrap_components as dbc
from flask_talisman import Talisman
# Local application/library specific imports
from system.register.layout import register_layout
from system.register.callbacks import register_callbacks

external_stylesheets = [dbc.themes.LUX]

app = Dash(
    __name__,
    external_stylesheets = external_stylesheets,
    # these meta_tags ensure content is scaled correctly on different devices
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.config['suppress_callback_exceptions'] = True

register_layout(app)
register_callbacks(app)


