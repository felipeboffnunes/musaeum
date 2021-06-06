# Python Standard Library
from datetime import date
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Local application/library specific imports
from system.layouts.fragments.calendar_heatmap import calendar_heatmap

logbook_page = html.Div([
    # Day
    html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Col(html.H1("8766", id="day-old")),
                dcc.DatePickerSingle(
                    date=date(2021, 6, 5),
                    id='day-picker'
                )
            ], width = 2, id="header-days"),
            calendar_heatmap,
        ]),
    ], id="day-div"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            #Activities
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.Img(src="./assets/images/icons/dog-side.svg", className="activity-icon"), width=2),
                        dbc.Col(html.H3("Walked Marbas", className="activity-header"), width=5),
                        dbc.Col(html.P("1Km - 15 min", className="activity-details"), width=5)
                    ], className="activity-row"),
                ], id="activities-col"),
            ]),
            html.Hr(),
            #Studies
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.Img(src="./assets/images/icons/book.svg", className="study-icon"), width=2),
                        dbc.Col(html.H3("Read 50 pages", className="study-header"), width=5),
                        dbc.Col(html.P("2 hours", className="study-details"), width=5)
                    ], className="study-div")
                ], id="studies-col")
            ])
        ], width = 4),
        
        dbc.Col([
            #Nutrition
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.H3("2300", id="nutrition=calories-n"), width=2),
                        dbc.Col(html.P("calories consumed", id="nutrition-calories-consumed")),
                    ]),
                    dbc.Row([
                        dbc.Col(dbc.Progress(value=74, id="nutrition-calories-progress"))
                    ])
                ])
            ]),
            html.Hr(),
            #Exercise
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(html.H3("2150", id="basal=calories-n"), width=2),
                        dbc.Col(html.P("calories burned", id="nutrition-calories-burned")),
                    ]),
                    dbc.Row([
                        dbc.Col(dbc.Progress(value=91, id="exercise-calories-progress"))
                    ])
                ])
            ])
        ], width=5)
    ], justify="between",)
    
], id="logbook-div")