import random

game = ["rock", "paper", "scissors"]
print("""Lets play a Rock Paper Scissors game
Rock X Paper = Paper wins
Rock X Scissors = Rock wins
Paper X Scissors = Scissors wins \n""")


      
usr_choice = input("Please enter youre choice (Rock, Paper, Scissors) \n").lower()

while True:
    random_choice = random.choice(game)
    if usr_choice in game:
        
        if random_choice == usr_choice:
            print("Congratulation you win....!")
        else:
            print("Ohh...You lost")

        again = input("Do you wan try again (to confirm YES or Y) \n").lower()
        # print(again)
        if (again == "yes") or (again == "y"):
            usr_choice = input("""Lets play again Rock Paper Scissors game
Rock X Paper = Paper wins
Rock X Scissors = Rock wins
Paper X Scissors = Scissors wins 
please enter youre choice (Rock, Paper, Scissors) \n""").lower()
        else:
            break

    else:
        usr_choice = input("Please enter Rock, Paper, Scissors other wise the game will not goes forword \n")
    
