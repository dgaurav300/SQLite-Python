from connection import conn

conn.execute("update student set age=30 where rollnumber=2;")

conn.commit()