# def is_consec(nums_list):
#     return sorted(nums_list) == list(range(min(nums_list), max(nums_list)+1))



# print(is_consec([1,2,3,4,7]))


# def moveZeros(numList):
#     return [num for num in numList if num != 0] + [num for num in numList if num == 0]


# print(moveZeros([0,1,2,3,0,4]))


# For this project, you will individually create a program that has a "player" and a "computer" advisary. The computer should randomly choose it's decision based on a list of actions it can take ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision. If player and computer choose the same decision then display ("Game Tied"), If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), if the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose") and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose") -- Vice versa for other descisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").

# In this project, you will need to use the random.randint function to enable to computer to make a random decision. Full documentation on the use of this function is attached in a link to this assignment.

# Once completed, commit your code to github and submit the link to this assignment.


import random


def rps():

    application_running = True
    while application_running:

        choices = ['rock', 'paper', 'scissors']
        computerChoice = random.choice(choices)

        choice = input("Enter your input here: Rock/Paper/Scissors/I quit ").lower()
        
        if choice == computerChoice:
            print(f"The computer chose {computerChoice}")
            print("Game Tied")
        elif choice == "rock" and computerChoice == "paper":
            print(f"The computer chose {computerChoice}")
            print("You Lose")
        elif choice == "paper" and computerChoice == "scissors":
            print(f"The computer chose {computerChoice}")
            print("You Lose")
        elif choice == "scissors" and computerChoice == "rock":
            print(f"The computer chose {computerChoice}")
            print("You Lose")
        elif choice == "rock" and computerChoice == "scissors":
            print(f"The computer chose {computerChoice}")
            print("You Win")
        elif choice == "paper" and computerChoice == "rock":
            print(f"The computer chose {computerChoice}")
            print("You Win")
        elif choice == "scissors" and computerChoice == "paper":
            print(f"The computer chose {computerChoice}")
            print("You Win")
        elif choice == "i quit":
            print("Thank you for playing")
            application_running = False
        else:
            print(f"Error: {choice} not recognized, try again")
    
rps()