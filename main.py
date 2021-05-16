import art
from game_data import data
import random
from replit import clear
print(art.logo)

a = []
b = []
play_game = True
score = 0
def detail():
  """
  Returns a random data from data list
  """
  details = random.choice(data)
  detail_list = list(details.values())
  return detail_list
a_details = detail()
b_details = detail()
if a_details == b_details:
  b_details = detail()

def game():
  print(f"Compare A: {a_details[0]}, a {a_details[2]} , from {a_details[3]}.")
  print(art.vs)
  print(f"Against B: {b_details[0]}, a {b_details[2]}, from {b_details[3]}")

def correct_answer():
  clear()
  print(art.logo)
  global a_details, b_details, score
  score += 1
  print(f"You're right! Current score: {score} ")
  a_details = b_details
  b_details = detail()
  game()
  
def wrong_answer():
  global play_game
  print(f"Sorry! That's wrong. Final score: {score} ")
  play_game = False


game()
while play_game:
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if user_choice == "a":
    if a_details[1] > b_details[1]:
      correct_answer()
    else:
      wrong_answer()
  else: 
    if b_details[1] > a_details[1]:
      correct_answer()
    else:
      wrong_answer()