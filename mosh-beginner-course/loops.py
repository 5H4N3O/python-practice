##### For Loops #####
print("\n# For Loops #")

# for(int i = 0; i++; i < 3), number is iterator
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# Iterator starts at 1 and goes till < 10, increases by 2 each time
for number in range(1, 10, 2):
    print("Attempt", number, (number * "."))

##### For...Else #####
print("\n# For...Else #")

successful = True
# Else will only execute if loop completes WITHOUT an early termination
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

##### Nested Loops #####
print("\n# Nested Loops #")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

##### Iterables #####
print("\n# Iterables #")

print(type(5))
print(type(range(5)))
# Range is iterable

# Strings are iterable
for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

##### While Loops #####
print("\n# While Loops #")

number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

##### Infinite Loops #####
print("\n# Infinite Loops #")

# Always have a way to break out of infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
