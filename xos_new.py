import time
import random
board=[i+1 for i in range(9)]
np=1

def print_board():
    print()
    for i in range(1,10,3):
            print ("| {} | {} | {} |".format(board[i-1],board[i],board[i+1]))
    print()

def player_init():
    np1=input("Choose from below:\n 1. vs Player\n 2. vs Computer\nEnter your option:")
    if ((np1 != "1") and (np1 != "2")):
        print("Please enter 1 or 2 only. Try again!")
        player_init()
    np1=int(np1)
    return np1

def player_move(sym):   
    #print ("np value is: {}".format(np))
    if np == 1 :
        if sym == "X":
            num="Player 1"
        elif sym == "O":
            num="Player 2"
        print("{}'s turn:".format(num))
        loc=int(input("Please enter the location [1-9]:"))
        if ( (loc - 1) in range (9)):
            if ( (str(board[loc-1]).strip() != "X") and (str(board[loc-1]).strip() != "O") ):
                board[loc-1]=sym
            else:
                print ("Location already used, please choose any vacant location")
                player_move(sym)
        else:
            print ("The location value entered is not in the range mentioned. Please enter a valid number from [1-9]")
            player_move(sym)
    elif np == 2 :
        if sym == "X":
            num="Player 1"
        elif sym == "O":
            num="Computer"
        print("{}'s turn".format(num))
        if sym == "X":
            loc=int(input("Please enter the location [1-9]:"))
            if ( (loc - 1) in range (9)):
                if ( (str(board[loc-1]).strip() != "X") and (str(board[loc-1]).strip() != "O") ):
                    board[loc-1]=sym
                else:
                    print ("Location already used, please choose any vacant location")
                    player_move(sym)
            else:
                print ("The location value entered is not in the range mentioned. Please enter a valid number from [1-9]")
                player_move(sym)
        elif sym == "O":
            while True:
                loc=random.randint(1,9)
                if ( (str(board[loc-1]).strip() != "X") and (str(board[loc-1]).strip() != "O") ):
                    break
            board[loc-1]=sym   

def vic(sym):
    if (str(board[0])==sym and str(board[1])==sym and str(board[2])== sym) or \
       (str(board[3])==sym and str(board[4])==sym and str(board[5])== sym) or \
       (str(board[6])==sym and str(board[7])==sym and str(board[8])== sym) or \
       (str(board[0])==sym and str(board[3])==sym and str(board[6])== sym) or \
       (str(board[1])==sym and str(board[4])==sym and str(board[7])== sym) or \
       (str(board[2])==sym and str(board[5])==sym and str(board[8])== sym) or \
       (str(board[0])==sym and str(board[4])==sym and str(board[8])== sym) or \
       (str(board[2])==sym and str(board[4])==sym and str(board[6])== sym):
        return True                                               
    else:
        return False

def tie():
    count=0
    for i in range(9):
       # print(i)
        if (board[i-1] == "X" or board[i-1] == "O"):
            count+=1
        else:
            break
    #print(count)
    if( count == 9 ):
        return True
    else:
        return False
            
print ("Welcome to X and Os Game")
np=player_init()
if np == 1:
    print ("Player 1 to play with X and Player 2 to play with O. Please check the board below")
else:
    print ("Player 1 to play with X and Computer to play with O. Please check the board below")
print_board()
while True:
    player_move("X")
    if vic("X"):
        print ("Player 1 wins!")
        print_board()
        time.sleep(5)
        break
    elif tie():
        print("Match is a tie")
        print_board()
        time.sleep(5)
        break
    print_board()
    player_move("O")
    if vic("O"):
        if (np == 1 ):
            print ("Player 2 wins!")
        elif (np == 2):
            print ("Computer wins!")
        print_board()
        time.sleep(5)
        break
    elif tie():
        print("Match is a tie")
        time.sleep(5)
        print_board()
        break
    print_board()
