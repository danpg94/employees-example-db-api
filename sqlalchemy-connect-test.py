from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PSWD = getenv('MYSQL_PSWD')
MYSQL_IP = getenv('MYSQL_IP')
engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PSWD}@{MYSQL_IP}")

connection = engine.connect()
query = text("SELECT * FROM employees.employees LIMIT 10")
result = connection.execute(query)

for row in result:
    print(row)
