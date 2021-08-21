import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

about_page = dbc.Row([

    dbc.Col(html.Img(src="./assets/images/background/left.gif", id="about-right"), width="auto"),
    dbc.Col([
        html.H2("Team", id="team-header"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/images/icons/team_member.png", id="member-icon"),
                            id="member-col",width="auto"),
                    dbc.Col([
                        dbc.Row(html.H5("Felipe Boff Nunes")),
                        dbc.Row(html.H6("pyrrhic buddha")),
                        dbc.Row(html.P("Founder, Software Engineer")),
                    ], width="auto", id="member-row")
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/images/icons/marbitos.png", id="member-icon"), id="member-col", width="auto"),
                    dbc.Col([
                        dbc.Row(html.H6("Marbas Bipu, PhD.")),
                        dbc.Row(html.P("Cyber Security Analyst")),
                    ], width="auto", id="member-row")
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/images/icons/luna.jpg", id="member-icon"), id="member-col", width="auto"),
                    dbc.Col([
                        dbc.Row(html.H6("Luna")),
                        dbc.Row(html.P("IT Consultant")),
                    ], width="auto", id="member-row")
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/images/icons/lilith.jpg", id="member-icon"), id="member-col", width="auto"),
                    dbc.Col([
                        dbc.Row(html.H6("Lilith")),
                        dbc.Row(html.P("Technical Writer")),
                    ], width="auto", id="member-row")
                ], id="team-row"),
            ], width="auto")
        ]),
        html.Hr(),
    ], id="about-content", width="auto"),

    dbc.Col([
        html.H2("Values", id="values-header"),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Row(html.P(
                    "Let us fight for a new world\n"
                )),
                dbc.Row(html.P(
                    "- a decent world, that will give men a chance to work -\n"
                )),
                dbc.Row(html.P(
                    "that will give youth a future and old age a security.\n"
                )),
                dbc.Row(html.P(
                    "By the promise of these things, brutes have risen to power.\n"
                )),
                dbc.Row(html.P(
                    "But they lie. They do not fulfil that promise. They never will.\n"
                )),
                dbc.Row(html.P(
                    "Dictators free themselves, but they enslave the people.\n"
                )),
                dbc.Row(html.P(
                    "Now let us fight to fulfil that promise!\n"
                )),
                dbc.Row(html.P(
                    "Let us fight to free the world\n"
                )),
                dbc.Row(html.P(
                    "- to do away with national barriers -\n"
                )),
                dbc.Row(html.P(
                    "to do away with greed, with hate and intolerance.\n"
                )),
                dbc.Row(html.P(
                    "Let us fight for a world of reason,\n"
                )),
                dbc.Row(html.P(
                    "a world where science and progress\n"
                )),
                dbc.Row(html.P(
                    "will lead to all men’s happiness.\n"
                )),
                dbc.Row(html.P(
                    "Let us all unite!"
                ))
            ])
        ], id="about-paragraph"),
    ], id="management-content", width="auto"),
    dbc.Col(html.Img(src="./assets/images/background/right.gif", id="about-left"), width="auto"),
], id="about-page", justify="between")
