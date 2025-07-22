#python q/a covered all topics ?

#functions and logic:( q1 to q10 )

#ans1
def numb(a):
    if a % 2 == 0 :
        print('yes it is even ')
    else:
        print('it is odd')
put=int(input("enter the no:"))
no=numb(put)
print(put)


#ans5
def vowl(y):
    count=0
    for i in y.lower():
        if i in  'a,e,i,o,u' :
         count+=1
    return count
str=input("enter the string:")
put=vowl(str)
print(put)

#ans6
def nu(a):
    sum1=0
    for i in range (1,a+1):
        digits=a%10
        sum1+=digits
        a=a//10
    return sum1
numb=int(input("enter the no:"))
print(f'the sum of digits of {numb} is {nu(numb)}')




#ans8
import math

def find_gcd(a, b):
    return math.gcd(a, b)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD is:", find_gcd(x, y))





#ans2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(0))


#ans3
def reverse_string(s):
    return s[::-1]
print(reverse_string("dev")) 


#ans4
def check(strin):
    if (strin==strin[::1]):
        print(f'yes it is palindrome!')
    else:

        print('not a palindrome')
check('madam')  





#ans10
def is_sorted(lst):
    return lst == sorted(lst)
print("Is the list sorted?", is_sorted([1, 2, 3, 4]))  
print("Is the list sorted?", is_sorted([1, 3, 2]))  



#ans9
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))



#ans7
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
terms = int(input("Enter number of terms: "))
result = fibonacci_recursive(terms)
print("Fibonacci series:", result)




# strings ,lists,tuples (q11 to q20):

#ans12
str=("the dog is bad")
print(str.replace("dog","cat"))


#ans11
lst="rohan is good boy "
print(lst.strip())


#ans13
lst=['rohan', 'is', 'good', 'boy' ]
result='_'.join(lst)
print(result)



#ans14
tup=(1,2,3,4,5)
total=0
for i in tup :
    total+=i
    print(total)



#ans16
list1=[1,1,2,3,4]
tup1=tuple(list1)
print(tup1)

#ans17
tup1=(1,2,3,4,5)
rev=tup1[::-1]
print(rev)

#ans18
tup = ("a", "b", "a", "c", "a", "d")
value = "a"

count = tup.count(value)
print("Count is:", count)


#ans19
t=(1,(2,3),4)
print(t[1][0])


#ans15
def remove_duplicates(input_list):
    return set(input_list)
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = remove_duplicates(my_list)
print(unique_set)


#ans20
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10      
        total += digit          
        number = number // 10    
    return total
num = 12345
print("Sum of digits:", sum_of_digits(num))





#set and dictionary (q21 to q28):

#ans21
set1={1,2,3}
set2={4,5,6}
print(set2.union(set1))


#ans22
set1={1,2,3}
set2={3,5,6}
print(set2.isdisjoint(set1))



#ans23
set1={1,2,3,4,5}
set2={4,5,6}
set3=set1.intersection(set2)
print(set3)
if set3==set():
    print("no elment is common")
else:
    print("common elements are :=",set3)



#ans24
text = "hello world"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)

#ans27
dict2={
    "mayank":20000,
    "dev":18000,
    "sumit":22000
}
swap={value:key for key , value in dict2.items()}       
print(swap) 



#ans26
score1={
    'physics':98,
    'maths':99,
    'chemistry':97
}
mark=dict(sorted(score1.items(),key=lambda item: item[1]))
print(score1)

#ans27

info1={
    'name':'mayank',
    'age':20,
    'mobile':9090999990
}
info1.pop('mobile')
print(info1)


#ans28
lst1=['a1','a2','a3']
lst2=[10,12,13]
dict3={}
for x,y in zip(lst1,lst2):
    dict3.update({x:y})
print(dict3)




#control flow and loops :(q29 to q33):
    
#ans29 
a=int(input("enter the num:"))

if (a>0):
        print("print positive :")
elif (a<0):
        print("print negative :")
else:
        print("print zero :")



#ans30
i=0
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")



#ans31
i=10
while i > 0 :
    print (i)
    i-=1



#ans32
word=(input("enter the no of vowels in a string="))
vowel=0
for i in word:
    if i.lower() in 'aeiou':
        vowel+=1
print(vowel)



#ans33
stri=("madam")
if stri ==stri [::-1]:
    print("yes it is palindrome ")
else:
    print("it is not palindrome")


# oops (q34 to q43):
# ans34
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

p = Person("Dev", 25)
p.display()

#ans35
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())


#ans36
class Secret:
    def __init__(self):
        self.__private_var = "This is private"

    def get_private(self):
        return self.__private_var

s = Secret()
print(s.get_private())

#ans37
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print("Balance:", self.balance)

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(500)
acc.display_balance()


#ans38
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

#ans39
class Grandparent:
    def house(self):
        print("Has a big house")

class Parent(Grandparent):
    def car(self):
        print("Drives a car")

class Child(Parent):
    def bike(self):
        print("Rides a bike")

c = Child()
c.house()
c.car()
c.bike()


#ans40
class Demo:
    @staticmethod
    def say_hello():
        print("Hello (Static Method)")

    @classmethod
    def show_class(cls):
        print(f"This is class: {cls.__name__}")

Demo.say_hello()
Demo.show_class()


#ans41
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)

    def __str__(self):
        return f"Point({self.x})"

p1 = Point(10)
p2 = Point(20)
p3 = p1 + p2
print(p3)

#ans42
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()


#ans43
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book Title: {self.title}"

b = Book("Python Programming")
print(b)










