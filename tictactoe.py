import random
      print("Enter an integer")


def computermove():
  possibleMove = [
    x for x, letter in enumerate(board) if letter == ' ' and x != 0
  ]
  move = 0
  def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

  for let in ['0', 'x']:
    for i in possibleMove:
      boardcopy = board[:]
      boardcopy[i] = let
      if isWinner(boardcopy, let):
        move = i
        return move
  cornerMove = []
  for i in possibleMove:
    if i in [1, 3, 7, 9]:
      cornerMove.append(i)
  if len(cornerMove) > 0:
    move = selectRandom(cornerMove)
    return move
  if 5 in possibleMove:
    move = 5
    return move

  edgeOpen = []

  for i in possibleMove:
    if i in [2, 4, 6, 8]:
      edgeOpen.append(i)

  if len(edgeOpen) > 0:
    move = selectRandom(edgeOpen)
    return move
def main():
  print('welcome to the game')
  printBoard(board)
  while not(isBoardFull(board)):
    if not(isWinner(board,'0')):
      playerMove()
      printBoard(board)
    else:
      print('you loose')
      break
    if not(isWinner(board,'x')):
      move = computermove()
      if move == 0:
        print(' ')
      else:
        insertLetter('0',move)
        print('computer is placed at o possition',move,":")
        printBoard(board)
    else:
        print('winner')
  if isBoardFull(board):
    print('tie game')
while True:
  x = input ('do you want play again y/n')
  if x.lower() =='y':
    board = [' ' for i in range(10)]
    print('__________________________')
    main()
  else:
    break