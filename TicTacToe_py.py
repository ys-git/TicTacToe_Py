#Tic Tac Toe using python

import random


ls=[0, 1, 2, 3, 4, 5, 6, 7, 8]
res=0
a,b='A'
again=True
p1=input("Enter the name of Player 1:")
p2=input("Enter the name of Player 1:")


def printboard():
    print(f"{ls[0]}  |  {ls[1]} |  {ls[2]} \n------------\n"
          f"{ls[3]}  |  {ls[4]} |  {ls[5]} \n------------\n"
          f"{ls[6]}  |  {ls[7]} |  {ls[8]} ")

while again:
    x = random.randint(0, 5)
    if x >= 0 and x <= 2:
        print("Player 1 will play the first move\nPlayer 1 : X\nPlayer 2 : O")

    else:
        print("Player 2 will play the first move\nPlayer 2 : X\nPlayer 1 : O")
    printboard()

def chk():
    for num in ls:
        if type(ls[num])==int:
            cont=True

    return cont


def play():
    t = 'X'
    while chk() == True:
        holder = input(f"Enter the position to place {t}")
        ls[holder] =t
        t='O'
















