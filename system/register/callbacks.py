
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
# Local application/library specific imports
from system.layouts.pages.pages_index import pages
from system.layouts.fragments.menu import sidebar

def register_callbacks(app):

    # Navigator
    #
    @app.callback(Output("inner-layout", "children"), [Input("url", "pathname")])
    def render_page_content(pathname): 
        if pathname == "/":
            content = html.Div([pages["HER"]], id="page-content")
            return None, content
        elif pathname == "/home":
            content = html.Div([pages["HOM"]], id="page-content")
            return sidebar, content
        elif pathname == "/library":
            content = html.Div([pages["LIB"]], id="page-content")
            return sidebar, content
        elif pathname == "/logbook":
            content = html.Div([pages["LOG"]], id="page-content")
            return sidebar, content
        # If the user tries to reach a different page, return a 404 message
        return sidebar, html.Div([dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )], id="page-content")
        
    # Collapse Sidebar
    #
    @app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
    )
    def toggle_classname(n, classname):
        if n and classname == "":
            return "collapsed"
        return ""
    #
    # 
    @app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
