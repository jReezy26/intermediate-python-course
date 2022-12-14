import random

def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input("How many sides are on the dice you're rolling? "))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll
    if roll == 1:
      print(f'You rolled a {roll}! Sucks to suck.')
    elif roll == dice_size:
      print(f"You rolled a {roll}! Rack 'em and stack 'em.")
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()