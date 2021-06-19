# Third party imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
# Local application/library specific imports
from system.layouts.pages.pages_index import pages
from system.layouts.fragments.menu import sidebar
from system.layouts.pages.info.logbook_handler import LogBook_Handler
from system.layouts.pages.info.library_info import authors

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
        elif pathname == "/writing":
            content = html.Div([pages["WRT"]], id="page-content")
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
    
    # Logbook
    #
    @app.callback(
    Output("logbook-div", "children"),
    [Input("day-picker", "date")]
    )
    def update_health(date_str):
        lg_handler = LogBook_Handler()
        return lg_handler.consume_data(date_str)
    #
    # Logbook Modal
    #
    @app.callback(
    [Output("logbook-act-modal", "is_open"),
     Output("logbook-act-modal-body", "children"),
     Output("logbook-act-modal-header", "children")],
    Input("ACTINFO", "n_clicks"),
    State("day-picker", "date")
    )
    def open_activities_modal(act_clicks, date_str):
        if act_clicks:
            lg_handler = LogBook_Handler()
            return [True, lg_handler.graphs(date_str, "ACT"), "ACTION"]
        return [dash.no_update, dash.no_update, dash.no_update]
    #
    @app.callback(
    [Output("logbook-stu-modal", "is_open"),
     Output("logbook-stu-modal-body", "children"),
     Output("logbook-stu-modal-header", "children")],
    Input("STUINFO", "n_clicks"),
    State("day-picker", "date")
    )
    def open_studies_modal(stu_clicks, date_str):
        if stu_clicks:
            return [True, "STUINFO", "STUINFO-yes"]
        return [dash.no_update, dash.no_update, dash.no_update]
    #
    @app.callback(
    [Output("logbook-nut-modal", "is_open"),
     Output("logbook-nut-modal-body", "children"),
     Output("logbook-nut-modal-header", "children")],
    Input("NUTINFO", "n_clicks"),
    State("day-picker", "date")
    )
    def open_nutrition_modal(nut_clicks, date_str):
        if nut_clicks:
            return [True, "NUTINFO", "NUTINFO-yes"]
        return [dash.no_update, dash.no_update, dash.no_update]
    #
    @app.callback(
    [Output("logbook-exe-modal", "is_open"),
     Output("logbook-exe-modal-body", "children"),
     Output("logbook-exe-modal-header", "children")],
    Input("EXEINFO", "n_clicks"),
    State("day-picker", "date")
    )
    def open_exercises_modal(exe_clicks, date_str):
        if exe_clicks:
            lg_handler = LogBook_Handler()
            return [True, lg_handler.graphs(date_str, "EXE"), "EXER"]
        return [dash.no_update, dash.no_update, dash.no_update]
    
    # Library
    #
    @app.callback(
    [Output("library-modal", "is_open"),
     Output("library-modal-body", "children"),
     Output("library-modal-header", "children")],
    [Input("library-datatable", "active_cell"),
     Input("library-datatable", "derived_viewport_data")]
    )
    def update_library_modal(active_cell, data):
        print(active_cell)
        if active_cell is None:
            return [dash.no_update, dash.no_update, dash.no_update]
        if active_cell["column"] == 1:
            return [True, authors[data[active_cell["row"]]["Author"]]["description"], data[active_cell["row"]]["Author"]]
        return [dash.no_update, dash.no_update, dash.no_update]