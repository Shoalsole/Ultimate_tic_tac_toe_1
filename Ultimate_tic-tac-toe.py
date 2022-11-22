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
  
  
print("Welcome to ultimate tic-tac-toe!" + "\n")

#print('-------------------------')
#print('| . . . | . . . | . . . |')
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

print(gameSeven[7] + '|' + gameSeven[8] + '|' + gameSeven[9])

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

          
          


print("Welcome to ULTIMATE Tic-Tac-Toe!")

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
  playerOneLetter,playerTwoLetter = inputPlayerLetter()
  turn = whoGoesFirst()
  print(turn + " will go first")
  gameIsPlaying = True         

#call the function that decides the first board here          

  while gameIsPlaying:
    if turn == "playerOne"
      #draw the board
      #get the move from the player
      #is the move in a full board
          #get new player move
      #make the player move
          #change the game you're playing in
      if localWin(game[nextGame],playerOneLetter): #This would be how you use the localWin function to check if one of the games has been won
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
      #change the turn variable
    else: 
      #draw the board     
      #get the player two move
      #is the move in a full board
        #get new player move
      #make the player two move
      #Change the game you're playing in 
      if localWin(game[nextGame],playerTwoLetter): #This would be how you use the localWin function to check if one of the games has been won
        gameState[nextGame-1] = playerTwoLetter
      else:
        pass
      if globalWin(gameState,playerTwoLetter): #this function will always be called with gameState
        print("player two has won! Congratulations!")
        break
      else:
        pass
       #change the turn variable
  
  playAgain = input("The game has ended. Would you like to play again?")
  if playAgain.upper().startswith("N"):
    break






















