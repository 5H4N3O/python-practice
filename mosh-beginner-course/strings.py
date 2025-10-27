course = "Python Programming"

# len Returns number of chars in string
print(len(course))

# Use [] and : to slice strings
# [] returns the i+1th char of the string
print(course[0])

# The first char starting from the end
print(course[-1])

# Chars 0-3
print(course[0:3])

# Chars 0-end
print(course[0:])

# Chars before 3
print(course[:3])

print(course[:])

# Escape Character (\)
# \'
# \\
# \n
course = "Python \nProgramming"
print(course)

# Format Strings f''
first = "Shane"
last = "Pratt"

full = first + " " + last
print(full)

full = f"{first} {last}"
print(full)

full = f"{len(first)} {last}"
print(full)

full = f"{len(first)} {2 + 2}"
print(full)

# String methods
course = "    python programming    "
course_capital = course.upper()
print(course_capital)
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)
