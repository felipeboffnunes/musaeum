import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from system.layouts.pages.info.writing_info import poetry

writing_page = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(
        [
            dbc.CardHeader(p["day"], className="poetry-card-header"),
            dbc.CardBody(
                [
                    html.Div(p["title"], className="poetry-card-title"),
                    html.Hr(),
                    html.Div(p["body"], className="poetry-card-text-div"),
                ]
            ),
            dbc.CardFooter(p["date"], className="poetry-card-footer"),
        ], className="writing-card"), className="writing-page-col", width="auto") for p in poetry
    ])
], id="writing-page-div")