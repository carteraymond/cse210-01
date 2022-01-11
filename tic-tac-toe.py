#Welcome to Tic-Tac-Toe, a simple game in which two players
#take turns marking up a 3x3 grid with "X" or "O". The winner is the player
#who succesfully creates a row with their symbol. the game ends in a draw when all
#nine spaces have been filled without a matching row of symbols.
#This code was made by Carter Raymond for CSE210

import os

Symbol_Input_List=[1,2,3,4,5,6,7,8,9]
def main():
    print("Hello and welcome to Tic-Tac-Toe, \n Lets Get Started!")
    while True:
        clear()
        create_board(Symbol_Input_List)
        player_one_move(Symbol_Input_List)
        if check_for_winner(Symbol_Input_List) or is_draw(Symbol_Input_List):
            clear()
            create_board(Symbol_Input_List)
            break
        clear()
        create_board(Symbol_Input_List)
        player_two_move(Symbol_Input_List)
        if check_for_winner(Symbol_Input_List) or is_draw(Symbol_Input_List):
            clear()
            create_board(Symbol_Input_List)
            break
    if check_for_winner(Symbol_Input_List):
        print("Congrats on winning")
    elif is_draw:
        print("No winner this time")
    else:
        print("Game undecided")
        
        

    





def clear():
    os.system("cls")


def create_board(Symbol_Input_List):
    SIL=Symbol_Input_List
    a=SIL[0]
    b=SIL[1]
    c=SIL[2]
    d=SIL[3]
    e=SIL[4]
    f=SIL[5]
    g=SIL[6]
    h=SIL[7]
    i=SIL[8]
    
    print(f"{a} | {b} | {c}")
    print("--+---+--")
    print(f"{d} | {e} | {f}")
    print("--+---+--")
    print(f"{g} | {h} | {i}")


def player_one_move(Symbol_Input_List):
    i=0
    while i==0:
        try:
            player1_symbol=int(input("\nPlayer ONE, where do you want to place an X? (enter 1-9): "))
            if Symbol_Input_List[player1_symbol-1]=="O":
                print("Player TWO has already chosen this space, try again")
                continue
            if Symbol_Input_List[player1_symbol-1]=="X":
                print("You have already chosen this space, try again")
                continue
            if player1_symbol<=0:
                print("That does not match a number, try again")
                continue
        except IndexError:
            print("That does not match a number, try again")
            continue
        except ValueError:
            print("That does not match a number, try again")
            continue
        except TypeError:
            print("That does not match a number, try again")
            continue
        i+=1
    Symbol_Input_List[player1_symbol-1]="X"
    
    
def player_two_move(Symbol_Input_List):
    i=0
    while i==0:
        try:
            player2_symbol=int(input("\nPlayer TWO, where do you want to place an O? (enter 1-9): "))
            if Symbol_Input_List[player2_symbol-1]=="X":
                print("Player ONE has already chosen this space, try again")
                continue
            if Symbol_Input_List[player2_symbol-1]=="O":
                print("You already chosen this space, try again")
                continue
            if player2_symbol<=0:
                print("That does not match a number, try again")
                continue
        except IndexError:
            print("That does not match a number, try again")
            continue
        except ValueError:
            print("That does not match a number, try again")
            continue
        except TypeError:
            print("That does not match a number, try again")
            continue
        i+=1
    Symbol_Input_List[int(player2_symbol-1)]="O"

def check_for_winner(Symbol_Input_List):
    SIL=Symbol_Input_List
    a=SIL[0]
    b=SIL[1]
    c=SIL[2]
    d=SIL[3]
    e=SIL[4]
    f=SIL[5]
    g=SIL[6]
    h=SIL[7]
    i=SIL[8]
    return(a == b == c or
            d == e == f or
            g == h == i or
            a == d == g or
            b == e == h or
            c == f == i or
            a == e == i or
            c == e == g)
    
    
def is_draw(Symbol_Input_List):
    SIL=Symbol_Input_List
    a=SIL[0]
    b=SIL[1]
    c=SIL[2]
    d=SIL[3]
    e=SIL[4]
    f=SIL[5]
    g=SIL[6]
    h=SIL[7]
    i=SIL[8]
    return(a!=1 and b!=2 and c!=3 and d!=4 and e!=5 and f!=6 and g!=7 and h!=8 and i!=9)
        
    
    
    
if __name__ == "__main__":
    main()