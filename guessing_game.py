import random

rand_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

while len(guessed_nums)<allowed_guesses:
  guess=input("Guess a number between 1 and 10: ")
  
  try:
    player_num = int(guess)
    
  except:
    print("That's not a whole number!")
    break
    
  if not player_num > 0 or not player_num < 11:
    print("That number is not between 1 and 10!")
    break
  
  guessed_nums.append(player_num)  
    
  if player_num == rand_num:
    print ("You Win!!! My number was {}.".format(rand_num))
    print("IT took you {} trys to get it right.".format(len(guessed_nums)))
    break
          
  else: 
    if player_num < rand_num:
      print("Wrong! Guess higher! Guess #{}".format(len(guessed_nums)))
          
    else: 
      print("Wrong! Guess lower! Guess #{}".format(len(guessed_nums)))
  
    continue
if not rand_num in guessed_nums:
  print("GAME OVER! Better go back to the wood shed and polish up your skills.")
  print("My number was {}.".format(rand_num))