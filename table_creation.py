from connection import conn


conn.execute("""CREATE TABLE STUDENT(
             ROLLNUMBER INT NOT NULL,
             NAME VARCHAR(255) NOT NULL,
             AGE INT NOT NULL               
             )""")



