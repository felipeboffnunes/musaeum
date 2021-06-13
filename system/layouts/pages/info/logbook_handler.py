from typing import List, Dict

import sqlite3
import datetime

import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


class LogBook_Handler():
    
    INITIAL_DATE: datetime.date = datetime.date(1997, 6, 4)
    START_AT: int = 8766

    SYSTEM: str = "system/data/sqlite/"
    LOCAL: str = "../../../data/sqlite/"

    PATH: str = SYSTEM


    TYPE: Dict[str, Dict] = {
        "LOG" : {"name": "small_log"},
        "NUT" : {
            "name":       "nutrition",
            "first_row":  ["Fish", "Meat", "Ham", "Tapioca", "Egg", "Power Ade", "Monster"],
            "second_row": ["Whey", "ZMA", "Multivitamin", "Omega 3", "Thermogenic"]
        },
        "EXE" : {
            "name": "exercises",
            "first_row": ["Bench Press", "Push-up", "Fly", "Overhead Press",
                        "Goblet Squat", "Back Squat",	"Alt. Reverse Lunge",
                        "Pull-up", "Chin-up", "Bent Row", "Alt. Row",
                        "Plank", "Alt. Plank", "Rower"],
            "second_row": ["Side Lateral Raise", "Close-Grip Push-up", "Unilateral Kickback",
                        "Alt. Leg Pelvic Tilt", "Isometric Squat", "Alt. Calf Raise",
                        "Reverse Fly", "Biceps Curl", "Alt. Biceps Curls",
                        "Jackknife", "Canoe Crunch", "Short Crunch"]
        }
    }
    
    IGNORE_COL: List[str] = ["index", "Day"]
    
    
    def consume_data(self, date_str:str) -> html.Div:
        
        day = self._date_str_to_day(date_str)
        date_ = self._date_str_to_date(date_str)
        
        exercise_data = self._health_day(day, "EXE")
        nutrition_data = self._health_day(day, "NUT")
        
        result: list = [html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Col(html.H1(day, id="day-old")),
                    dcc.DatePickerSingle(
                        date=date_,
                        id='day-picker'
                    )
                ], width = 2, id="header-days"),
                self._calendar(),
                ]),
            ], id="day-div"),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.H4("Activities"),
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                            html.Img(src="./assets/images/icons/dog-side.svg", className="activity-icon"),
                            ], width="auto"),
                            dbc.Col([
                                html.H3("Walked Marbas", className="activity-header"),
                                html.P("1Km - 15 min", className="activity-details")
                            ], width = 9)
                        ], className="activity-row")
                    ], id="activities-col"),
                    html.Hr(),
                    html.H4("Studies"),
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.Img(src="./assets/images/icons/book.svg", className="study-icon"),
                            ], width="auto"),
                            dbc.Col([
                                html.H3("Read 50 pages", className="study-header"),
                                html.P("2 hours", className="study-details")
                            ], width=9)
                        ], className="study-row")
                    ], id="studies-col")
                ], width = 4),
                dbc.Col([
                    dbc.Row([
                        html.Img(src="./assets/images/background/VitruvianMan_post.jpg", id="vitruvian")
                    ]),
                    dbc.Row([
                        html.Span("Iron rusts from disuse; water loses its purity from stagnation... even so does inaction sap the vigor of the mind.", id="vitruvian-quote")
                    ])
                ],id="vitruvian-col", width = 4),
                dbc.Col([
                    html.H4("Nutrition"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(html.H3("2300", id="nutrition=calories-n"), width=2),
                                dbc.Col(html.P("calories consumed", id="nutrition-calories-consumed")),
                            ]),
                            dbc.Row([
                                dbc.Col(dbc.Progress(value=74, id="nutrition-calories-progress"))
                            ]),
                            dbc.Row(
                                nutrition_data, id="nutrition-data"
                            )
                        ])
                    ]),
                    html.Hr(),
                    html.H4("Exercises"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(html.H3("2150", id="basal=calories-n"), width=2),
                                dbc.Col(html.P("calories burned", id="nutrition-calories-burned")),
                            ]),
                            dbc.Row([
                                dbc.Col(dbc.Progress(value=91, id="exercise-calories-progress"))
                            ]),
                            dbc.Row(
                                exercise_data, id="exercises-data"
                            )
                        ])
                    ])
                ], width=4)
            ], justify="between",)]
        
        return result  
        
    
    def _date_str_to_day(self,date_str: str) -> int:
        date_ = self._date_str_to_date(date_str)
        delta = date_ - self.INITIAL_DATE
        return delta.days
    
    def _date_str_to_date(self, date_str: str) -> datetime.date:
        date_ = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_

    def _health_day(self, day:int, type_:str) -> tuple: 
        
        conn = sqlite3.connect(f"{self.PATH}{self.TYPE[type_]['name']}.db")
        df = pd.read_sql_query(f"SELECT * from {self.TYPE[type_]['name']}", conn)
        
        day_df = df[df["Day"] == day]
        day_df = day_df.reset_index(drop=True)
        day_first_rows = []
        day_second_rows = []
        for idx, row in day_df.iteritems():
            if idx not in self.IGNORE_COL and row[0] != 0:
                row = dbc.Row(html.P(f"{idx}: {row[0]}"), id=f"{self.TYPE[type_]['name']}-row")
                if idx in self.TYPE[type_]["first_row"]:
                    day_first_rows.append(row)
                elif idx in self.TYPE[type_]["second_row"]:
                    day_second_rows.append(row)
        
        result = dbc.Col(day_first_rows, width= {"size": 5, "offset": 1}), dbc.Col(day_second_rows, width={"size": 5})
        return result
    
    def _calendar(self) -> dbc.Col:
        
        number_of_weeks = 16
        first_week = self.START_AT//7 
        week_offset = 3
        
        def _setup_calendar_data() -> list:
        
            conn = sqlite3.connect(f"{self.PATH}{self.TYPE['LOG']['name']}.db")
            df = pd.read_sql_query(f"SELECT * from {self.TYPE['LOG']['name']}", conn)
        
            rows = [__setup_number_row()]
            rows.extend(__setup_day_rows(df))
            rows.extend(__setup_tooltips(df))
        
            return rows  
        
        def __setup_tooltips(df: pd.DataFrame) -> list:
            
            tooltips = []
            for idx, row in df.iterrows():  
                tooltip = dbc.Tooltip(
                    row["Description"],
                    target=f"_{row['Day']}",
                )
                tooltips.append(tooltip)
                
            return tooltips
        
        def __setup_number_row() -> list:
            
            number_week_row = [dbc.Col(html.P(" ", className = "heatmap-week-number"))]
            for i in range(first_week, first_week+number_of_weeks):
                col = dbc.Col(html.P(i, className = "heatmap-week-number"))
                number_week_row.append(col)
                
            return dbc.Row(number_week_row)
        
        def __setup_day_rows(df: pd.DataFrame) -> list:
            week = "sunday monday tuesday wednesday thursday friday saturday".split()
            week_abv = "sun mon tur wed thu fri sat".split()  
            
            day_rows = []
            for i, (day, day_abv) in enumerate(zip(week, week_abv)):
                day_row = [dbc.Col(html.Span(day_abv, className = "heatmap-day-week"))]
                
                for y in range(first_week, first_week+number_of_weeks):
                    
                    day_number = y*7 + i - week_offset
                    
                    rate_aux = df[df["Day"] == day_number]["Rate"]
                    rate = rate_aux.values[0] if len(rate_aux) > 0 else 0
                    
                    day_col = dbc.Col(html.Br(), id = f"_{day_number}", className = f"heatmap-day heatmap-{rate}")
                    day_row.append(day_col)
                    
                day_rows.append(dbc.Row(day_row, id=f"heatmap-day-row heatmap-{day}"))
                
            return day_rows

        calendar_heatmap = dbc.Col(_setup_calendar_data(), className = "heatmap-weeks")
        
        return calendar_heatmap
    