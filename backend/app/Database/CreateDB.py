import mysql.connector
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from Models import Base
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
    d.execute(f"CREATE DATABASE {MYSQL_DB}")
    d.close()
    engine = create_engine( pool_size=5,max_overflow=10,pool_recycle=3600, url=f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}")
    Base.metadata.create_all(engine)
















    
    # mydb = mysql.connector.connect(
    #     user=MYSQL_USER, password=MYSQL_PASS, port=MYSQL_PORT, host=MYSQL_HOST, database=MYSQL_DB)
    # d = mydb.cursor()
#     d.execute("""
# CREATE TABLE student (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     title_name text(20) NOT NULL,
#     first_name text(100) NOT NULL,
#     last_name text(100) NOT NULL,
#     birthday text(200) NOT NULL,
#     ethnicity text(100) NOT NULL,
#     nationality text(100) NOT NULL,
#     religion text(100) NOT NULL,
#     tel text(10) NOT NULL,
#     gpa double NOT NULL,
#     gpax double NOT NULL,
#     term text(100) NOT NULL,
#     reason text(5000) NOT NULL,
#     id_std_copy text(255) NOT NULL,
#     id_card_copy text(255) NOT NULL,
#     house_copy text(255)NOT NULL,
#     gpa_gpax_copy text(255) NOT NULL,
#     photo_house text(255) NOT NULL,
#     photo_family text(255) NOT NULL,
#     photo_std text(255) NOT NULL
# );

# CREATE TABLE address_house (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     address text(500)NOT NULL,
#     subdistrict text(100)NOT NULL,
#     district text(100)NOT NULL,
#     province text(100)NOT NULL,
#     postal_code text(20)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE address_ez (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     address text(500)NOT NULL,
#     subdistrict text(100)NOT NULL,
#     district text(100)NOT NULL,
#     province text(100)NOT NULL,
#     postal_code text(20)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE address_part_time (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     address text(1000)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE father (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     first_name text(100)NOT NULL,
#     last_name text(100)NOT NULL,
#     age INT(2)NOT NULL,
#     life_status text(30)NOT NULL,
#     job text(255)NOT NULL,
#     position text(255)NOT NULL,
#     address_job text(1000)NOT NULL,
#     salary INT(7)NOT NULL,
#     tel text(10)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE mother (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     first_name text(100)NOT NULL,
#     last_name text(100)NOT NULL,
#     age INT(2)NOT NULL,
#     life_status text(30)NOT NULL,
#     job text(255)NOT NULL,
#     position text(255)NOT NULL,
#     address_job text(1000)NOT NULL,
#     salary INT(7)NOT NULL,
#     tel text(10)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE living_with (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     title text(20) NOT NULL,
#     first_name text(100) NOT NULL,
#     last_name text(100) NOT NULL,
#     relationship_living_with text(255)NOT NULL,
#     tel text(10) NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE support (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     title text(10) NOT NULL,
#     first_name text(100)NOT NULL,
#     last_name text(100)NOT NULL,
#     relevant text(255)NOT NULL,
#     job text(255)NOT NULL,
#     position text(255)NOT NULL,
#     address_job text(1000)NOT NULL,
#     salary INT(8)NOT NULL,
#     tel text(10)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE information_history (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     marital_status_of_parents text(255)NOT NULL,
#     scholar_history text(2000)NOT NULL,
#     sibling_study text(2000)NOT NULL,
#     sibling_job text(2000)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE part_time_job (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     address text(500)NOT NULL,
#     type text(255)NOT NULL,
#     how_long text(255)NOT NULL,
#     salary INT(6)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# CREATE TABLE payment_history (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     student_id INT NOT NULL,
#     std_pay_month INT(6)NOT NULL,
#     std_pay_year INT(7)NOT NULL,
#     FOREIGN KEY (student_id) REFERENCES Student(id)
# );
# """)
#     d.close()
