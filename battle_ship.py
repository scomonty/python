from random import randint

board = []

for o in range(0,5):
  i= ['O'] * 5
  board.append(i)
   
def print_board(board):
  # creates the game board
  for row in board:
    row = ' '.join(row)
    print(row)
	
	
def random_row(board):
#creates random number for the row
  return randint(0, len(board) - 1)
  
def random_col(board):
#creates random number for the column
  return randint(0, len(board) - 1)
  
ship_row = random_row(board)
ship_col = random_col(board)
print_board(board)
#print(ship_row) # reveals answer
#print (ship_col) # reveals answer


for turn in range(4):
  print('Turn', turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_col == ship_col and guess_row == ship_row:
    print("Congratulations! You sank my battleship!")
    break
  else:
      if guess_row not in range(5) or guess_col not in range(5):
        print("ooops! That's not even in the ocean!")
      elif board[guess_row][guess_col] == 'X':
        print ("You already guessed that!")
      else:
        print ("Miss!")
        board[guess_row][guess_col] = 'X'
        if turn == 3:
          print ('You ran out of tries!')
          break
  print_board(board)