#importing random package
import random

#GUESS THE NUMBER
#variable declaration
lowest_no = 1
highest_no = 100
#inorder to store the guessing count guesses variable is used
guesses = 0
#flag variable will help to continue the loop until the correct number is guessed by the player
flag = True
#random.randrange will help to generate random values between the range 100 to 200
the_number = random.randint(1, 100)
print("Welcome to the Guess the Number game!")
print(f"Select the number between {lowest_no} and {highest_no}")
#untill the flag is false while will continue to run
while flag:
    #player_guess variable will hold the no entered by the player
    player_guess = input("Enter the number")
    #isdigit() method will check whether player had entered digit or string
    if player_guess.isdigit():
        #if player had entered digit value converted to int
        player_guess = int(player_guess)
        #guess count will get incremented until the player enters the correct number
        guesses += 1
        #checking guess number is greater than or less than the actual number
        if player_guess < lowest_no or player_guess > highest_no:
            print("Number is out of range")
            print(f"Please enter a number between {lowest_no} and {highest_no} range")
            #if guess number is too low this part will get executed
        elif player_guess < the_number:
            print("Too low! try again")
            #if guess number is too high this part will get executed
        elif player_guess > the_number:
            print("Too high! try again")
        else:
            #if player entered the correct number this part will get executed
            print(f"Congratulations! The entered number is correct{the_number}")
            print(f"The number of guesses {guesses}")
            #once number gets matched flag will turn false and looping will get terminated
            flag = False
    else:
        #if player entered string or character value it will trough invalid guess message
        print("Invalid Guess")
        print(f"Please enter a number between {lowest_no} and {highest_no} range")



#WORD SCRAMBLE
#creating a words list
words = ['python','javascript','java','automation','pytest','guvi','selenium']
#variable declaration
attempts = 0
flag_value = True
#selected_words variable is used to store the random value selected from the words list
selected_words = random.choice(words)
#selected word are stored in character list
character = list(selected_words)
#using random.shuffle letters are getting shuffled to create scrambled letters
random.shuffle(character)
#scrambled_word variable will store scrambled word
scrambled_word = "".join(character)
print("Scrambled word:",scrambled_word)
while flag_value:
    # getting player input
    guess = input("Enter the correct word: ")
    #checking whether the selected value and scrambled value is getting matched
    if guess.lower() == selected_words.lower():
        attempts += 1
        print("Congratulations! You have guessed the word in " + str(attempts) + " attempts.")
        flag_value = False
    else:
        #if player guess is wrong this part will get executed
        attempts += 1
        print("Incorrect. Try again.")
