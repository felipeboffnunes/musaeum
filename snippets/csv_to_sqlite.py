# Python Standard Library
import sqlite3
# Third party imports
import pandas

TARGET = "LIB"

CSV_NAME = {
    "LIB" : "library.csv",      
}

DB_NAME = {
    "LIB" : "library",
}

LAYOUT = {
    "LIB" : "(author, title, pages, publisher, language, isbn-13, genre-1, genre-2, genre-3, rating)",
}

CSV_PATH = f"../data/csv/{CSV_NAME[TARGET]}"
SQ_PATH = f"../data/sqlite/{DB_NAME[TARGET]}.db"

cnx = sqlite3.connect(SQ_PATH)
df = pandas.read_csv(CSV_PATH)
df.to_sql(DB_NAME[TARGET], cnx)