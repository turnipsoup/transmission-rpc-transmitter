import sqlite3, logging, os


class DAO():
    def __init__(self, SQL_DB):
        self.sql_db = SQL_DB
        self.connectdb()

    def connectdb(self):
        logging.info(f"Conncting to DB {self.sql_db}")

        if not os.path.isfile(self.sql_db):
            logging.info(f"{self.sql_db} does not exist, creating!")
        self.conn = sqlite3.connect(self.sql_db)
        logging.info(f"Connected to DB {self.sql_db}")