from flask import Flask
import sqlite3
from orders import orders_pages
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_NAME = os.environ.get("DB_NAME")
PORT = os.environ.get("FLASK_RUN_PORT")
DEBUG_MODE = os.environ.get("DEBUG_MODE")

# Checking all the ENV variables exist or not
if DB_NAME == None or PORT == None or DEBUG_MODE == None :
    raise SystemExit("ERROR IN Loading Environment File in main.py. Please check if .env file exists with these keys : DB_NAME, PORT. Also check if the database is running. Please fix the .env file and start the server again")
else:
    print('Loaded ENV Variables')

try:
    dbcon = sqlite3.connect(DB_NAME)
except Exception as error:
    raise SystemExit("Could not connect to DB")


app = Flask(__name__)
app.register_blueprint(orders_pages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG_MODE)
