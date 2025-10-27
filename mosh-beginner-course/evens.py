evens = 0
for i in range(1, 10):
    if (i % 2) == 0:
        print(i)
        evens += 1
print(f"We have {evens} even numbers")
