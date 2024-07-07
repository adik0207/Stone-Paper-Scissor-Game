import random

print("How the game works \n 1. If Stone Vs Paper, then Paper wins \n 2. If Paper Vs Scissor, then Scissor wins \n 3. If Scissor Vs Stone, then Stone wins")

while True:
    # Taking input from user
    print("Enter a number \n Type 1 for Stone \n Type 2 for Paper \n Type 3 for Scissor : ")
    choice = int(input())
    
    # Checking for invalid input
    if choice > 3 or choice < 1:
        choice = int(input("Please enter a valid number 😊: \n"))
    
    # Taking user's choice
    if choice == 1:
        choice_name = "Stone"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
        
    # Printing user choice
    print("You chose : ", choice_name)
    
    # Computer's turn
    print("Now it's Computer's turn ........")
    
    # Declaring and initializing a variable for computer to choose a number randomly using randint function
    comp_choice = random.randint(1, 3)
    
    # Initializing choice of Computer
    if comp_choice == 1:
        comp_choice_name = "Stone"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"
    
    # Printing choice of Computer
    print("Computer chose : ", comp_choice_name)
    
    print(choice_name, " Vs ", comp_choice_name)
    
    # Check for draw
    if choice == comp_choice:
        print("Draw")
        result = 'Draw'
    
    # Check for win
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("Paper Wins")
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Stone Wins")
        result = 'Stone'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        print("Scissor Wins")
        result = 'Scissor'
    
    # Print either user win or computer win or draw
    if result == 'Draw':
        print("It's a draw")
    elif result == choice_name:
        print("User Wins!")
    else:
        print("Computer Wins!")
    
    # Ask if user wants to play again
    print("Do you want to play again? (Y/N)")
    answer = input().lower()
    
    # if user types n/N come out of the loop
    if answer == 'n':
        break

print("Thank You For Playing")
