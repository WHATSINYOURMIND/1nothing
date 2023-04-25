import MySQLdb
c=MySQLdb.connect('localhost','root','root','pythonfriday')
s=c.cursor()
s1="create table employee(eno int,ename varchar(20),address varchar(30))"
s.execute(s1)
print("Table Created...")
s2="insert into employee values(1,'SSS','Dadar')"
s3="insert into employee values(2,'ABC','Thane')"
s4="insert into employee values(3,'XYZ','Vashi')"
s.execute(s2)
s.execute(s3)
s.execute(s4)
print("Records Inserted...")
s5="delete from employee where eno=2"
s.execute(s5)
print("Record Deleted...")
s6="update employee set ename='Vidyalankar' where eno=3"
s.execute(s6)
print("Record Updated...")
s.execute('select * from employee')
rows=s.fetchall()    #s.fetchone()
print("Total number of rows=",s.rowcount)
for a in rows:
    print(a)
print("Records Displayed...")
c.commit()
s.close()
c.close()
    

