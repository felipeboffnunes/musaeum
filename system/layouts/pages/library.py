# Python Standard Library
import sqlite3
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

conn = sqlite3.connect("system/data/sqlite/library.db")
library_df = pd.read_sql_query("SELECT * from library", conn)

library_page = html.Div([
    dash_table.DataTable(
        id='library-datatable',
        style_cell={
        'whiteSpace': 'normal',
        },
        style_cell_conditional=[
        {'if': {'column_id': 'index'},
         'width': '6%'},
        {'if': {'column_id': 'Pages'},
         'width': '6%'},
        {'if': {'column_id': 'Review'},
         'width': '7%'},
        {'if': {'column_id': 'Language'},
         'width': '8%'},
        {'if': {'column_id': 'Publisher'},
         'width': '10%'},
        {'if': {'column_id': 'Genre 1'},
         'width': '10%'},
        
        ],
        columns=[
            {"name": i, "id": i} for i in library_df.columns
        ],
        data=library_df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
], id="library-div")