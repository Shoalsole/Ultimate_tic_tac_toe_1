#This is the python file for Tic-tac-toe-ultimate. Note that the regular tic-tac-toe code is on Quinn's repo. 


# Notes from Tuesday...

#gameOne = [" "]*10
#gameTwo = [" "]*10
#gameThree = [" "]*10
#gameFour = [" "]*10
#gameFive = [" "]*10
#gameSix = [" "]*10
#gameSeven = [" "]*10
#gameEight = [" "]*10
#gameNine = [" "]*10

#games = [gameOne,gameTwo,gameThree,gameFour,gameFive,fiveSix,fiveSeven,gameEight,gameNine]
#gameState = games.copy()
  
  #startGame will be the choice of the game that we start in
  #we are doing two player
  # moveOne is the move by player one
  # moveTwo is the move by player two
  
  #playerOneLetter
  #playerTwoLetter
  
  #1. print the game
  #2. print the game we're curruently playing in (RAY)
  
  
  #3. swap between games/play in the proper game (XIUWEN)
  
  
  #4. local win conditions (QUINN)
  #5. global win conditions
  
  
  #7. Starting the game -while game is playing loop (JOHN)
  
  
  
  
  #nextGame[moveOne] = playerOneLetter
  #nextGame = (moveOne-1) 
  
  #nextGame = 5
  #moveOne from player 
  #play moveOne in nextGame - games[nextGame-1][moveOne] = playerOneLetter 
  #change game - nextGame
  
  #moveTwo from player2
  #play moveTwo in nextGame
  #change game - reassign nextGame
  
  #moveOne from player 1
  #play moveOne in nextGame
  #ghange game - reassign nextGame
  
  
  #isWinner(games[4],playerOneLetter)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Insert variable and import declearations 
  
import random
  
  
# print("Welcome to ultimate tic-tac-toe!" + "\n")

# print("The game is in 9 games of tic-tac toe. Of which, each tic-tac toe game is represented in one of the nine squares below. Within a tic-tac-toe game, the regular rules apply for tic-tac-toe.")

# print('\n' + 'The games in the top row correspond to the numbers 7, 8, 9 respectively, same goes for the middle row, where the games correspond to the numbers 4, 5, 6. Same goes for the bottom row.")
      
# print('\n" + "Within each instance of a tic-tac-toe game, the same rules of tic-tac-toe apply.")
      
# print("The 3 entries in the top row correspond to the number 7, 8, 9. 
      
# print("The 3 entries in the middle row correspond to the numbers 4, 5, 6, and same logic for the bottom 3 entries - very similar to the logic with each game as described above.") 

# print('-------------------------')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('-------------------------')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('-------------------------')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('| . . . | . . . | . . . |')
# print('-------------------------')
      
#I moved this stuff further down the code (QW)
      

def print_board(): #maybe prints the board if the condition of the game being started is true, elsewise do not print. 
      
  print('----------------------------')

  print('|' + gameSeven[7] + gameSeven[8] + gameSeven[9] + '|' + gameEight[7] + gameEight[8] + gameEight[9] + '|' + gameNine[7] + gameNine[8] + gameNine[9] + '|')
  print('|' + gameSeven[4] + gameSeven[5] + gameSeven[6] + '|' + gameEight[4] + gameEight[5] + gameEight[6] + '|' + gameNine[4] + gameNine[5] + gameNine[6] + '|')
  print('|' + gameSeven[1] + gameSeven[2] + gameSeven[3] + '|' + gameEight[1] + gameEight[2] + gameEight[3] + '|' + gameNine[1] + gameNine[2] + gameNine[3] + '|')

  print('----------------------------')

  print('|' + gameFour[7] + gameFour[8] + gameFour[9] + '|' + gameFive[7] + gameFive[8] + gameFive[9] + '|' + gameSix[7] + gameSix[8] + gameSix[9] + '|')
  print('|' + gameFour[4] + gameFour[5] + gameFour[6] + '|' + gameFive[4] + gameFive[5] + gameFive[6] + '|' + gameSix[4] + gameSix[5] + gameSix[6] + '|')
  print('|' + gameFour[1] + gameFour[2] + gameFour[3] + '|' + gameFive[1] + gameFive[2] + gameFive[3] + '|' + gameSix[1] + gameSix[2] + gameSix[3] + '|')

  print('----------------------------')

  print('|' + gameOne[7] + gameOne[8] + gameOne[9] + '|' + gameTwo[7] + gameTwo[8] + gameTwo[9] + '|' + gameThree[7] + gameThree[8] + gameThree[9] + '|')
  print('|' + gameOne[4] + gameOne[5] + gameOne[6] + '|' + gameTwo[4] + gameTwo[5] + gameTwo[6] + '|' + gameThree[4] + gameThree[5] + gameThree[6] + '|')
  print('|' + gameOne[1] + gameOne[2] + gameOne[3] + '|' + gameTwo[1] + gameTwo[2] + gameTwo[3] + '|' + gameThree[1] + gameThree[2] + gameThree[3] + '|')

  print('----------------------------')

      
#Prints visual representation of global board...

#Top row: 7, 8, 9
#Middle row: 4, 5, 6
#Bottom 3 rows: 1 2 3

def chose_player_letter():
  
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print("Do you want to play as 'X' or 'O'?"
    letter = input().upper()
      
          
  if letter == 'X':
          return['X', 'O']      
  else:
    return ['O', 'X']
          
def who_go_first():       
  if random.randint(0,1) == 0: 
    return 'player1'              #placeholder for player1's move  

  else:
    return 'player2'              #placeholder for player2's move  
          
#need a function where we prompt the player1 or player2 (whoever goes first) on which gam (out of 9) they want to play in. 
          #and prompts them to make a move
          
def choose_board():
		selection=' '
		while selection not in '1 2 3 4 5 6 7 8 9'.split() or not isBoardFree(board,int(selection)):
			print("Which board do you want to go to?")
			selection = input()
		return int(selection)
       
#--------------------------------------------------------------------
#Quinn's section, checking for local and global win conditions

def localWin(game,player): #game is in reference to which game is being checked, meaning it will be one of the game lists. Player is the player letter
  return ((game[7] == player and game[8] == player and game[9] == player) or 
  (game[4] == player and game[5] == player and game[6] == player) or 
  (game[1] == player and game[2] == player and game[3] == player) or 
  (game[7] == player and game[4] == player and game[1] == player) or 
  (game[8] == player and game[5] == player and game[2] == player) or 
  (game[9] == player and game[6] == player and game[3] == player) or 
  (game[7] == player and game[5] == player and game[3] == player) or 
  (game[9] == player and game[5] == player and game[1] == player)) 
      #When it gets called, it should look something like this:
      #localWin(games[nextGame],playerOneLetter)
      #Since nextGame is being called, this function must be run BEFORE you reassign nextGame (meaning it should be run while nextGame is talking about the right game)

def globalWin(gameState,player):
  return ((gameState[6] == player and gameState[7] == player and gameState[8] == player) or 
  (gameState[3] == player and gameState[4] == player and gameState[5] == player) or 
  (gameState[0] == player and gameState[1] == player and gameState[2] == player) or 
  (gameState[6] == player and gameState[3] == player and gameState[0] == player) or 
  (gameState[7] == player and gameState[4] == player and gameState[1] == player) or 
  (gameState[8] == player and gameState[5] == player and gameState[2] == player) or 
  (gameState[6] == player and gameState[4] == player and gameState[2] == player) or 
  (gameState[8] == player and gameState[4] == player and gameState[0] == player))  #These numbers don't match how the original guy does his game checks. Thats because each game is a list of ten entries, whereas the overal games list has only 9 entries. To correct for this, 1 is taken away from each number      

def getPlayerMove(board):
# Let the player enter their move.
	move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)): 
          print('What is your next move? (1-9)')
          move = input() #The integer assigned to move is where the player is making their move (QW)
        return int(move)

def makeMove(games, letter, move): 
	games[nextGame-1][move] = letter #Recall: board is the section of the tictactoe board. Here, that section is being assigned to the move (QW)	  
	  
print("Welcome to ultimate tic-tac-toe!" + "\n")

print("The game is in 9 games of tic-tac toe. Of which, each tic-tac toe game is represented in one of the nine squares below. Within a tic-tac-toe game, the regular rules apply for tic-tac-toe.")

print('\n' + 'The games in the top row correspond to the numbers 7, 8, 9 respectively, same goes for the middle row, where the games correspond to the numbers 4, 5, 6. Same goes for the bottom row.")
      
print('\n" + "Within each instance of a tic-tac-toe game, the same rules of tic-tac-toe apply.")
      
print("The 3 entries in the top row correspond to the number 7, 8, 9. 
      
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
  gameOne = [" "]*10
  gameTwo = [" "]*10
  gameThree = [" "]*10
  gameFour = [" "]*10
  gameFive = [" "]*10
  gameSix = [" "]*10
  gameSeven = [" "]*10
  gameEight = [" "]*10
  gameNine = [" "]*10

  games = [gameOne,gameTwo,gameThree,gameFour,gameFive,fiveSix,fiveSeven,gameEight,gameNine]
  gameState = [" "]*9
  playerOneLetter,playerTwoLetter = chose_player_letter()
  print("Player one is",playerOneLetter,"and player two is",playerTwoLetter,sep=" ")    
  turn = who_go_first()
  print(turn + " will go first")
  nextGame = choose_board()
  gameIsPlaying = True  
  
      

#call the function that decides the first board here          

  while gameIsPlaying:
    if turn == "playerOne"
      print_board()
      #check if nextGame is in a full board
      	#if yes, player can pick whaever
      move = getPlayerMove(games[nextGame-1])
      makeMove(games,playerOneLetter,move)
          nextGame = move
      if localWin(game[nextGame],playerOneLetter): 
        gameState[nextGame-1] = playerOneLetter
      else:
        pass  
          
      if globalWin(gameState,playerOneLetter): #this function will always be called with gameState
        print("player one has won! Congratulations!")
        break
      else:
        pass
  #continue playing the game
          #stop the game
      turn = "playerTwo"
    else: 
      print_board()     
      #check if nextGame is in a full board
      	#if yes, player can pick whaever
      move = getPlayerMove(games[nextGame-1])
      makeMove(games,playerTwoLetter,move)
          nextGame = move
      if localWin(game[nextGame],playerTwoLetter): #This would be how you use the localWin function to check if one of the games has been won
        gameState[nextGame-1] = playerTwoLetter
      else:
        pass
      if globalWin(gameState,playerTwoLetter): #this function will always be called with gameState
        print("player two has won! Congratulations!")
        break
      else:
        pass
       turn = "playerOne"
  
  playAgain = input("The game has ended. Would you like to play again?")
  if playAgain.upper().startswith("N"):
    break






















