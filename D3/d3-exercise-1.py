from math import *
from statistics import *

all_numbers = [1, 2, 11, 12, 50]
"""while True:
    user_input = input("Please give a number: ")

    if user_input == "":
        break

    number = int(user_input)
    all_numbers.append(number)"""

print(f"Min: {min(all_numbers)}")
print(f"Max: {max(all_numbers)}")
print(f"Sum: {sum(all_numbers)}")
print(f"Mean: {mean(all_numbers)}")
print(f"Median: {median(all_numbers)}")
print(f"Mode: {mode(all_numbers)}")


