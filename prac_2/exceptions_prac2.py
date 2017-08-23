"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        num_1 = int(input("Please enter a number: "))
        num_2 = int(input("Please enter another number: "))
        result = num_1 + num_2
        print(result)
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)