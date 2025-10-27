temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

##### Ternary Operator #####
print("\n##### Ternary Operator #####")
age = 22

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

##### Logical Operators #####
print("\n##### Logical Operators #####")
high_income = False
good_credit = True
student = False

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if not student:
    print("Eligible")
else:
    print("Not Eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

##### Short-cicuit Evaluation #####
print("\n##### Short-circuit Evaluation #####")
high_income = False
good_credit = True
student = True

# Evaluation stops as soon as a False is seen
if high_income and good_credit and not student:
    print("Eligible")

# Evaluation stops as soon as a True is seen
if high_income or good_credit or not student:
    print("Eligible")

##### Chaining Comparison Ops #####
print("\n##### Chaining Comparison Ops #####")

# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")
