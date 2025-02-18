#Project 2 Driver

'''
Created 2/7/2025
'''

import sort
import time
import random

div = "\n-------------------------\n"

error = "Invalid input\n"
## Supporting Driver Arrays
    
def genArray(n, case_type): #generate an array
    
    array = random.sample(range(10*n), n) #generate an array of random numbers
    
    if case_type == "1": # if best case, sort
        array.sort()
    elif case_type == "3": # if worst case, sort and reverse
        array.sort(reverse = True)
    
    return array 


def runTest (algorithm, array): #test an algorithm
    t1 = time.perf_counter() #start timer
    
    if algorithm == sort.mergeSort: #if operating merge sort, input necessary parameters
        algorithm(array, 0, len(array)-1)
    else:
        algorithm(array)
        
    t2 = time.perf_counter(); #end timer
    
    return t2 - t1 #return time
    

def handleCase(case_type, algorithm): #operate driver functions on an algorithm and case
    
    #string literal variables for easy rewriting if necessary
    nTest = "For N = %d,\t it takes %.6f seconds" #for N = 100/1000/10000/etc it takes x.xxxxxx seconds
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
        y = 10 ** (x+2) #10 ^ 2, 3, 4; 100, 1,000, 10,000
        
        array = genArray(y, case_type) #create an array based on current size y and case chosen
        
        time = runTest(algorithm, array) #collect time from algorithm test
        
        print(nTest % (y, time)) #print result
        
    while True: #loop while user generates N
        user = input('\n' + nMes) #input N yes/no
        if user.lower() == "y": #if yes
            user = input(nWhat) #input number
            try: #test if input is valid for functions
                
                array = genArray(int(user), case_type) #generate array with user input
                    
                time = runTest(algorithm, array) #test algorithm
                
                print(nTest % (int(user), time)) #print results
            except:
                print(error)
        else: #if not yes, break
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
                    handleCase(user, sort.bubble_Sort)
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
                    handleCase(user, sort.Quick_Sort)
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
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
