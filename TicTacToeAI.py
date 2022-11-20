board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1]+ '|' + board[2]+ '|' + board[3])
    print('-+-+-')
    print(board[4]+ '|' + board[5]+ '|' + board[6])
    print('-+-+-')
    print(board[7]+ '|' + board[8]+ '|' + board[9])
    print('-+-+-')
    print('\n')
    
def spaceIsFree(position):
   return True if board[position]==' ' else False

def checkDraw():
   for key in board.keys():
        if board[key]==' ':
           return False
   return True

def checkWin():
    if(board[1]==board[2] and board[1]==board[3] and board[1]!= ' '):
       return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4]!= ' '):
       return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7]!= ' '):
       return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1]!= ' '):
       return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2]!= ' '):
       return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3]!= ' '):
       return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1]!= ' '):
       return True
    elif(board[3]==board[5] and board[3]==board[7] and board[3]!= ' '):
       return True
    else:
       return False
    
def checkWhichMarkWon(mark):
    if(board[1]==board[2] and board[1]==board[3] and board[1] == mark):
       return True
    elif(board[4]==board[5] and board[4]==board[6] and board[4] == mark):
       return True
    elif(board[7]==board[8] and board[7]==board[9] and board[7] == mark):
       return True
    elif(board[1]==board[4] and board[1]==board[7] and board[1] == mark):
       return True
    elif(board[2]==board[5] and board[2]==board[8] and board[2] == mark):
       return True
    elif(board[3]==board[6] and board[3]==board[9] and board[3] == mark):
       return True
    elif(board[1]==board[5] and board[1]==board[9] and board[1] == mark):
       return True
    elif(board[3]==board[5] and board[3]==board[7] and board[3] == mark):
       return True
    else:
       return False
        
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position]=letter
        printBoard(board)
        
        if checkDraw():
            print('Draw!')
            exit()    
                 
        if checkWin():
           if letter=='x':
               print('Bot Wins')
               exit()
           else:
               print('Player Wins')
               exit()
        return
        
    else:
        print('space is filled')
        position= int(input('Enter a new position'))
        insertLetter(letter,position)
        return 
       
player = 'o'
bot='x'

def playerMove():
    position = int(input('Enter the position for "o" '))
    insertLetter(player, position)
    return

def computerMove():
   bestScore= -1000
   bestMove= 0
   
   for key in board.keys():
      if board[key]==' ':
         board[key]=bot
         score= minimax(board, 0, False)
         board[key]= ' '
         if(score> bestScore):
            bestScore = score
            bestMove = key 
   insertLetter(bot, bestMove)
   return


def minimax(board, depth , isMaximizing):
   
   if checkWhichMarkWon(bot):
      return 100
   elif checkWhichMarkWon(player):
      return -100
   elif checkDraw():
      return 0
   
   if isMaximizing:
      bestScore = -1000
      
      for key in board.keys():
         if board[key]==' ':
            board[key]=bot
            score= minimax(board, 0 , False)
            board[key]= ' '
            if(score> bestScore):
               bestScore = score
      return bestScore
     
   else:
      bestScore=800
      for key in board.keys():
         if board[key]==' ':
            board[key]=player
            score= minimax(board, 0, True)
            board[key]= ' '
            if(score < bestScore):
               bestScore = score
      return bestScore

           
 
while not checkWin():
   computerMove()
   playerMove()
   
