#Project 2 Driver

'''
Created 2/7/2025
'''

import sort
import time
import random

div = "\n-------------------------\n"

def printArray(array):
    for x in array:
        print(x, end = " ")
    print('\n')
    
def genArray(n):
    array = random.sample(range(10*n), n)
    return array
    
if __name__ == "__main__":
    #commonly repeated messages held in variable (to prevent typos or inconsistency in messages)
    caseMenu = f"Case Scenarios for %s {div}1. Best Case\n2. Average Case\n3. Worst Case\n4. Exit %s"
    nTest = "For N = %d,\t it takes %d seconds"
    
    caseMes = "Select the case: "
    nMes = "Do you want to input another N (Y/N)? "
    nWhat = "What is the N? "
    
    best = "In best case,\n"
    average = "In average case,\n"
    worst = "In worst case,\n"
    
    error = "Invalid input\n"
    
    print("Welcome to the test suite of selected sorting algorithms!\n\n")
    
    while True:
        print("Select the sorting algorithm you want to test.",
              div,
              "1. Bubble Sort\n",
              "2. Merge Sort\n", 
              "3. Quick Sort\n",
              "4. ??? Sort\n",
              "5. Exit")
        user = input("Select a sorting algorithm: ")
        
        if user == "1": #Bubble Sort
            while True:
                print(caseMenu % ("Bubble Sort", "bubble sort test"))
                user = input(caseMes) #Choose best, average, worst, exit case
                print ()
                
                if user == "1": #Best Case
                    print(best)
                    for x in range(3):
                        y = 10 ** (x+2)
                        
                        array = genArray(y).sort()
                        
                        t1 = time.perf_counter()
                        #call bubble sort on array
                        t2 = time.perf_counter()
                        
                        print(nTest % (y, t2-t1))
                    while True:
                        user = input('\n' + nMes)
                        if user.lower() == "y":
                            user = input(nWhat)
                            try:
                                array = genArray(int(user)).sort()
                            except:
                                print(error)
                            else:
                                array = genArray(int(user)).sort()
                                
                                t1 = time.perf_counter()
                                #call bubble sort on array
                                t2 = time.perf_counter()
                                
                                print(nTest % (int(user), t2-t1))
                        else:
                            break
                elif user == "2": #Average Case
                    print(average)
                    for x in range(3):
                        y = 10 ** (x+2)
                        
                        array = genArray(y)
                        
                        t1 = time.perf_counter()
                        #call bubble sort on array
                        t2 = time.perf_counter()
                        
                        print(nTest % (y, t2-t1))
                    while True:
                        user = input('\n' + nMes)
                        if user.lower() == "y":
                            user = input(nWhat)
                            try:
                                int(user)
                            except:
                                print(error)
                            else:
                                array = genArray(int(user))
                                
                                t1 = time.perf_counter()
                                #call bubble sort on array
                                t2 = time.perf_counter()
                                
                                print(nTest % (int(user), t2-t1))
                        else:
                            break
                elif user == "3": #Worst Case
                    print(average)
                    for x in range(3):
                        y = 10 ** (x+2)
                        
                        array = genArray(y).sort(reverse=True)
                        
                        t1 = time.perf_counter()
                        #call bubble sort on array
                        t2 = time.perf_counter()
                        
                        print(nTest % (y, t2-t1))
                    while True:
                        user = input('\n' + nMes)
                        if user.lower() == "y":
                            user = input(nWhat)
                            try:
                                int(user)
                            except:
                                print(error)
                            else:
                                array = genArray(int(user)).sort(reverse=True)
                                
                                t1 = time.perf_counter()
                                #call bubble sort on array
                                t2 = time.perf_counter()
                                
                                print(nTest % (int(user), t2-t1))
                        else:
                            break
                        
                    
                elif user == "4": #Exit Case
                    break
                
                else:
                    print(error)
        elif user == "2": #Merge Sort
            print(caseMenu % ("Merge Sort", "merge sort test"))
            user = input(caseMes) #Choose best, average, worst, exit case
            print ()
            
            if user == "1": #Best Case
                print(best)
                for x in range(3):
                    y = 10 ** (x+2)
                    
                    array = genArray(y).sort()
                    
                    t1 = time.perf_counter()
                    sort.mergeSort(array, 0, (len(array)-1))
                    t2 = time.perf_counter()
                    
                    print(nTest % (y, t2-t1))
                while True:
                    user = input('\n' + nMes)
                    if user.lower() == "y":
                        user = input(nWhat)
                        try:
                            array = genArray(int(user)).sort()
                        except:
                            print(error)
                        else:
                            array = genArray(int(user)).sort()
                            
                            t1 = time.perf_counter()
                            sort.mergeSort(array, 0, (len(array)-1))
                            t2 = time.perf_counter()
                            
                            print(nTest % (int(user), t2-t1))
                    else:
                        break
            elif user == "2": #Average Case
                print(average)
                for x in range(3):
                    y = 10 ** (x+2)
                    
                    array = genArray(y)
                    
                    t1 = time.perf_counter()
                    sort.mergeSort(array, 0, (len(array)-1))
                    t2 = time.perf_counter()
                    
                    print(nTest % (y, t2-t1))
                while True:
                    user = input('\n' + nMes)
                    if user.lower() == "y":
                        user = input(nWhat)
                        try:
                            int(user)
                        except:
                            print(error)
                        else:
                            array = genArray(int(user))
                            
                            t1 = time.perf_counter()
                            sort.mergeSort(array, 0, len(array)-1)
                            t2 = time.perf_counter()
                            
                            print(nTest % (int(user), t2-t1))
                    else:
                        break
            elif user == "3": #Worst Case
                print(average)
                for x in range(3):
                    y = 10 ** (x+2)
                    
                    array = genArray(y).sort(reverse=True)
                    
                    t1 = time.perf_counter()
                    sort.mergeSort(array, 0, len(array)-1)
                    t2 = time.perf_counter()
                    
                    print(nTest % (y, t2-t1))
                while True:
                    user = input('\n' + nMes)
                    if user.lower() == "y":
                        user = input(nWhat)
                        try:
                            int(user)
                        except:
                            print(error)
                        else:
                            array = genArray(int(user)).sort(reverse=True)
                            
                            t1 = time.perf_counter()
                            sort.mergeSort(array, 0, (len(array)-1))
                            t2 = time.perf_counter()
                            
                            print(nTest % (int(user), t2-t1))
                    else:
                        break
                    
                
            elif user == "4": #Exit Case
                break
            
            else:
                print(error)
        elif user == "3": #Quick Sort
            pass
        elif user == "4": #??? Sort
            pass
        elif user == "5": #Exit
            break
        else: #Errorcase
            print(error)

    print("Goodbye!")
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
