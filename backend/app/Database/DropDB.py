import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS = os.getenv('MYSQL_PASS')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_PORT = os.getenv('MYSQL_PORT')


if __name__ == "__main__":
    mydb = mysql.connector.connect(
    user=MYSQL_USER, password=MYSQL_PASS, port=MYSQL_PORT, host=MYSQL_HOST)
    d = mydb.cursor()
    d.execute(f"DROP DATABASE {MYSQL_DB}")
    d.close()
