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
    return weight / (height ** 2)

bmi = calculate_bmi(70, height)
print(f"BMI: {bmi:.2f}")

# 8. List Comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

# 9. Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
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
