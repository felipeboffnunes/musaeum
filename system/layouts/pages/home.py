
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

home_page = html.Div([
    html.Video(
        src="./assets/images/background/home_babel.webm",
        autoPlay=True,
        loop=True,
        muted=True,
        poster="./assets/images/icons/loading.gif",
        id="home-background"
        ),
    html.Div([
        html.Span("I am building a tower."),
        html.Br(),
        html.Span("Upwards; Inwards.")
    ], id="home-header-text"),
    html.Div([
        html.P("They said, Go to, let us build us a city and a tower, whose top may reach unto heaven; and let us make us a name, lest we be scattered abroad upon the face of the whole earth.\n"),
        html.P("And the LORD came down to see the city and the tower, which the children of men builded.\n"),
        html.P("And the LORD said, Behold, the people is one, and they have all one language; and this they begin to do: and now nothing will be restrained from them, which they have imagined to do.\n"),
        html.P("Go to, let us go down, and there confound their language, that they may not understand one another's speech.\n"),
        html.P("So the LORD scattered them abroad from thence upon the face of all the earth: and they left off to build the city.")
    ], id="home-paragraph"),
    html.Div(id="home-black-background")
], id="home-page")