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
    print(e.__str__())
    

class MYZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MYZeroDivisionError("some worse news")
    else:
        raise ModuleNotFoundError("some bad news")
 
do_the_division(False)   
do_the_division('mine')

 # String
city = 'Bhopal'
print(city[0])
print(city[2])

print(city[-1])
print(city[5])

print(city[-3])
print(city[3])

#Slicing: string[start:stop:step]
name = "Priys Sharma"
print(name[0:5])
print(name[6:])
print(name[:5])
print(name[::2])
print(name[::-1])

#Length of string
print(len(name))

text = "Hello python world"
# case
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

# strip whitespace
print(text.strip())

#search
print('python' in text)
print(text.find('python'))
print(text.count('l'))

#replace
print(text.replace('python', 'AI'))

#split and join
csv = 'Rahul,22,Bhopal,Engineer'
parts = csv.split(',')
print(parts)
print(parts[0])
rejoined ='|'.join(parts)
print(rejoined)

#check content
print('hello123'.isalnum())
print('122345'.isdigit())
print('python'.isalpha())
print(' '.isspace())

#start/end check
email = 'student@gmail.com'
print(email.endswith('.com'))
print(email.startswith('stu'))

name, marks, rank = 'Anita', 97.567, 3

#Basic
print(f'Hello, {name}!')

#format numbers
print(f'Marks:{marks: .2f}')
print(f'Marks:{marks:.0f}')
print(f'count:{1000000:,}')

#padding and alignment
print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')#left/right align

#Expressions inside {}
price, gst = 500, 0.18
print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f}|Total:Rs.{price*(1+gst):.2f}')

# padding and alignment

print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')#left/right
print(f'hello {name:^10}')
print(f'hello{name:<10}')
print(f'hello{name: *^11}')

price,gst = 500, 0.18
print(f'price:Rs..{price}| GST:Rs')


string = "hello,How are you doing today?
count vowels in the string
print you from the string
print the string in reverse order
non_polin, palin = "abcdef","axttxa"
#check if the string is palindrome or not


string = "hello, How are you doing today"
vowel = ['a','e','i','o','u']
count = 0
lower_string = string.lower

for i in lower_string:
    for i in vowel:
        count += 1
        
print(f'total vowel:{count}')'''

#miscellaneou
with open("data.txt","r") as file:
    data = file.read()
print(data)

with open('student.txt', 'w') as f:
    f.write('Rahul Sharma,85,Bhopal\n')
    f.write('priya Verma,92,Indore \n')
    f.write('Amit kumar,73,Jabalpur\n')
    
with open('student.txt', 'a') as f:
    f.write('sneha Joshi,88,Bhopal\n')
    
with open('student.txt', 'r') as f:
    content = f.read()
print(content)

with open('student.txt', 'r') as f:
    for line in f:
        name, marks, city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("---------")









