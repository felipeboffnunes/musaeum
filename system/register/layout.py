import dash_core_components as dcc
import dash_html_components as html

def register_layout(app):
        layout = html.Div([
                    html.Div()
                    ])
        
        app.layout = html.Div([dcc.Location(id="url"), layout], id="layout")
