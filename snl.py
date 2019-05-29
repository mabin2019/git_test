import random;
import time;
board=[ str((100-i)) for i in range(100)]
play_posn=[]
players=[]
for i in range(100):
    if int(board[i]) < 10:
        board[i]=board[i]+" "
    if int(board[i]) < 100:
        board[i]=" "+board[i]
def print_board():
    print()
    for i in range(1,100,10):
        if (((i+9) % 20) != 0):
            print ("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(board[i-1],board[i],board[i+1],board[i+2],board[i+3],board[i+4],board[i+5],board[i+6],board[i+7],board[i+8]))                  
        else:
            print ("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(board[i+8],board[i+7],board[i+6],board[i+5],board[i+4],board[i+3],board[i+2],board[i+1],board[i],board[i-1]))

    print()

snake_loc=[13,29,43,67,78,81,94,98]
snake_end_loc=[6,4,11,42,26,64,86,80]
ladder_loc=[9,20,34,46,58,70,83]
ladder_end_loc=[36,65,48,73,77,88,96]
np=1

def game_mode():
    np=input("Please choose from below:\n 1. vs Player(s)\n 2. vs Computer\nEnter your choice: ")
    if ((np != "1") and (np != "2")):
        print("Please choose either 1 or 2. Try again!")
        game_mode()
    np=int(np)
    return np

def player_input():
    i=1
    if (mode == 1):
        num_play=input("Enter the number of players: ")
        if ( int(num_play) < 2 ):
            print ("Number of players should be more than 1!")
            player_input()
        else:
            while ( i <= int(num_play) ):
                players.append(str(i))
                i+=1
            print ("Game starting with {} players".format(num_play))
    elif (mode == 2):
        while ( i <= 2 ):
            players.append(str(i))
            i=i+1
        print ("Game starting single player mode")
        
 
def player_init():
    for j in players:
        play_posn.append(int(0))

def player_move(n):
    n=int(n)
    if ( (mode == 1) or ((mode == 2) and (n != 2)) ):
        print ("Player {}'s turn - Currently at {}".format(n,play_posn[n-1]))
        option=input ("Press enter to continue the game!. \"q/Q\" to Quit: ")
        if (option.lower() == "q"):
            quit()
    elif ((mode == 2) and (n == 2)):
        print ("Computer's turn - Currently at {}".format(play_posn[1]))
    dice=int(random.randint(1,6))
    if (play_posn[n-1] == 0):
        if dice == 6:
            print("You got a 6. Starting the game!")
            play_posn[n-1]=play_posn[n-1]+dice
        else:
            play_posn[n-1]=0
            print("You got a {}. Game would only start once rolled on to 6!".format(dice))
    else:       
        #print (play_posn[n-1]+dice,n,dice,play_posn[n-1])
        if ((play_posn[n-1]+dice) <= 100):
            play_posn[n-1]=play_posn[n-1]+dice
            print ("You got a {} and reached {}".format(dice,play_posn[n-1]))
        else:
            play_posn[n-1]=play_posn[n-1]
            print ("You got a {} but position would remain at {}" .format(dice,play_posn[n-1]))
        if play_posn[n-1] in snake_loc:
            print("Ohh! U got into a snake at {} number".format(play_posn[n-1]))
            loc=snake_loc.index(play_posn[n-1])
            play_posn[n-1]=snake_end_loc[loc]
            print("Player currently in {}".format(play_posn[n-1]))
        elif play_posn[n-1] in ladder_loc:
            print("Yaayyy! U got a ladder at {} number".format(play_posn[n-1]))
            loc=ladder_loc.index(play_posn[n-1])
            play_posn[n-1]=ladder_end_loc[loc]
            print("Player currently in {}".format(play_posn[n-1]))
mode=game_mode()

player_input()
print_board()
player_init()
c=0
while c != 1:
    for turn in players:
        #print("{}p's turn:".format(turn))
        print()
        player_move(turn)
        print()
        if (int(100) in play_posn):
            c=1;
            break;
winner=play_posn.index(100)
if (mode ==1):
    print("Player {} has won".format(players[winner]))
else:
    if (winner == 0 ):
        print("Congratulations Player 1. You have won")
    elif (winner == 1):
        print("Computer won. Better luck next time")
time.sleep(5)
