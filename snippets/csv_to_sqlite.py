# Python Standard Library
import sqlite3
# Third party imports
import pandas

TARGET = "LOG"

CSV_NAME = {
    "LIB" : "library.csv",  
    "NUT" : "nutrition.csv",
    "EXE" : "exercises.csv",
    "LOG" : "small_log.csv"
}

DB_NAME = {
    "LIB" : "library",
    "NUT" : "nutrition",
    "EXE" : "exercises",
    "LOG" : "small_log"   
}

CSV_PATH = f"../system/data/csv/{CSV_NAME[TARGET]}"
SQ_PATH = f"../system/data/sqlite/{DB_NAME[TARGET]}.db"

cnx = sqlite3.connect(SQ_PATH)
df = pandas.read_csv(CSV_PATH)
df.to_sql(DB_NAME[TARGET], cnx)