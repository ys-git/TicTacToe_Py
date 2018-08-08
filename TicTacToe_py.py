#Tic Tac Toe using python

import random


ls=[1, 2, 3, 4, 5, 6, 7, 8, 9]
res=0
a='A'
b='A'
#cont=True
again=True
p1=input("Enter the name of Player 1:")
p2=input("Enter the name of Player 1:")


def printboard():
    print(f"{ls[0]}  |  {ls[1]} |  {ls[2]} \n------------\n"
          f"{ls[3]}  |  {ls[4]} |  {ls[5]} \n------------\n"
          f"{ls[6]}  |  {ls[7]} |  {ls[8]} ")

def chk():
    cont=False
    for num in ls:
        if type(num)==int:
            cont=True
    if cont == False:
            print("Game Over!!")

    return cont

def play():
    t = 'X'
    while chk() == True:
        holder = input(f"Enter the position to place {t}")
        holder=int(holder-1)
        ls[holder] = t
        if t == 'X':
            t = 'O'
        elif t == 'O':
            t = 'X'
        printboard()

def winchk():
    win='None'

    if ls[0]==ls[1]==ls[2]=='X':
        win='X'
    elif ls[0]==ls[1]==ls[2]=='O':
        win = 'O'

    if ls[3]==ls[4]==ls[5]=='X':
        win='X'
    elif ls[3]==ls[4]==ls[5]=='O':
        win = 'O'

    if ls[6]==ls[7]==ls[8]=='X':
        win='X'
    elif ls[6]==ls[7]==ls[8]=='O':
        win = 'O'

    if ls[0]==ls[3]==ls[6]=='X':
        win='X'
    elif ls[0]==ls[3]==ls[6]=='O':
        win = 'O'

    if ls[1]==ls[4]==ls[7]=='X':
        win='X'
    elif ls[1]==ls[4]==ls[7]=='O':
        win = 'O'

    if ls[2]==ls[5]==ls[8]=='X':
        win='X'
    elif ls[0]==ls[1]==ls[2]=='O':
        win = 'O'

    if ls[0]==ls[4]==ls[6]=='X':
        win='X'
    elif ls[0]==ls[4]==ls[6]=='O':
        win = 'O'

    if ls[2]==ls[4]==ls[8]=='X':
        win='X'
    elif ls[2]==ls[4]==ls[8]=='O':
        win = 'O'

    if ls[0]==ls[4]==ls[2]=='X':
        win='X'
    elif ls[0]==ls[4]==ls[2]=='O':
        win = 'O'

    if ls[6]==ls[4]==ls[8]=='X':
        win='X'
    elif ls[6]==ls[4]==ls[8]=='O':
        win = 'O'

    if ls[0]==ls[4]==ls[8]=='X':
        win='X'
    elif ls[0]==ls[4]==ls[8]=='O':
        win = 'O'

    if ls[6]==ls[4]==ls[2]=='X':
        win='X'
    elif ls[6]==ls[4]==ls[2]=='O':
        win = 'O'




x = random.randint(0, 5)
if x >= 0 and x <= 2:
    print("Player 1 will play the first move\nPlayer 1 : X\nPlayer 2 : O")

else:
    print("Player 2 will play the first move\nPlayer 2 : X\nPlayer 1 : O")
printboard()
play()





