#Authors:
#John Huynh (JH), Quinn Wesener (QW), Ray Wang (RW), Xin Wen Du (XD)

import random


def globalIsFull(board): #function checks if the overall board(global) is full (JH)
    for i in range(0,9):
        if board[i] == " ":
            return False
    return True
def localIsFull(board): #function checks the nine individual boards(local) is full (JH)
    for i in range(0,9):
        if isSpaceFree(board,i):
            return False
    return True

def gameIsDone(gameState,nextGame): #function checks whether the game is done (JH)
  if gameState[nextGame-1] != " ":
    return True
  else:
    return False

#-----------------------------Ray's section starts here below.

def print_board(): # maybe prints the board if the condition of the game being started is true, elsewise do not print. (RW)
                   # prints the entire board, including all nine local tic-tac-toe games and all nine spots within a local tic-tac-toe game. (RW)

  print('-------------')                    

  print('|' + gameSeven[7] + gameSeven[8] + gameSeven[9] + '|' + gameEight[7] + gameEight[8] + gameEight[9] + '|' + gameNine[7] + gameNine[8] + gameNine[9] + '| \t')
  print('|' + gameSeven[4] + gameSeven[5] + gameSeven[6] + '|' + gameEight[4] + gameEight[5] + gameEight[6] + '|' + gameNine[4] + gameNine[5] + gameNine[6] + '| \t')
  print('|' + gameSeven[1] + gameSeven[2] + gameSeven[3] + '|' + gameEight[1] + gameEight[2] + gameEight[3] + '|' + gameNine[1] + gameNine[2] + gameNine[3] + '| \t')

  print('-------------    State of overall games')             

  print('|' + gameFour[7] + gameFour[8] + gameFour[9] + '|' + gameFive[7] + gameFive[8] + gameFive[9] + '|' + gameSix[7] + gameSix[8] + gameSix[9] + '| \t' + gameState[6] +' | '+ gameState[7] +' | '+ gameState[8])
  print('|' + gameFour[4] + gameFour[5] + gameFour[6] + '|' + gameFive[4] + gameFive[5] + gameFive[6] + '|' + gameSix[4] + gameSix[5] + gameSix[6] + '| \t' + gameState[3] +' | '+ gameState[4] +' | '+ gameState[5])
  print('|' + gameFour[1] + gameFour[2] + gameFour[3] + '|' + gameFive[1] + gameFive[2] + gameFive[3] + '|' + gameSix[1] + gameSix[2] + gameSix[3] + '| \t' + gameState[0] +' | '+ gameState[1] +' | '+ gameState[2])

  print('-------------')                    

  print('|' + gameOne[7] + gameOne[8] + gameOne[9] + '|' + gameTwo[7] + gameTwo[8] + gameTwo[9] + '|' + gameThree[7] + gameThree[8] + gameThree[9] + '| \t')
  print('|' + gameOne[4] + gameOne[5] + gameOne[6] + '|' + gameTwo[4] + gameTwo[5] + gameTwo[6] + '|' + gameThree[4] + gameThree[5] + gameThree[6] + '| \t')
  print('|' + gameOne[1] + gameOne[2] + gameOne[3] + '|' + gameTwo[1] + gameTwo[2] + gameTwo[3] + '|' + gameThree[1] + gameThree[2] + gameThree[3] + '| \t')


#Prints visual representation of global board... (RW)

#Top row: 7, 8, 9
#Middle row: 4, 5, 6
#Bottom 3 rows: 1 2 3

def chose_player_letter():              #this function prompts the players on whether they want to be  "X" or "O"? (RW)                

  letter = ''                                          
  while not (letter == 'X' or letter == 'O'):           
    print("Do you want to play as 'X' or 'O'?")        
    letter = input().upper()                            


  if letter == 'X':
          return['X', 'O']
  else:
    return ['O', 'X']

def who_go_first():                    #this function will randomly determine whether player 1 or player 2 will go first. (RW)
    
  if random.randint(0,1) == 0:         #this is why imported random, this randomly determines which player will go first. (RW)
    return '1'                         #for player 1, they can move first. (RW)

  else:
    return '2'                         #for player 2, they can move first. (RW)

#need a function where we prompt the player1 or player2 (whoever goes first) on which gam (out of 9) they want to play in.
#and prompts them to make a move
    
#-----------------------------Ray's section ends here^^^^^.
#-----------------------------John's section starts here.

def choose_board(number): #function that ask what board the current player wants to go to (JH)
    print("Which board does player", number ,"want to go to?")
    selection = input()
    while selection not in '1 2 3 4 5 6 7 8 9'.split() or not isGameStateFree(gameState,int(selection)):
      print("Which board does player", number ,"want to go to?")
      selection = input()
    return int(selection)

def isSpaceFree(board, move):
      # Return True if the passed move is free on the passed board.
      return board[move] == '.'

def isGameStateFree(board,move):        
        return board[move-1] == ' '
    
#-------------------John's section ends here.
#-------------------Xiu Wen's section starts here.
    
def localWin(game,player): #game is in reference to which game is being checked, meaning it will be one of the game lists. Player is the player letter
  return ((game[7] == player and game[8] == player and game[9] == player) or    #Checks Local win conditions for all 3x3 patterns (XD)
  (game[4] == player and game[5] == player and game[6] == player) or
  (game[1] == player and game[2] == player and game[3] == player) or
  (game[7] == player and game[4] == player and game[1] == player) or
  (game[8] == player and game[5] == player and game[2] == player) or
  (game[9] == player and game[6] == player and game[3] == player) or
  (game[7] == player and game[5] == player and game[3] == player) or
  (game[9] == player and game[5] == player and game[1] == player))

def globalWin(gameState,player):
  return ((gameState[6] == player and gameState[7] == player and gameState[8] == player) or #Checks for Global win conditions for all 3x3 local win patterns (XD)
  (gameState[3] == player and gameState[4] == player and gameState[5] == player) or
  (gameState[0] == player and gameState[1] == player and gameState[2] == player) or
  (gameState[6] == player and gameState[3] == player and gameState[0] == player) or
  (gameState[7] == player and gameState[4] == player and gameState[1] == player) or
  (gameState[8] == player and gameState[5] == player and gameState[2] == player) or
  (gameState[6] == player and gameState[4] == player and gameState[2] == player) or
  (gameState[8] == player and gameState[4] == player and gameState[0] == player))  #These numbers don't match how the original guy does his game checks. Thats because each game is a list of ten entries, whereas the overal games list has only 9 entries. To correct for this, 1 is taken away from each number

def globalTie(board):
    for i in range(0,9):
      if board[i] == " ": # If variable "i" from 1 to 9 are all filled then return False. (XD)
        return False
    return True # returns True else wise. (XD)

#----------------------------------------Xiu Wen's section ends here.
#----------------------------------------Quinn's section starts below.

def getPlayerMove(board):
# Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your move?')
        move = input() #The integer assigned to move is where the player is making their move (QW)
    return int(move)

def makeMove(games, letter, move):
    games[nextGame-1][move] = letter #Recall: board is the section of the tictactoe board. Here, that section is being assigned to the move (QW)

print("Welcome to ultimate tic-tac-toe!" + "\n")

print("The game is in 9 games of tic-tac toe. Of which, each tic-tac toe game is represented in one of the nine squares below. Within a tic-tac-toe game, the regular rules apply for tic-tac-toe.")

print('The games in the top row correspond to the numbers 7, 8, 9 respectively, same goes for the middle row, where the games correspond to the numbers 4, 5, 6. Same goes for the bottom row.')

print("Within each instance of a tic-tac-toe game, the same rules of tic-tac-toe apply.")

print("The 3 entries in the top row correspond to the number 7, 8, 9.")

print("The 3 entries in the middle row correspond to the numbers 4, 5, 6, and same logic for the bottom 3 entries - very similar to the logic with each game as described above.")

print('-------------------------')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('-------------------------')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('-------------------------')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('| . . . | . . . | . . . |')
print('-------------------------')


while True:
  gameOne = ["."]*10 #Make the list of each local game (QW)
  gameTwo = ["."]*10
  gameThree = ["."]*10
  gameFour = ["."]*10
  gameFive = ["."]*10
  gameSix = ["."]*10
  gameSeven = ["."]*10
  gameEight = ["."]*10
  gameNine = ["."]*10

  games = [gameOne,gameTwo,gameThree,gameFour,gameFive,gameSix,gameSeven,gameEight,gameNine] #Make the master list that holds each local game, so that they are easily accessible (QW)
  gameState = [" "]*9
  playerOneLetter,playerTwoLetter = chose_player_letter() #Pick the player letters. The following line just prints them (QW)
  print("Player one is",playerOneLetter,"and player two is",playerTwoLetter,"\n",sep=" ")
  turn = who_go_first() #Pick who goes first (QW)
  print("Player "+turn + " will go first \n")
  nextGame = 0 #This is here so that the next line doesn't break the code, as choose_board uses the variable nextGame so it must be defined (QW)
  nextGame = choose_board(turn)
  gameIsPlaying = True #Start the game!

  while gameIsPlaying:
    if turn == "1": #Player ones turn (QW)
      print_board() #Print the board (QW)
      if gameIsDone(gameState,nextGame): #Check if the board the player is expected to play in is inacessible (its a tie/its been won). For more information about this mechanic, see the rules pdf (QW)
        nextGame = choose_board("1") #They get to pick their board, if the previous statement was true (QW)
      print("player one is playing in board",nextGame)
      move = getPlayerMove(games[nextGame-1]) #Get the player move for the proper board (QW)
      makeMove(games,playerOneLetter,move) #Make the move on the proper board (QW)

      if localWin(games[nextGame-1],playerOneLetter): #Has the player won the local game they've played in? (QW)
        gameState[nextGame-1] = playerOneLetter
      if globalWin(gameState,playerOneLetter): #Has the player won the global game? (QW) 
        print("player one has won! Congratulations!")
        break
      if globalIsFull(gameState): #Is the global game a tie? (QW)
        print("The game is a tie!")
        break
      if localIsFull(games[nextGame-1]): #Is the local game a tie? (QW)
        gameState[nextGame-1] = "tie"
      nextGame = move #Reassign nextGame to the board that player two is expected to play on (QW)
      turn = "2"
    else: #The same process follows, except its for player two (QW)
      print_board()
      if gameIsDone(gameState,nextGame):
        nextGame = choose_board("2")
      print("player two is playing in board",nextGame)
      move = getPlayerMove(games[nextGame-1])
      makeMove(games,playerTwoLetter,move)

      if localWin(games[nextGame-1],playerTwoLetter): #This would be how you use the localWin function to check if one of the games has been won (QW)
        gameState[nextGame-1] = playerTwoLetter
      if globalWin(gameState,playerTwoLetter): #this function will always be called with gameState (QW)
        print("player two has won! Congratulations!")
        break
      if globalIsFull(gameState):
        print("The game is a tie!")
        break
      if localIsFull(games[nextGame-1]):
        gameState[nextGame-1] = "tie"
      nextGame = move
      turn = "1"

  playAgain = input("The game has ended. Would you like to play again?") #Once the gameIsPlaying loop is broken, they will be prompted on whether or not they'd like to continue (QW)
  if playAgain.upper().startswith("N"): #If they say no, stop the game (QW)
    break
    
 
