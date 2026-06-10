# introduction to polymorphism
'''class One:
    def do_it(self):
        print("do_it from one")
        
    def doanything(self):
        self.do_it()
        
class Two(One):
    def do_it(self):
        print("do_it from Two")
        
one = One()
two = Two()
one.doanything()
two.doanything()

#MRO IN PYTHON
def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n
    
print("-----------")
print("reciprocal(2):", reciprocal(2))
print("------------")
print("reciprocal(0): ", reciprocal(0))
print("------------")

def reciprocal(n):
    try:
        n = 1/n
    except ZeroDivisionError:
        print("Division failed")
        n = None
        
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n
    
print("--------")
print("reciprocal(2):", reciprocal(2))
print("----------")
print("reciprocal(0):",reciprocal(2))
print("---------")
print("reciprocal(0):", reciprocal(0))

try:
    i = int("Hello")
except Exception as e:
    print(e)
    print(e.__str__())'''
    

class MYZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MYZeroDivisionError("some worse news")
    else:
        raise ModuleNotFoundError("some bad news")
 
do_the_division(False)   
do_the_division('mine')

