board = ['' for i in range(10)]


def insertletter(letter='', pos=0):
  board[pos] = letter


def printboard(board):
  print('  |  |  ')
  print("" + board[1] + "  | " + board[2] + " | " + board[3] + "  ")
  print('  |  |  ')
  print('_________')
  print('  |  |  ')
  print("" + board[4] + "  |  " + board[5] +"|" + board[6] + "  ")
  print('  |  |  ')
  print('_________')
  print('  |  |  ')
  print("" + board[7] + "  | " + board[8] + "| " + board[9] + "  ")
  print('  |  |  ')
  print('_________')


def isfreespace(pos):
  return board[pos] == ''


def isboardfull(board):
  if board.cound('') > 1:
    return False
  else:
    return True


def iswinner(b, l):
  return (b[1] == l and b[2] == l and b[3] == l
          or b[4] == l and b[5] == l and b[6] == l
          or b[7] == l and b[8] == l and b[9] == l
          or b[1] == l and b[4] == l and b[7] == l
          or b[2] == l and b[5] == l and b[8] == l
          or b[3] == l and b[6] == l and b[9] == l
          or b[1] == l and b[5] == l and b[9] == l
          or b[3] == l and b[5] == l and b[7] == l)


def playermove():
  run = True
  while run:
    move = input('enter the possition of from 1 to 9')
    try:
      move = int(move)
      if move > 0 and move < 10:
        if isfreespace(move):
          run = False
          insertletter('x', move)
          printboard(board)
        else:
          print('the possition is alredy exist')
      else:
        print('enter the number between 1 to 9')
    except:
      print('enter the number')


playermove()
