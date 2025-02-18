import random
import sys
import math


random.seed()

def randomize (amount):
    numbers = list(range(amount))
    
    for n in numbers:
        
        numbers[n] = random.randrange(0,999)
    
    for n in numbers:
        print(n)
        
        
    return numbers
    
    
    
def bubble_Sort(numbers):
    
    def swap(i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]

    n = len(numbers)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if numbers[i - 1] > numbers[i]:
                swap(i - 1, i)
                swapped = True
                    
    return numbers

    
def Quick_Sort(numbers):
    if len(numbers) <= 1:
        return numbers  # Base case: already sorted

    pivot = random.choice(numbers)  # Pick a random pivot

    left = [x for x in numbers if x < pivot]   # Elements smaller than pivot
    middle = [x for x in numbers if x == pivot]  # Elements equal to pivot
    right = [x for x in numbers if x > pivot]  # Elements greater than pivot

    return Quick_Sort(left) + middle + Quick_Sort(right)
