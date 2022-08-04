#exception handling 

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


def fun(a):
    if a < 4:
        b = a/(a-3)
        print("Value of b = ", b)
      
try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled") 

#error raising
x= 'hello'
if not type(x) is int:
    raise TypeError('only integrs are allowed')
#finally 
try :
    print(x)
except:
    print("something went wrong")
finally:
    print('the try except is finished')

#encapsulation 
class student:
    def __int__(self,name,rollno,subject):
        self.name = name
        self.rollno = rollno
        self.subject = subject
    def show(self):
        print('name: ',self.name, 'roll no: ',self.rollno)
    def work(self):
        print(self.name,'is syudying in', self.subject)
st = student('arpit',2004548,'cse')
st.show()
st.work()
##########################################################
class A:
    __studentname = 'arpit'
    def set_studentname(arpit):
        self__studentname=arpit
    def get_studentname():
        return self.__studentname
ob = A()
ob.__studentname

#abstraction
from abc import ABC
class polygon(ABC):
    @abstractionmethod
    def sides(self):
        pass
class triangle(polygon):
    def sides(self):
        print('triangle has three sides')
        obj = triangle()
        obj.m1 ()

##################################################

