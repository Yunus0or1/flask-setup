import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

current_folder = os.path.dirname(os.path.realpath(__file__))
base_path = os.path.dirname(current_folder)


class Config:
    BASE_DIR = base_path
    DB_URI_TYPE = os.environ.get("DB_URI_TYPE")
    PORT = os.environ.get("FLASK_RUN_PORT")
    DEBUG_MODE = os.environ.get("DEBUG_MODE")
    DB_NAME = os.environ.get("DB_NAME")
    DB_TYPE = os.environ.get("DB_TYPE")
    DB_URL = 'sqlite:///' + os.path.join(BASE_DIR,  DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def verify(self):
        # Checking all the ENV variables exist or not
        if self.DB_NAME == None or self.PORT == None or self.DEBUG_MODE == None or self.DB_URI_TYPE is None:
            raise SystemExit("=> ERROR IN Loading Environment File in main.py. Please check if .env file exists with these keys : DB_NAME, PORT. Also check if the database is running. Please fix the .env file and start the server again")
        else:
            print('=> Loaded ENV Variables')
