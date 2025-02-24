#Project 2: sorting algorithms
"""
Created 2/7/2025
"""
import random

### MERGE SORT FUNCTIONS
def merge (array, left, mid, right):
    #define sizes of halves of array
    n1 = mid - left + 1
    n2 = right - mid
    
    #temporary arrays
    tempL = [0] * n1
    tempR = [0] * n2
    
    #fill arrays
    for i in range(n1):
        tempL[i] = array[left + i]
    for j in range(n2):
        tempR[j] = array[mid + 1 + j]
        
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into array[left..right]
    while i < n1 and j < n2:
        if tempL[i] <= tempR[j]:
            array[k] = tempL[i]
            i += 1
        else:
            array[k] = tempR[j]
            j += 1
        k += 1

    # Copy the remaining elements of tempL[],
    # if there are any
    while i < n1:
        array[k] = tempL[i]
        i += 1
        k += 1

    # Copy the remaining elements of tempR[], 
    # if there are any
    while j < n2:
        array[k] = tempR[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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