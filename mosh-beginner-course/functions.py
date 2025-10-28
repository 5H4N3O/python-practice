##### Functions #####
print("\n# Functions #")


def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


##### Arguments #####
print("\n# Arguments #")


# Parameters are passed into functions
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


# Argument is actual value for given parameter
greet("Shane", "Pratt")
greet("John", "Smith")

##### Types of Functions #####
print("\n# Types of Functions #")
# 1 - Perform a task
# 2 - Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Shane")
print(message)
file = open("content.txt", "w")
file.write(message)


def greet(name):
    print(f"Hi {name}")


# Prints None, because that is the function's return value, all return None by default
print(greet("Sara"))

##### Keyword Arguments #####
print("\n# Keyword Arguments #")


def increment(number, by):
    return number + by


print(increment(2, 1))
print(increment(number=2, by=1))

##### Default Arguments #####
print("\n# Default Arguments #")


# Default by value of 1
# Default arguments need to
# come last in function def,
# cant do def increment(by=1, number)
def increment(number, by=1):
    return number + by


print(increment(2))
print(increment(2, 5))

##### xargs #####
print("\n# xargs #")


# numbers is a tuple of objects
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
print(multiply(10, 10))
