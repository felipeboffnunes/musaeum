# Python Standard Library
import sqlite3
# Third party imports
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
#

conn = sqlite3.connect("system/data/sqlite/library.db")
library_df = pd.read_sql_query("SELECT * from library", conn)

library_page = html.Div([
    dash_table.DataTable(
        id='library-datatable',
        fixed_rows={'headers': True},
        style_table={
        'height': 'auto',
        'overflowY': 'auto',
        'overflowX': 'hidden'
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
        tooltip_data=[
        {
            'Author': {
                'value': """
                \n![Aldous Leonard Huxley](./assets/images/authors/aldous_leonard_huxley_.jpg)
                \nAldous Leonard Huxley
                \n26 July 1894 - 22 November 1963
                \nAldous Leonard Huxley was an English writer and philosopher.
                \nHe wrote nearly 50 books—both novels and non-fiction works—as well as wide-ranging essays, narratives, and poems.
                \nBy the end of his life, Huxley was widely acknowledged as one of the foremost intellectuals of his time.
                \nHe was nominated for the Nobel Prize in Literature nine times and was elected Companion of Literature by the Royal Society of Literature in 1962.
                \nHuxley was a pacifist.  
                \nIn his most famous novel Brave New World (1932) and his final novel Island (1962), he presented his vision of dystopia and utopia, respectively.
                \n""",
                'type': 'markdown',
            }
        }
        ],
        tooltip_duration = None,
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
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    ),
], style={"height": "100vh",
          "overflow": "hidden",
          "display": "flex",
          "flex-flow": "column"}, id="library-div")