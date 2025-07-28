# Rock, Paper, Scissor Game
# 1 - rock
# 2 - Paper
# 3 - scissor

import random 

# the choices available to pick from
Choices = {"r" : 1, "p" : 2, "s" : 3}
reverse_Choices = {1 : "Rock", 2: "Paper", 3: "Scissor"}

# computer will pick one of the three
computer_num = random.choice([1,2,3])

#  user will input the pick
print("Choose any of the of the following:")
print("Rock(r), Paper(p), Scissor(s)")
user_selection = input("Enter your choice: ")

# if wrong input is given by the user
if(user_selection not in Choices):
    print("You have enter an invalid choice! (x ^ x)")
    exit() 

user_num = Choices[user_selection]

# Declaring the choice of the user and computer
print("")
print(f"Your choice is {reverse_Choices[user_num]}")
print(f"Computer choice is {reverse_Choices[computer_num]}")
print("And the result is --> ")

# rules for the game
if(user_num == computer_num):
    print("It is a Draw!")
elif(user_num == 1 and computer_num == 3):
    print("You Win! (^ w ^)") 
elif(user_num == 2 and computer_num == 1):
    print("You Win! (^ w ^)") 
elif(user_num == 3 and computer_num == 2):
    print("You Win! (^ w ^)") 
elif(user_num == 1 and computer_num == 2):
    print("You Lose! (! ^ !)") 
elif(user_num == 2 and computer_num == 3):
    print("You Lose! (! ^ !)") 
elif(user_num == 3 and computer_num == 1):
    print("You Lose! (! ^ !)") 
else:
    print("You have enter an invalid choice! (x ^ x)") 