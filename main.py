# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:26:08 2025

@author: Kade
"""

import functions

def main():
    error = "Invalid Input"
    inputText = "Enter your choice: "
    s = "\n\n" #extra space between menus
    
    encryptedMessages = []
    signedMessages = []
    
    
    keys = functions.genKey() #keys[0] = e, keys[1] = d, keys[2] = n
    print("RSA keys have been generated.")
    
    while True:
        print("Please select your user type:\n" +
              "1. A public user\n" + 
              "2. The owner of the keys\n" + 
              "3. Exit Program" + s)
        userInput = input(inputText)
        
        if (userInput == "1"): #public user
            while True:
                print("As a public user, what would you like to do?\n" + 
                      "1. Send an encrypted message.\n" + 
                      "2. Authenticate a digital signature.\n" + 
                      "3. Exit" + s)
                userInput = input(inputText)
                
                if (userInput == "1"): #send encrypted message
                    messageEncrypt = input("Enter a message: ")

                    #encrypt message here
                    
                    #send message here
                    encryptedMessages.append(messageEncrypt)
                    
                    print("Message encrypted and sent." + s)
                elif (userInput == "2"): #Authenticate a digital signature
                    if(len(signedMessages) > 0):
                        while True:
                            for i, j in zip(range(len(signedMessages)), signedMessages): #present list of messages availble
                                print(f"{i+1}. {j}")
                                
                            userInput = input(inputText)
                            
                            try:
                                int(userInput)
                            except:
                                print(error)
                                continue
                            
                            if (int(userInput)-1 in range(len(signedMessages))):
                                #authenticate signature
                                authentic = True #put authentication here
                                if authentic:
                                    print("Signature is valid."+ s)
                                else:
                                    print("Signature is invalid."+ s)
                                break
                            else:
                                print(error)
                    else:
                        print("There are no signatures to authenticate." + s)
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
                      "5. Exit" + s)
                userInput = input(inputText)
                
                if (userInput == "1"): # decrypt received messages
                    if (len(encryptedMessages) > 0): #if there are messages to decrypt
                        while True:
                            #present numbered list of messages of (length = n) here
                            print("The following messages are available: ")
                            
                            for i, j in zip(range(len(encryptedMessages)), encryptedMessages):
                                print(f"{i+1}. {j}")
                            userInput = input(inputText)
                            
                            try:
                                int(userInput)
                            except:
                                print(error)
                                continue
                            
                            if(int(userInput)-1 in range(len(encryptedMessages))):
                                #decrypt message
                                print("Decrypted message: ")
                                break
                            else:
                                print(error)
                                continue
                            print(s)
                    else:   #if there are no messages to decrypt
                        print("No messages available to decrypt." + s)
                        
                elif (userInput == "2"): #digital signature
                    signMessage = input("Enter a message: ")
                    
                    #sign message
                    
                    #send message
                    signedMessages.append(signMessage)
                    
                    print("Message signed and sent." + s)
                    
                elif (userInput == "3"): #Show keys
                    print("The current keys are:\n" +
                          f"encryption key: {keys[0]}\n" +
                          f"decryption key: {keys[1]}{s}")
                    
                    
                elif (userInput == "4"): #generate new keys
                    keys = functions.genKey()
                    print("New keys generated." + s)
                    
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