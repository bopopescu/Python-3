
class Employee:

    raise_amount=1.04
    num_of_emps=0

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+"@company.com"
        self.newpay=self.pay
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return '{}.{}'.format(self.first,self.last)

    @classmethod
    def set_raise_amt(ls, amount):
        ls.raise_amount=amount

    # #@property
    def apply_raise(self):
        self.pay = int(self.raise_amount*self.pay)

    def __add__(self, other):
        if isinstance(other,Employee):
            return self.pay+other.pay
        else:
            return "Not Employee"

    def __len__(self):
        return len(self.fullname)
            #len(self.first)+len(self.last)

    #__str__ = fullname

    def __str__(self):
         return "str_{}".format(self.fullname)

    ##def __repr__(self):
        ##return "repr_{}".format(self.fullname)


emp_1 = Employee("a","b",500)
emp_2 = Employee("w","c",800)


# f=[1,2]
# print(f.__class__)
emp_2.raise_amount= 4

emp_1.email="867@ww.com"
print(emp_1.pay)
print(emp_1.email)
emp_1.apply_raise()
print(emp_1.pay)
print(type(emp_1))
emp_1.set_raise_amt(7)
print(Employee.raise_amount)
Employee.set_raise_amt(3)
print(emp_1.raise_amount)

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang=None):
        super().__init__(first,last, pay)
        self.prog_lang = prog_lang
#
# d= Developer("a","b",300,"JAVA")
# d.apply_raise()
# print(d.pay)

class Manager(Employee):

     def __init__(self, first, last, pay, managee=None):
         super().__init__(first, last, pay)
         if managee is None:
             self.managee = []
         else:
             self.managee = managee

     def add_managee(self,managee_add):
         if managee_add not in self.managee:
             self.managee.append(managee_add)

     def remove_managee(self, managee_remove):
          if managee_remove in self.managee:
              self.managee.remove(managee_remove)

     def print_managee(self):
         for managee_test in self.managee:
             print("-->",managee_test.fullname())


f=Manager("j","d",200,[emp_1])
f.add_managee(emp_2)
#print(f.print_managee())


f.remove_managee(emp_1)
#print(f.print_managee())
# print(emp_2.pay)
# print(emp_2.email)
# emp_2.apply_raise()
# print(emp_2.pay())

# print(help(emp_1))

print(isinstance(d,Employee))

print(emp_1.pay, emp_2.pay,emp_1+"as")
print(len(emp_1))
print(emp_1)