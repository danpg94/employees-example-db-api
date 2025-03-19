from sqlalchemy import create_engine
from sqlalchemy import select
from dotenv import load_dotenv
from os import getenv
from employees_db_table_definitions import employee_tbl, departments_tbl, dept_emp_tbl, dept_manager_tbl, titles_tbl, salaries_tbl

load_dotenv()
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PSWD = getenv('MYSQL_PSWD')
MYSQL_IP = getenv('MYSQL_IP')
DB_NAME= getenv('DB_NAME')

engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PSWD}@{MYSQL_IP}/{DB_NAME}")

def print_select_statement(stmt):
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)

with engine.connect() as conn:
    
    stmt = select(employee_tbl).where(employee_tbl.c.emp_no == 10001)
    print_select_statement(stmt)

    stmt = select(departments_tbl)
    print_select_statement(stmt)

    stmt = select(dept_emp_tbl).where(dept_emp_tbl.c.emp_no == 10001)
    print_select_statement(stmt)

    stmt = select(dept_manager_tbl).limit(5)
    print_select_statement(stmt)

    stmt = select(titles_tbl).where(titles_tbl.c.emp_no == 10004)
    print_select_statement(stmt)
    
    stmt = select(salaries_tbl).where(salaries_tbl.c.emp_no == 10004)
    print_select_statement(stmt)