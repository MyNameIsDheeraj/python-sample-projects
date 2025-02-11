import random

list_word = ["superman", "batman", "wonder women"]
word = random.choice(list_word)

#to create a length of the random word lengthe list with all index has "_"
display_word = ["_"]*len(word)

print(word)

#createing a veriable to check the continue the game
game_over = False
while not game_over:
    special_letter = input("Enter a letter ").lower()
    for i in range(0,len(word)):
        
        if special_letter == word[i]:
            # print(word[i], end="")
            display_word[i] = word[i]
            # else:
            #     # print("_", end=" ")
            #     display_word[i] = "_"
    print(display_word)

#checking the _ not in the random word
    if "_" not in display_word:
        print("Your Win!...")
        
        #changing the game over variable to true to stop the while loop
        game_over = True