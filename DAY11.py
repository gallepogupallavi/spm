'''
usage/importance of underscores in python
--> single underscore-->'_'
-->single traling underscore->'var_'
--> double leading underscore-->'__var'
-->double leading and double trailing underscores
(python special methods-->__var__)
'''
#single underscore:it isgenarally used for
#temparary purposes/to join multiple words
#snake case eonvention

'''for _ in range(1,11):
    print(_,end='')
email_id="u220369@gmail.com"
print(email_id)
mobile_no=9110721011
print(mobile_no)
for _ in range(1,22):
    print(_,end='')
email_id="indrasushma77@gmail.com"
print(email_id)
mbile_no=6303172783
print(mobile_no)
'''
'''#single trailing underscore-->var_
#it is generally used in order to avoid name
#coflicts with python key words
def students(name,age,class_):
    print(f'{name} is of{age} years old in {class_}\class')
students("indra",19,15)'''

'''#double leading underscores--> _var
class details:
    """usage of doubl leading under"""
    def __init__(self):
        self.name="uma"
        self.place="kowkuntla"
        self.__age=20
a=details()
print(dir(a))
print(f'{a.name} is in {a.place} of {a._details__age} years old')
'''
'''#DOUBLE LEADING AND DOUBLE TRAILING UNDERSCORES
#these are reprasent which python follows or
#special methods

class students:
    """student class with basic detils"""
    #def details(self):
    def __init__(self):
        self.name="indra"
        self.place="kowkuntla"
        self.branch="mech"
#a=student()
#a.details()
#print(a.name)
a=students()
print(a.name, "is  in",a.place)
print(a.__dict__)#name space
'''
'''#wepronounce as dunders
a=5;b=3
print(a+b)

print(a.__add__(25))
print(a.__divmod__(b))
print(a.__ge__(b))
a=[1,5,8,9,6]
print(len(a))
print(a.__getitem__(2))

#those special metids for any object are terms
#as margic methods
'''
'''#create a student class to accept marks and
#other details as input and evaluate the grades
#we will use__init__() for object intilization
class students:
    """students class with constructor"""
    def __init__(self,name="abc",marks=100):
        self.name=name
        self.marks=marks
        #instance methods
    def display(self):
            print(f'students  name is{self.name}')
            print(f'he/she got {self.marks}marks')
#a=Students()#default attributes
#a.display()
#b=Students("uma",250)
#b.display()
               #instance method to evaluate grade
    def evaluate(self):
        if self.marks>=700:
             print(f'he/she secured first grade')
        elif self.marks>=500:
             print(f'he/she secured second grade')
        else:
              print(f'sorry you are failed prepare well')
#a=students()
#a.display()
#a.evaluate()
#let's  make it dynamic to accpt n number
n=int(input("entre the number of students"))
for i in range(n):
    x=input("enter the student name")
    y=int(input("enter the marks"))
    a=students(x,y)
    a.display()
    a.evaluate()
    print('----------')'''
#A function is like a house whereas class is like
    #a power house
    
#exception handling
#errors that occur during execution can be
#handled by try,except statement along with
#finally keyword
#errors-->runtime errors,logical errors,
#syntax errors
#syntax errors--> invalid syntax,indenation,
#mismatch bracess...learner should avoid them
#runtime errors--> value errors,index errors,
#type errors,attribute errors...-->try,except
#will be closed by finally block
#logical errors and syntax errors are to be
#handled by programmera/users
#every try block must have one or more except
#blocks
#simple usecase for try-except block wiyh assert usage


#usage of assert(mainly for debugging)
#syntax for assert-->assert expression,message
#assserta>0
#assert a>0,"enter anly+ve numbers"
#print(a**b)
                                                              
#as in above case we made message along with
#assertion error lrt's handle it

'''try:
    a,b=map(int,input("enter the values").split(','))
    print(a,b)
    assert a>0,"enter only+ve numbers"
k.n,    print(a**b)
#except:   
#print("wrong input")

except Exception as e:
    print(e)
'''
#has now will  write individuval except blocks
try:
    a,b=map(int,input("enter the values").split(','))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("enter denominator other than zero")
except ValueError:
    print("float/str cannot be taken")
except Exception as e:
    print(e)




























