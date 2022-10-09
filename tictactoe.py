board  =[' ' for i in range(10)]

def insertletter(letter,poss):
    board[pos]= letter

def printboard(board):
    print('  |  |  ')
    print("" +board[1]+"  | "+board[2]+" | "+board[3]+"  ")
    print('  |  |  ')
    print('_________')
    print('  |  |  ')
    print("" +board[4]+"  | "+board[5]+" | "+board[6]+"  ")
    print('  |  |  ')
    print('_________')
    print('  |  |  ')
    print("" +board[7]+"  | "+board[8]+" | "+board[9]+"  ")
    print('  |  |  ')
    print('_________')

def isfreespace(pos):
    return boardpos == ""
def isboardfull(board):
    if board.cound('') >1:
       return False
    else:
        return True
def iswinner(b,l):
    return(b[1]==l and b[2]==l and b[3]==l or
            b[4]==l and b[5]==l and b[6]==l or
            b[7]==l and b[8]==l and b[9]==l or
            b[1]==l and b[4]==l and b[7]==l or
            b[2]==l and b[5]==l and b[8]==l or
            b[3]==l and b[6]==l and b[9]==l or
            b[1]==l and b[5]==l and b[9]==l or
            b[3]==l and b[5]==l and b[7]==l 
            )
print(iswinner(board," "))            