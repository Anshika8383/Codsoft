"""""
WORKFLOW OF PROJECT:
computer science(computer will choose randomly not conditionally)
result project

cases:
A - Rock
Rock - Rock = tie
Rock - paper = paper  win
Rock - scissor = Rock win

B - Paper
paper - Rock = tile
Paper - Rock = Paper win
paper = scissor = scissor win

C - Scissor
Scissor - paper = tie
Scisor - Rock = paper win
Scissor - scissor = scissor win

"""


import random
item_list = ["Rock", "paper", "scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor=):")
comp_choice = random.choice(item_list)

print("user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
      print("Both  chooses same: = Match Tie")

elif user_choice == "Rock":
     if comp_choice == "paper":
          print("Paper covers Rock = Computer win")
     else:
          print("Rock smashes Scissor = you  win")

elif user_choice == "Paper":
     if comp_choice ==  "Scissor":
          print("Scissor cuts paper, Computer win")
     else:
          print("paper covers rock, You win")
           
elif user_choice == "Scissor":
     if comp_choice ==  "Rock":
          print("Rock smashes  scissor, computer win")
     else:
          print("Scissor cuts paper, you win")

else:         
     print("Invalid input.Please enter Rock, Paper or scissor.")
while True:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower()!= "yes" "No":
     print("Thaks for playing!")
     break
