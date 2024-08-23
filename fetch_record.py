from connection import conn

students=conn.execute("select rollnumber,name,age from student;")

for s in students:
    print("Roll Number:",s[0])
    print("Name:",s[1])
    print("Age:",s[2])
    



