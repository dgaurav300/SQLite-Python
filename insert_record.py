from connection import conn

#conn.execute("""insert into student (rollnumber,name,age) 
#             values (3,'Jack',22)""")
#or
conn.execute("""insert into student (rollnumber,name,age) 
           values (?,?,?)""",(5,"Rakesh",25))


conn.commit()
