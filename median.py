"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

listLeng = len(numbers)
numbers.sort()

if (listLeng % 2 !=0 ):
    print(numbers[listLeng // 2 ])
else:
    med = (numbers[listLeng // 2 ] + numbers[listleng // 2 - 1 ]) / 2
    print( med)
