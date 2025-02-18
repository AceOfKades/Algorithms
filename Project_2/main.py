#Project 2 Driver

'''
Created 2/7/2025
'''

import sort
import time
import random

div = "\n-------------------------\n"

error = "Invalid input\n"

def printArray(array):
    for x in array:
        print(x, end = " ")
    print('\n')
    
def genArray(n, case_type):
    
    array = random.sample(range(10*n), n)
    
    if case_type == "1":
        array.sort()
    elif case_type == "3":
        array.sort(reverse = True)
    
    return array


def runTest (algorithm, array):
    t1 = time.perf_counter()
    
    if algorithm == sort.mergeSort:
        algorithm(array, 0, len(array)-1)
    else:
        algorithm(array)
        
    t2 = time.perf_counter();
    
    return t2 - t1
    

def handleCase(case_type, algorithm):
    
    
    nTest = "For N = %d,\t it takes %.6f seconds"
    nMes = "Do you want to input another N (Y/N)? "
    nWhat = "What is the N? "
    
    best = "In best case,\n"
    average = "In average case,\n"
    worst = "In worst case,\n"
    
    caseMessages = {
        "1": best,
        "2": average,
        "3": worst
    }

    print(caseMessages.get(case_type, "Invalid case"))
    
    for x in range(3):
        y = 10 ** (x+2)
        
        array = genArray(y, case_type)
        
        time = runTest(algorithm, array)
        
        print(nTest % (y, time))
        
    while True:
        user = input('\n' + nMes)
        if user.lower() == "y":
            user = input(nWhat)
            try:
                if case_type == "2": 
                    array = genArray(int(user))
                else:
                    array = genArray(int(user), case_type)
                    
                time = runTest(algorithm, array)
                
                print(nTest % (int(user), time))
            except:
                print(error)
        else:
            break
        
    

if __name__ == "__main__":
    #commonly repeated messages held in variable (to prevent typos or inconsistency in messages)
    caseMenu = f"Case Scenarios for %s Sort {div}1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit %s sort test"
    
    caseMes = "Select the case: "
    
    print("Welcome to the test suite of selected sorting algorithms!\n\n")
    
    while True:
        print("Select the sorting algorithm you want to test.",
              div,
              "1. Bubble Sort\n",
              "2. Merge Sort\n", 
              "3. Quick Sort\n",
              "4. Insertion Sort\n",
              "5. Exit")
        user = input("Select a sorting algorithm: ")
        
        if user == "1": #Bubble Sort
            while True:
                print(caseMenu % ("Bubble", "bubble"))
                user = input(caseMes) #Choose best, average, worst, exit case
                print ()
                
                if user in ["1", "2", "3"]: #Cases
                    handleCase(user, sort.bubbleSort)
                elif user == "4": #Exit Case
                    break
                else:
                    print(error)

        elif user == "2": #Merge Sort
            while True:
                print(caseMenu % ("Merge", "merge"))
                user = input(caseMes) #Choose best, average, worst, exit case
                print ()
                
                if user in ["1", "2", "3"]: #Cases
                    handleCase(user, sort.mergeSort)
                elif user == "4": #Exit Case
                    break
                else:
                    print(error)

        elif user == "3": #Quick Sort
            while True:
                print(caseMenu % ("Quick", "quick"))
                user = input(caseMes) #Choose best, average, worst, exit case
                print()
                
                if user in ["1", "2", "3"]:
                    handleCase(user, sort.quickSort)
                elif user == "4": # Exit Case
                    break
                else:
                    print(error)
                
        elif user == "4": #Insert Sort
            while True:
                print(caseMenu % ("Insertion", "insertion"))
                user = input(caseMes) #Choose best, average, worst, exit case
                print ()
                
                if user in ["1", "2", "3"]: #Cases
                    handleCase(user, sort.insertionSort)
                elif user == "4": #Exit Case
                    break
                else:
                    print(error)

        elif user == "5": #Exit
            break
        else: #Errorcase
            print(error)

    print("Goodbye!")
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
