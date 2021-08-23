import random

print("Rock...")
print("Papers...")
print("Scissors...")

options = ['rock', 'paper', 'scissors'];

human_choice  = input("Player 1, make your move:  ")
machine_choice = random.choice(options)

def play(human, machine):
  human = human.lower()
  machine = machine.lower()

  print({human_choice}, {machine_choice})

  if human == machine:
    print("draw")

  if human == 'rock' and machine == 'paper':
    print("machine wins")
  elif human == 'rock' and machine == 'scissors':
      print("human wins")
  elif human == 'scissors' and machine == 'paper':
    print("human wins")
  elif human == 'scissors' and machine == 'rock':
      print("mahine wins")
  elif human == 'paper' and machine == 'scissors':
    print("machine wins")
  elif human == 'paper' and machine == 'rock':
    print("human wins")
  else:
    print("invalid selections")
      
play(human_choice, machine_choice)
