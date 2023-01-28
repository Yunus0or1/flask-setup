import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

current_folder = os.path.dirname(os.path.realpath(__file__))
base_path = os.path.dirname(current_folder)

ERROR_MESSAGE = "=> ERROR IN Loading Environment File in main.py. Please check if .env file exists with these keys : DB_NAME, PORT. Also check if the database is running. Please fix the .env file and start the server again"


class Config:
    def __init__(self):
        try:
            self.BASE_DIR = base_path
            self.DB_URI_TYPE = os.environ.get("DB_URI_TYPE")
            self.PORT = os.environ.get("FLASK_RUN_PORT")
            self.DEBUG_MODE = os.environ.get("DEBUG_MODE")
            self.DB_NAME = os.environ.get("DB_NAME")
            self.DB_TYPE = os.environ.get("DB_TYPE")
            self.DB_URL = 'sqlite:///' + \
                os.path.join(self.BASE_DIR,  self.DB_NAME)
            self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        except Exception as e:
            print(e)
            raise SystemExit(ERROR_MESSAGE)

    def verify(self):
        # Checking all the ENV variables exist or not
        if self.DB_NAME == None or self.PORT == None or self.DEBUG_MODE == None or self.DB_URI_TYPE is None:
            raise SystemExit(ERROR_MESSAGE)
        else:
            print('=> Loaded ENV Variables')
