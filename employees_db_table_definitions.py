import enum
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, INT, VARCHAR, CHAR, DATE, Enum
from sqlalchemy import PrimaryKeyConstraint, ForeignKey

metadata_obj = MetaData()


""" CREATE TABLE employees (
    emp_no      INT             NOT NULL,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,    
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
); """
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'

employee_tbl = Table(
    "employees",
    metadata_obj,
    Column("emp_no", INT, primary_key=True, nullable=False),
    Column("birth_date", DATE, nullable=False),
    Column("first_name", VARCHAR(14), nullable=False),
    Column("last_name", VARCHAR(16), nullable=False),
    Column("gender", Enum(GenderEnum), nullable=False),
    Column("hire_date", DATE, nullable=False)
)

""" CREATE TABLE departments (
    dept_no     CHAR(4)         NOT NULL,
    dept_name   VARCHAR(40)     NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE  KEY (dept_name)
); """
departments_tbl = Table(
    "departments",
    metadata_obj,
    Column("dept_no", CHAR(4), primary_key=True, nullable=False),
    Column("dept_name", VARCHAR(40), unique=True, nullable=False) 
)

""" CREATE TABLE dept_emp (
    emp_no      INT             NOT NULL,
    dept_no     CHAR(4)         NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no)  REFERENCES employees   (emp_no)  ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,dept_no)
); """
dept_emp_tbl = Table(
    "dept_emp",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("dept_no", CHAR(4), ForeignKey("departments.dept_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE, nullable=False),
    PrimaryKeyConstraint("emp_no", "dept_no")
)

""" CREATE TABLE dept_manager (
   emp_no       INT             NOT NULL,
   dept_no      CHAR(4)         NOT NULL,
   from_date    DATE            NOT NULL,
   to_date      DATE            NOT NULL,
   FOREIGN KEY (emp_no)  REFERENCES employees (emp_no)    ON DELETE CASCADE,
   FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
   PRIMARY KEY (emp_no,dept_no)
); """
dept_manager_tbl = Table(
    "dept_manager",
    metadata_obj,
    Column("dept_no", CHAR(4), ForeignKey("departments.dept_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "dept_no")
)

""" CREATE TABLE titles (
    emp_no      INT             NOT NULL,
    title       VARCHAR(50)     NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,title, from_date)
); """
titles_tbl = Table (
    "titles",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("title", VARCHAR(50), nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "title", "from_date")
)

""" CREATE TABLE salaries (
    emp_no      INT             NOT NULL,
    salary      INT             NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, from_date)
); """
salaries_tbl = Table(
    "salaries",
    metadata_obj,
    Column("emp_no", INT, ForeignKey("employees.emp_no", ondelete="CASCADE"), index=True, nullable=False),
    Column("salary", INT, nullable=False),
    Column("from_date", DATE, nullable=False),
    Column("to_date", DATE),
    PrimaryKeyConstraint("emp_no", "from_date")
)