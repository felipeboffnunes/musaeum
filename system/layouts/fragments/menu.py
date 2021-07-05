import dash_bootstrap_components as dbc
import dash_html_components as html


def get_sidebar(collapse: bool = False):
    if collapse:
        collapsed = "collapsed"
    else:
        collapsed = "simple",

    sidebar_header = dbc.Row(
        [
            dbc.Col(html.P("Musaeum"), id="musaeum-header"),
            dbc.Col(
                [
                    html.Button(
                        html.Span(className="navbar-toggler-icon"),
                        className="navbar-toggler",
                        style={
                            "color": "rgba(0,0,0,.5)",
                            "border-color": "rgba(0,0,0,.1)",
                        },
                        id="navbar-toggle",
                    ),
                    html.Button(
                        html.Span(className="navbar-toggler-icon"),
                        className="navbar-toggler",
                        style={
                            "color": "rgba(0,0,0,.5)",
                            "border-color": "rgba(0,0,0,.1)",
                        },
                        id="sidebar-toggle",
                    ),
                ],
                width="auto",
                align="center",
            ),
        ]
    )

    sidebar = html.Div(
        [
            sidebar_header,
            html.Hr(id="line-logo"),
            html.P("not a university"),

            html.Div(
                [
                    html.Hr(),
                ],
                id="blurb",
            ),

            dbc.Collapse([
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/home", active="exact"),
                        dbc.NavLink("About", href="/about", active="exact"),
                        dbc.NavLink("Wiki", href="https://wiki.musaeum.university")
                    ],
                    vertical=True,
                    pills=True,
                ),
                html.Div([
                    html.Hr(id="line-logo"),
                    dbc.Col(html.P("Pyrrhic Buddha", id="pyrrhic-header")),
                    dbc.Nav(
                        [
                            dbc.NavLink("Library", href="/library", active="exact"),
                            dbc.NavLink("Logbook", href="/logbook", active="exact"),
                            dbc.NavLink("Writing", href="/writing", active="exact"),
                        ],
                        vertical=True,
                        pills=True,
                    )
                ], id="pyrrhic-sidebar")
            ],
                id="collapse",
            ),
        ],
        className=collapsed if isinstance(collapsed, str) else collapsed[0],
        id="sidebar",
    )

    return sidebar
