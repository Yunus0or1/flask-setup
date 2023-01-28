from dotenv import load_dotenv, find_dotenv
import sqlite3
import os
load_dotenv(find_dotenv())

DB_NAME = os.environ.get("DB_NAME")
DB_TYPE = os.environ.get("DB_TYPE")


def connectToDB():
    try:
        if DB_TYPE == 'sqlite3':
            dbcon = sqlite3.connect(DB_NAME)
            return dbcon
        else:
            raise SystemExit("=> Could not connect to DB, check DB type and name.")
    except Exception as error:
        raise SystemExit("=> Could not connect to DB, check DB type and name.")

