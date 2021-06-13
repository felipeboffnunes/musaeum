# Python Standard Library
import sqlite3
# Third party imports
import pandas

TARGET = "ACT"

NAME = {
    "LIB" : "library",
    "NUT" : "nutrition",
    "EXE" : "exercises",
    "LOG" : "small_log",
    "ACT" : "activities" 
}

CSV_PATH = f"../system/data/csv/{NAME[TARGET]}.csv"
SQ_PATH = f"../system/data/sqlite/{NAME[TARGET]}.db"

cnx = sqlite3.connect(SQ_PATH)
df = pandas.read_csv(CSV_PATH)
df.to_sql(NAME[TARGET], cnx)