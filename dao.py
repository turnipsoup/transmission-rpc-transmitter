import sqlite3, logging, os


class DAO():
    def __init__(self, SQL_DB):
        self.sql_db = SQL_DB
        self.make_all_tables = False
        self.connectdb()
        

    def connectdb(self):
        logging.info(f"Conncting to DB {self.sql_db}")

        if not os.path.isfile(self.sql_db):
            logging.info(f"{self.sql_db} does not exist, creating!")
            self.make_all_tables = True

        self.conn = sqlite3.connect(self.sql_db)
        logging.info(f"Connected to DB {self.sql_db}")

        if self.make_all_tables:
            self.create_start_tables()
        


    def insert(self, table, csv):
        """
        Given the table name and a csv of the values, inserts them.
        Programmer must be aware of schema.
        """

        cur = self.conn.cursor()
        string_csv = ",".join([f"'{str(x)}'" for x in csv.split(",")])

        logging.debug(f"Insert into table {table} values {string_csv}")
        cur.execute(f"INSERT INTO {table} VALUES ({string_csv})")
        self.conn.commit()


    def create_table(self, table_name, table_columns):
        """
        Creates a table in the SQLite db.
        table_name: string
        table_values: comma-sep string
        """

        cur = self.conn.cursor()

        logging.info(f"Creating table {table_name} with values {table_columns}")
        cur.execute(f'''CREATE TABLE {table_name} ({table_columns})''')

    def create_start_tables(self):
        start_tables = {
            "peers": "address,clientIsChoked,\
                    clientIsInterested,clientName,\
                    flagStr,isDownloadingFrom,\
                    isEncrypted,isIncoming,\
                    isUTP,isUploadingTo,\
                    peerIsChoked,peerIsInterested,\
                    port,progress,rateToClient,\
                    rateToPeer,tag,date,torrent_name",
            
            "stats": "name,rateDownload,rateUpload,status,totalSize,uploadRatio,tag,date"
        }

        logging.info(f"Creating all ({len(start_tables)}) starting tables")
        for table in start_tables:
            self.create_table(table, start_tables[table].replace(" ", ""))
