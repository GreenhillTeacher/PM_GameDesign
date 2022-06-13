#Susie Fagelman
#Guessing Game with 3 lists using while loops

import random 
import os
Game=True #making the game = true is a way to eventually end the entire game by doing game=false

def option1 (): #this is to define option1 as i use it later in the code
    global cnt #global count is used so that it refers to and affects the entire game
    cnt=0 #count, this means that the user starts with 0 tries
    check=True 
    list1=['red','orange','green','blue', 'yellow', 'purple', 'pink', 'black', 'white', 'navy']
    theword= random.choice(list1) #this selects a random word from list 1
    while check and cnt <10: #this means that the user has less than 10 tries 
        guess=input("Please select your color: ") 
        if guess==theword:
            print("Congrats you got the right color!")
            check=False #this ends the loop
        else:
            print("Wrong color, try again! ")
        cnt+=1 #this count+1 is adding on a try as the user did not get the correct word first
    print('You guessed it in',cnt,'tries.')

def option2 (): #this defines the second list. the code for these next two lists are almost identical to the previous one.
    global cnt
    cnt=0
    check=True
    list1=['soccer','baseball','tennis','hockey','basketball','swimming','lacrosse','rugby','football','golf']
    theword= random.choice(list1)
    while check and cnt <10:
        guess=input("Please select your sport: ") 
        print()
        if guess==theword:
            print("Congrats you guessed the right sport!")
            check=False
        else:
            print("Wrong sport, try again!")
        cnt+=1
    print('You guessed it in',cnt,'tries.')

def option3 ():
    global cnt
    cnt=0 
    check=True
    list1=['apple','pinapple','grape','lemon','strawberry','blueberry','melon','blackberry','grapefruit','pear']
    theword= random.choice(list1)
    while check and cnt <10:
        guess=input("Please select your fruit: ") 
        print()
        if guess==theword:
            print("Congrats you guessed the right fruit!")
            check=False
        else:
            print("Wrong fruit, try again!")
        cnt+=1 
    print('You guessed it in',cnt,'tries')
    
  

while Game: #starts loop

    title= '|guessing game!                                                                          |'
    print(' ========================================================================================') #border
    print(title.upper()) #makes the title all uppercase
    #instructions
    print("|This is a guessing game where you guess a word from a list.                             |")
    print("|You get to pick what you went to guess on out of three lists with different categories  |")  
    print("|The three categories include: 1. Colors, 2. Sports, and 3. Fruits                       |")    
    print("|You have 10 tries to guess the right choice.                                            |")
    print("|If you use all of your guesses and never get the right word, you can just play again!   |")
    print(' ========================================================================================') #here to separate between instructions and game

    print(' ') #this gives a space betwen my instructions and the game


    name=input("What is your name? ")

    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        print('We are sorry to hear that, come back soon!')
        break #use break to end this certain loop as there are things that follow it
    while Game:
        choice=input("What game would you like to play 1,2, or 3? ")
        try:
            choice=int(choice)
            if choice > 0 and choice < 4:
                break
            else:
                print ("give me 1,2, or 3")
        except:
            print("Please enter a number ")
        
        os.system('cls')
        check=True
    if choice==1: #these means that if the user picks choice one, the code for that list is used 
        option1()
    if choice==2: #same for the other choices/options
        option2()
    if choice==3:
        option3()
        

    answer=input("Do you want to play again? ")
    if('n' or 'N') in answer:
        Game=False #end the entire game
        print("Thank you for playing my game!! ")