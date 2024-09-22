from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

# Write ur function here
def findSecondLargest(sequenceOfNumbers):
    if len(sequenceOfNumbers) < 2:
        return None  # Not enough elements for a second largest

    max_number = second_max_number = None

    for i in sequenceOfNumbers:
        if max_number is None or i > max_number:
            second_max_number = max_number
            max_number = i
        elif i != max_number and (second_max_number is None or i > second_max_number):
            second_max_number = i

    return second_max_number if second_max_number is not None else -1


# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
