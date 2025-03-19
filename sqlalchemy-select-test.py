import enum
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, INT, VARCHAR, CHAR, DATE, Enum
from sqlalchemy import PrimaryKeyConstraint, ForeignKey
from sqlalchemy import create_engine, text
from sqlalchemy import select
from dotenv import load_dotenv
from os import getenv

load_dotenv()
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PSWD = getenv('MYSQL_PSWD')
MYSQL_IP = getenv('MYSQL_IP')
DB_NAME= getenv('DB_NAME')

engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PSWD}@{MYSQL_IP}/{DB_NAME}")

class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'

metadata_obj = MetaData()

employee_table = Table(
    "employees",
    metadata_obj,
    Column("emp_no", INT, primary_key=True, nullable=False),
    Column("birth_date", DATE, nullable=False),
    Column("first_name", VARCHAR(14), nullable=False),
    Column("last_name", VARCHAR(16), nullable=False),
    Column("gender", Enum(GenderEnum), nullable=False),
    Column("hire_date", DATE, nullable=False)
)

departments_table = Table(
    "departments",
    metadata_obj,
    Column("dept_no", CHAR(4), primary_key=True, nullable=False),
    Column("dept_name", VARCHAR(40), unique=True, nullable=False) 
)

department_employees_table = Table(
    "dept_emp",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("dept_no", CHAR(4), ForeignKey("departments.dept_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE, nullable=False),
    PrimaryKeyConstraint("emp_no", "dept_no")
)

department_manager_table = Table(
    "dept_manager",
    metadata_obj,
    Column("dept_no", CHAR(4), ForeignKey("departments.dept_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "dept_no")
)

titles_table = Table (
    "titles",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("title", VARCHAR(50), nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "title", "from_date")
)

salaries_table = Table(
    "salaries",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("salary", INT, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "from_date")
)

with engine.connect() as conn:
    
    stmt = select(employee_table).where(employee_table.c.emp_no == 10001)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)

    stmt = select(departments_table)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)

    stmt = select(department_employees_table).where(department_employees_table.c.emp_no == 10001)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)

    stmt = select(department_manager_table).limit(5)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)

    stmt = select(titles_table).where(titles_table.c.emp_no == 10004)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row)
    
    stmt = select(salaries_table).where(salaries_table.c.emp_no == 10004)
    print("\nSQL: ", stmt, "\nOutput: \n")
    for row in conn.execute(stmt):
        print(row) 