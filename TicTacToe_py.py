import random


ls=[0, 1, 2, 3, 4, 5, 6, 7, 8]
res=0
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
        pt=1
    else:
        print("Player 2 will play the first move\nPlayer 2 : O\nPlayer 1 : X")
        pt=2
        printboard()





def play():
    for num in ls:
        if type(ls[num])==int:
            cont=True
    if pt=1:
        a='X'
        b='O'

    holder = input(f"Enter the position to place {}")






