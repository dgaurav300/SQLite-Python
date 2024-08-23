from connection import conn

conn.execute("delete from student where rollnumber=1;")

conn.commit()