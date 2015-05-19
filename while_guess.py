from random import randint
random_number = randint(1, 10)
print (random_number)

guesses_left = 3


while guesses_left > 0:
  guess = int(input('Your guess: '))
  print (guesses_left)
  guesses_left -= 1
  if guess == random_number:
    print('You win!')
    break
else:
  print('You lose')