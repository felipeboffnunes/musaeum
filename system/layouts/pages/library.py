import sqlite3

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

from system.layouts.pages.info.library_info import authors

conn = sqlite3.connect("system/data/sqlite/library.db")
library_df = pd.read_sql_query("SELECT * from library", conn)

library_page = html.Div([
    dash_table.DataTable(
        id='library-datatable',
        fixed_rows={'headers': True},
        style_table={
        'overflowY': 'auto',
        'overflowX': 'hidden',
        "width": "100vw",
        "minWidth": "100vw",
        "height": "90vh", 
        "maxHeight": "90vh"
        },
        style_cell={
        'whiteSpace': 'normal',
        'border': '1px solid grey' 
        },
        style_cell_conditional=[
        {'if': {'column_id': 'index'},
         'width': '6%',
         'textAlign': 'center'},
        {'if': {'column_id': 'Author'},
         'textAlign': 'left'},
        {'if': {'column_id': 'Title'},
         'textAlign': 'left'},
        {'if': {'column_id': 'Pages'},
         'width': '6%',
         'textAlign': 'center'},
        {'if': {'column_id': 'Publisher'},
         'width': '10%',
         'textAlign': 'center'},
        {'if': {'column_id': 'Language'},
         'width': '8%',
         'textAlign': 'center'},
        {'if': {'column_id': 'ISBN-13'},
         'textAlign': 'center'},
        {'if': {'column_id': 'Genre 1'},
         'width': '10%',
         'textAlign': 'center'},
        {'if': {'column_id': 'Genre 2'},
         'textAlign': 'center'},
        {'if': {'column_id': 'Genre 3'},
         'textAlign': 'center'},
        {'if': {'column_id': 'Review'},
         'width': '6%',
         'textAlign': 'center'},
        ],
        style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
        ],
        style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
        },
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
        page_size=25,
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
    dbc.Modal(
        [
            dbc.ModalHeader("Author", id="library-modal-header"),
            dbc.ModalBody(
                "Author Description", id="library-modal-body"
            )
        ],
        id="library-modal",
        is_open=False,
        backdrop=True,
        size="lg",
        scrollable=False
    ),
], id="library-page")