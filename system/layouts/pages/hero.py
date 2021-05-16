
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

hero_page = html.Div([
    html.Div([
        html.Img(src="./assets/images/icons/hero-pyrrhic.gif", id="hero-pyrrhic"),
        html.H1("MUSAEUM"),
        html.Hr(),
        html.P("by pyrrhic buddha"),
        dbc.NavLink("ENTER", href="/home", active="exact", id="hero-button"),
    ], id="hero-title-div")
], className="row", id="hero-page")