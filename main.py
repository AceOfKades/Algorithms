# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:26:08 2025

@author: Kade
"""

def main():
    error = "Invalid Input"
    inputText = "Enter your choice: "
    
    #generate RSA here
    print("RSA keys have been generated.")
    
    while True:
        print("Please select your user type:\n" +
              "1. A public user\n" + 
              "2. The owner of the keys\n" + 
              "3. Exit Program")
        userInput = input(inputText)
        
        if (userInput == "1"): #public user
            while True:
                print("As a public user, what would you like to do?\n" + 
                      "1. Send an encrypted message.\n" + 
                      "2. Authenticate a digital signature.\n" + 
                      "3. Exit")
                userInput = input(inputText)
                
                if (userInput == "1"): #send encrypted message
                    messageEncrpyt = input("Enter a message: ")
                    #encrypt message here
                    #send message here
                    print("Message encrypted and sent.")
                elif (userInput == "2"): #Authenticate a digital signature
                    #if there are messages:
                        #while True:
                            #present list of messages availble
                            #if selection is valid:
                                #authenticate signature
                                #if authentic:
                                    #print("Signature is valid.")
                                #else:
                                    #print("Signature is invalid.)
                                #break
                            #else:
                                #print(error)
                    #elif there are not messages:
                        #print("There are no signature to authenticate.)
                    print("code is happening here...") #placeholder to indicated this optioon was selected
                elif (userInput == "3"): # exit
                    break
                else:
                    print(error)
                    continue
                    
                
        elif (userInput == "2"): #owner of keys
            while True:
                print("As the owner of the keys, what would you like to do?\n" +
                      "1. Decrypt a received message\n" + 
                      "2. Digitally sign a message\n" + 
                      "3. Show the keys\n" +
                      "4. Generate a new set of the keys\n" +
                      "5. Exit")
                userInput = input(inputText)
                
                if (userInput == "1"): # decrypt received messages
                    #while True:
                        print("The following messages are available: ")
                        #present numbered list of messages of (length = n) here
                        #userInput = input(inputText)
                        #if valid choice:
                            #decrypt message
                            #print("Decrypted message: " + decrypted message)
                            #break
                        #else:
                            #print(error)
                            #continue
                elif (userInput == "2"): #digital signature
                    signedMessage = input("Enter a message: ")
                    #sign message
                    print("Message signed and sent.")
                    
                elif (userInput == "3"): #Show keys
                    print("The current keys are: ")
                    #display keys
                    
                elif (userInput == "4"): #generate new keys
                    #generate new keys
                    print("New keys generated.")
                    
                elif (userInput == "5"): #exit
                    break
                else:
                    print(error)
                    
        
        
        elif (userInput == "3"): #exit program
            break
        
        else:
            print(error)
            continue
            
    print("Goodbye!")
    return

main()
    