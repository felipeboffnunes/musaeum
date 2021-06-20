from typing import List, Dict, Union
import sqlite3
import datetime

import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px


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
        },
        "ACT" : {
            "name": "activities",
            "individual": "activity"
        },
        "STU": {
            "name": "studies",
            "individual": "study"
        }
    }
    
    ICONS: Dict[str, str] = {
        "Walked Marbas" : "./assets/images/icons/dog-side.svg",
        "Water Plants"  : "./assets/images/icons/watering-can.svg",
        "Meditate"      : "./assets/images/icons/meditation.svg",
        "Clean Dishes"  : "./assets/images/icons/silverware-clean.svg",
        "Wash Clothes"  : "./assets/images/icons/washing-machine.svg",
        "Clean House"   : "./assets/images/icons/spray-bottle.svg",
        "Buy Food"      : "./assets/images/icons/cart.svg"
    }
    
    IGNORE_COL: List[str] = ["index", "Day"]
    
    
    def consume_data(self, date_str:str) -> html.Div:
        
        day = self._date_str_to_day(date_str)
        
        result: list = [html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Col(html.H1(day, id="day-old")),
                    dcc.DatePickerSingle(
                        date=self._date_str_to_date(date_str),
                        min_date_allowed=datetime.date(2021, 6, 4),
                        max_date_allowed=datetime.date(2021, 6, 19),
                        id='day-picker'
                    )
                ], width = 2, id="header-days"),
                self._calendar(),
                ]),
            ], id="day-div"),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.H4(["Activities", html.Img(src="./assets/images/icons/information-outline.svg", id="ACTINFO", className="info-icon")]),
                    self._data(day, "ACT"),
                    html.Hr(),
                    html.H4(["Studies", html.Img(src="./assets/images/icons/information-outline.svg", id="STUINFO", className="info-icon")]),
                    self._data(day, "STU")
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
                    html.H4(["Nutrition", html.Img(src="./assets/images/icons/information-outline.svg", id="NUTINFO", className="info-icon")]),
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([
                                dbc.Col(html.H3("2300", id="nutrition=calories-n"), width=2),
                                dbc.Col(html.P("calories consumed", id="nutrition-calories-consumed")),
                            ]),
                            dbc.Row([
                                dbc.Col(dbc.Progress(value=74, id="nutrition-calories-progress"))
                            ]),
                            self._data(day, "NUT")
                        ])
                    ]),
                    html.Hr(),
                    html.H4(["Exercises", html.Img(src="./assets/images/icons/information-outline.svg", id="EXEINFO", className="info-icon")]),
                    dbc.Row([
                        dbc.Col([
                            self._data(day, "EXE")
                        ])
                    ])
                ], width=4)
            ], justify="between")]
        
        return result  
        
    
    def _date_str_to_day(self,date_str: str) -> int:
        date_ = self._date_str_to_date(date_str)
        delta = date_ - self.INITIAL_DATE
        return delta.days
    
    def _date_str_to_date(self, date_str: str) -> datetime.date:
        date_ = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_

    def _get_df(self, type_:str, day:int, rangex: bool = False, range_n:int = 0) -> pd.DataFrame:
        conn = sqlite3.connect(f"{self.PATH}{self.TYPE[type_]['name']}.db")
        df = pd.read_sql_query(f"SELECT * from {self.TYPE[type_]['name']}", conn)
        
        conn.close()
        if rangex:
            df = df[df["Day"] <= day+range_n].reset_index(drop=True)
            df = df[df["Day"] >= day-range_n].reset_index(drop=True)
        else: 
            df = df[df["Day"] == day].reset_index(drop=True)
        
        return df

    def _data(self, day:int, type_:str) -> Union[dbc.Row, html.Div]: 
        
        def __health() -> list:
            day_first_rows = []
            day_second_rows = []
            for idx, row in df.iteritems():
                if idx not in self.IGNORE_COL and row[0] != 0:
                    row = dbc.Row(html.P(f"{idx}: {row[0]}"), id=f"{self.TYPE[type_]['name']}-row")
                    if idx in self.TYPE[type_]["first_row"]:
                        day_first_rows.append(row)
                    elif idx in self.TYPE[type_]["second_row"]:
                        day_second_rows.append(row)
        
            if day_first_rows or day_second_rows:
                col = [dbc.Col(day_first_rows, width= {"size": 5, "offset": 1}), dbc.Col(day_second_rows, width={"size": 5})]
            else:
                col = [dbc.Col("No info.")]
            return col
            
        def __tasks() -> list:
            rows = []
            for idx, row in df.iteritems():
                if idx not in self.IGNORE_COL and row[0] != 0 and row[0] != "0":
                    row = dbc.Row([
                        dbc.Col(
                            html.Img(src=self.ICONS[idx], 
                                     className=f"{self.TYPE[type_]['individual']}-icon" 
                                     if idx in ["Walked Marbas", "Meditate"] 
                                     else f"{self.TYPE[type_]['individual']}-icon-small"),
                            width="auto"),
                        dbc.Col(
                            [
                            html.H3(idx, className=f"{self.TYPE[type_]['individual']}-header"),
                            html.P(row[0], className=f"{self.TYPE[type_]['individual']}-details")
                            if row[0] != "1" and row[0] != 1 else None
                            ] if idx in ["Walked Marbas", "Meditate"] else 
                            html.H4(idx, className=f"{self.TYPE[type_]['individual']}-header")
                            , width=9)
                    ], className=f"{self.TYPE[type_]['individual']}-row")
                    rows.append(row)
            if rows:        
                return rows
            else:
                return ["No info."]
        
        df = self._get_df(type_, day)

        health = ["NUT", "EXE"]
        tasks = ["ACT", "STU"]
        
        if type_ in health:
            result = dbc.Row(__health(), id=f"{self.TYPE[type_]['name']}-data")
        elif type_ in tasks:
            result = html.Div(__tasks(), id=f"{self.TYPE[type_]['name']}-data")
        
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
    
    def graphs(self, date_str:str, category:str):
        
        
        def graphs_exercise():
            day = self._date_str_to_day(date_str)

            df = self._get_df(category, day, True, 4)
            
            training_1 = pd.concat([df.iloc[:, 1],df.iloc[:, 2:9]], axis=1)
            training_1["Train"]=1
            
            training_2 = pd.concat([df.iloc[:, 1],df.iloc[:, 9:15]], axis=1)
            training_2["Train"]=2
            
            training_3 = pd.concat([df.iloc[:, 1],df.iloc[:, 15:22]], axis=1)
            training_3["Train"]=3
            
            training_4 = pd.concat([df.iloc[:, 1],df.iloc[:, 22:]], axis=1)
            training_4["Train"]=4
            
            training = pd.concat([training_1,training_2,training_3,training_4])
            training = training.melt(id_vars=["Train", "Day"])
            
            fig = px.line(training, x="Day", y="value", color="variable", facet_row="Train", labels=dict(value=""))

            legend_layout = dict(
                orientation="h",
                title="",
                font=dict(
                    size=10,
                    color="black"
                ),
                yanchor="bottom",
                y=-0.5,
                xanchor="right",
                x=1
            )
            
            fig.update_layout(legend=legend_layout)
            
            fig.update_xaxes(dtick=1)
            fig.update_yaxes(rangemode="tozero")
            
            for anno in fig['layout']['annotations']:
                anno['text']=''
                
            return dcc.Graph(figure=fig, config={'displayModeBar': False})
        
        def graphs_nutrition():
            day = self._date_str_to_day(date_str)

            df = self._get_df(category, day, True, 4)
            
            gram_nutrition = pd.concat([df.iloc[:, 1],df.iloc[:, 2:5], df.iloc[:, 9]], axis=1)
            gram_nutrition["Type"]="gram"
            
            unitary_nutrition = pd.concat([df.iloc[:, 1],df.iloc[:, 5:9], df.iloc[:, 10:]], axis=1)
            unitary_nutrition["Type"]="unit"
            
            nutrition = pd.concat([gram_nutrition,unitary_nutrition])
            nutrition = nutrition.melt(id_vars=["Type", "Day"])
        
            fig = px.line(nutrition, x="Day", y="value", color="variable", facet_row="Type", labels=dict(value=""))
        
            legend_layout = dict(
                orientation="h",
                title="",
                font=dict(
                    size=10,
                    color="black"
                ),
                yanchor="bottom",
                y=-0.5,
                xanchor="right",
                x=1
            )
            
            fig.update_layout(legend=legend_layout)
            
            fig.update_xaxes(dtick=1)
            fig.update_yaxes(rangemode="tozero")
            
            for anno in fig['layout']['annotations']:
                anno['text']=''
                
            return dcc.Graph(figure=fig, config={'displayModeBar': False})
        
        def graphs_activities():
            day = self._date_str_to_day(date_str)

            df = self._get_df(category, day, True, 4)
            
            df = df.iloc[:,1:]
            
            
            calendar_col_icons = [dbc.Col(className = "heatmap-act-icon")]
            for col in df.columns:
                if col in self.ICONS:
                    icon_col = dbc.Col(html.Img(src=self.ICONS[col], className = "heatmap-act-icon"))
                    calendar_col_icons.append(icon_col)
                    
            calendar_header = [dbc.Row(calendar_col_icons)]
            
            calendar_data = []
            for i, row in df.iterrows():
                
                calendar_row_data = []
                for col in row:

                    if col < 1:
                        col_data = dbc.Col(html.Br(), className = f"heatmap-day heatmap-{0}")
                    elif col < 10:
                        col_data = dbc.Col(html.Br(), className = f"heatmap-day heatmap-{2}")
                    else:
                        col_data = dbc.Col(html.P(col), className = "heatmap-day-act")
                        
                    calendar_row_data.append(col_data)
                    
                calendar_row = dbc.Row(calendar_row_data)
                calendar_data.append(calendar_row)
            
            calendar_header.extend(calendar_data)
            
            calendar_heatmap = dbc.Col(calendar_header, className = "heatmap-weeks")
            return calendar_heatmap
            
        
        if category == "EXE":
            return graphs_exercise()
        elif category == "NUT":
            return graphs_nutrition()
        elif category == "ACT":
            return graphs_activities()
        elif category == "STU":
            return "HELLOSTU"
