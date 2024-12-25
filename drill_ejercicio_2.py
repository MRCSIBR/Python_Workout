# Python Drill Exercise

# 1. Variables and Data Types
name = "Alice"
age = 30
height = 1.75
is_student = False

# 2. String Operations
full_name = f"{name} Johnson"
greeting = "Hello, " + full_name
print(greeting.upper())

# 3. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits[1:3])

# 4. Dictionaries
person = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person.get("occupation", "Not specified"))

# 5. Conditional Statements
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# 6. Loops
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

# 7. Functions
def calculate_bmi(weight, height):
    """Calculates the BMI given weight and height"""
    return weight / (height ** 2)

bmi = calculate_bmi(70, height)
print(f"BMI: {bmi:.2f}")

# 8. List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

# 9. Error Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Operation attempted")

# 10. File Operations
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 11. Importing Modules
import random
print(random.choice(fruits))

# 12. Lambda Functions
multiply = lambda x, y: x * y
print(multiply(4, 5))

# 13. Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

# 14. Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))  # prints 0
print(next(gen))  # prints 1

# 15. Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 16. Class and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.greet()

# 17. Inheritance
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

employee = Employee("Jane", 25, 50000)
employee.display_details()

# 18. Exception Handling with Custom Exceptions
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance}")

account = BankAccount(1000)
try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print(e)

# 19. Regular Expressions
import re
text = "Hello, my phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())

# 20. Multithreading
import threading
import time

def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in "abcdefghij":
        time.sleep(1)
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
