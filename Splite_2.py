import sqlite3
from OOP_1 import Employee
conn=sqlite3.connect('employee.db')
c=conn.cursor()

# c.execute("show databases")

###'''MULTIPLE

# c.execute("drop table employees")
# c.execute("drop table employees1")
c.execute("drop table employees3")
c.execute(""" CREATE TABLE employees3(first text,last text,pay integer)""")
c.execute("INSERT INTO employees3 VALUES('Ke','Bian',90000)")
c.execute("SELECT first, last from employees3 where pay >100")
#print(c.fetchall())



print(type(c))
#
emp1 = Employee("a","b",50000)
emp2 = Employee("w","c",80000)
emp3 = Employee("e","b",100)
print(emp_1.last)


def insert_emp(emp):
    with conn:
        c.execute('INSERT INTO employees3 VALUES(:first, :last, :pay)',{'first':emp.first,'last':emp.last,'pay':emp.pay})
#
#
def insert_emp(emp):
    with conn:
        c.execute('INSERT INTO employees3 VALUES(?,?,?)',(emp.first, emp.last,emp.pay))


def out_emp(lastname):
    c.execute('SELECT * from employees3 where last=:last', {'last':lastname} )
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute('UPDATE employees3 SET pay= :pay WHERE first=:first and last=:last', {'first': emp.first, 'last': emp.last,'pay': pay})
#
def update_pay(emp, pay):
    with conn:
         c.execute('UPDATE employees3 SET pay= ? WHERE first=? and last=?', (pay,  emp.first,  emp.last))


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees3 SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute('DELETE FROM employees3 WHERE first=:first AND last =:last', {'first': emp.first, 'last': emp.last})



insert_emp(emp1)
insert_emp(emp2)
insert_emp(emp3)
print(out_emp(lastname="b"))
update_pay(emp3,200)
print(out_emp(lastname="b"))
remove_emp(emp2)


c.execute("SELECT first, last,pay from employees3")
print(c.fetchall())

conn.commit()
#
conn.close()