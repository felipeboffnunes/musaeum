
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


# Color pallete
# 0 - FFFFFF - Score 0
# 1 - DEE7DB - Score <20
# 2 - BCCFB8 - Score >20 <40
# 3 - 9BB894 - Score >40 <60
# 4 - 79A071 - Score >60 <80
# 5 - 58884D - Score >80


calendar_heatmap = dbc.Col([
    dbc.Row(
       [
            dbc.Col(html.P("1238", className = "heatmap-week-number")),
            dbc.Col(html.P("1239", className = "heatmap-week-number")),
            dbc.Col(html.P("1240", className = "heatmap-week-number")),
            dbc.Col(html.P("1241", className = "heatmap-week-number")),
            dbc.Col(html.P("1242", className = "heatmap-week-number")),
            dbc.Col(html.P("1243", className = "heatmap-week-number")),
            dbc.Col(html.P("1244", className = "heatmap-week-number")),
            dbc.Col(html.P("1245", className = "heatmap-week-number")),
            dbc.Col(html.P("1246", className = "heatmap-week-number")),
            dbc.Col(html.P("1247", className = "heatmap-week-number")),
            dbc.Col(html.P("1248", className = "heatmap-week-number")),
            dbc.Col(html.P("1247", className = "heatmap-week-number")),
            dbc.Col(html.P("1248", className = "heatmap-week-number")),
            dbc.Col(html.P("1249", className = "heatmap-week-number")),
            dbc.Col(html.P("1250", className = "heatmap-week-number")),
            dbc.Col(html.P("1251", className = "heatmap-week-number")),
            dbc.Col(html.P("1252", className = "heatmap-week-number")),
            dbc.Col(html.P("1253", className = "heatmap-week-number")),
        ], className = "heatmap-weeks"
    ),
    dbc.Row(
        [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-1", className = "heatmap-day"),
        ], className = "heatmap-sunday"
    ),
    dbc.Row(
        [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-monday"
    ),
    dbc.Row(
        [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-tuesday"
    ),
    dbc.Row(
        [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-wednesday"
    ),
    dbc.Row(
       [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-thursday"
    ),
    dbc.Row(
       [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-friday"
    ),
    dbc.Row(
       [
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
            dbc.Col(html.Br(), id = "heatmap-0", className = "heatmap-day"),
        ], className = "heatmap-saturday"
    ),
    #dbc.Tooltip(
    #        "Noun: rare, "
    #        "the action or habit of estimating something as worthless.",
    #        target="tooltip-target",
    #    ),
])