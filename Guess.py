# import randint to generate the secret number 
from random import randint
#os package to remove files at last
import os

#sequence type to store points
points= [ 50, 40, 30, 20, 10]

# open file in append mode and read lines
f= open('guess.txt', 'a+')
f.seek(0,0)
content = f.read()

#check whether user completed any stage(s) already
if content != '':
  #split level and points at each level
  level, points_content = content.split(':')
  level= int(level)
  #store points of each level
  points_scored= list(map(int, points_content.rstrip(',').split(',')))

#if no stage(s) completed
else:
  level= 1
  points_scored= list()
f.close()

#loop for 3 levels
while (level <= 3):
  
  #complexity range for each stage
  end_number= level * 10
  secret_number= randint(1, end_number)

  #looping statment for 5 attempts at each stage
  for i in range(0, 5):
    #gets the guessing number as user input
    guess_number= int(input('Guess the secret number between 1 and {} ({} attempts left): '.format(end_number, 5-i)))

    #conditional statement to check guessing number 
    #is correct or higher or lower
    if (secret_number == guess_number):
      print('Your Guess is right, You won the level {} with {} points'.format(level, points[i]))

      points_scored.append(points[i])
      level += 1

      break

    elif (secret_number < guess_number):
      print('Your guess is higher than the secret number')

    else:
      print('Your guess is lower than the secret number')

  else:
    print('GAME OVER, You loose the game. Secret number is {}'.format(secret_number))

    #remove if user lose the game
    os.remove('guess.txt')
    break

else:
  print('CONGRATS ! You won the game with {} points out of 150.'.format(sum(points_scored)))

  for i in range(0,3):
    print(' Level {} : Points {}'.format(i+1, points_scored[i]))
  
  #remove if user wins the game
  os.remove('guess.txt')

