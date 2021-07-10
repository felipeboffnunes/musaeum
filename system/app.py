from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from system.register.callbacks import register_callbacks

external_stylesheets = [dbc.themes.LUX]

app = Dash(
    __name__,
    title='Musaeum',
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([dcc.Location(id="url"), html.Div(id="inner-layout")], id="layout")

register_callbacks(app)
