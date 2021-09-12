"""
Student: Noa Israeli
ID: 316392356
Assignment no.: 4
Program: minesweeper.py
"""

import random
def makeBoard(n):
    board = [[0 for column in range(n)] for row in range(n)]
    return board

def makePlayerBoard(n):
    playerBoard = [[' ' for row in range(n)] for column in range(n)]
    return playerBoard

def exposeCells(playerBoard,board,x,y,n):
    # If the coordinate value is != 0 there's and != 'X' nothing to expose
    if(board[x][y] != 'X' and board[x][y]!=0):
        playerBoard[x][y] = board[x][y]
        return playerBoard
    playerBoard[x][y] = board[x][y]
    if (y >=0 and y <= n-2) and (x >= 0 and x <= n-1):
        if playerBoard[x][y+1] == " ": 
            exposeCells(playerBoard,board,x,y+1,n) # center right 1

    if (y >=1 and y <= n-1) and (x >= 0 and x <= n-1):
        if playerBoard[x][y-1] == " ": 
            exposeCells(playerBoard,board,x,y-1,n) # center left

    if (y >= 1 and y <= n-1) and (x >= 1 and x <= n-1):
        if playerBoard[x-1][y-1] == " ": 
            exposeCells(playerBoard,board,x-1,y-1,n)# top left

    if (y >= 0 and y <= n-2) and (x >= 1 and x <= n-1):
        if playerBoard[x-1][y+1] == " ": 
            exposeCells(playerBoard,board,x-1,y+1,n) # top right

    if (y >= 0 and y <= n-1) and (x >= 1 and x <= n-1):
        if playerBoard[x-1][y] == " ": 
            exposeCells(playerBoard,board,x-1,y,n) # top center

    if (y >=0 and y <= n-2) and (x >= 0 and x <= n-2):
        if playerBoard[x+1][y+1] == " ": 
            exposeCells(playerBoard,board,x+1,y+1,n) # bottom right 2

    if (y >= 1 and y <= n-1) and (x >= 0 and x <= n-2):
        if playerBoard[x+1][y-1] == " ": 
            exposeCells(playerBoard,board,x+1,y-1,n) # bottom left

    if (y >= 0 and y <= n-1) and (x >= 0 and x <= n-2):
        if playerBoard[x+1][y] == " ": 
            exposeCells(playerBoard,board,x+1,y,n) # bottom center 
        
    return playerBoard




def printBoard(board,n):
    i=1
    for r in board:
        print("  +",end="")
        for c in range(n):
            print("---+",end="")
        print("")
        print(i,"| ",end="")
        print(" | ".join(str(cell) for cell in r), end="")
        print(" |")
        i+=1
    print("  +",end="")
    for c in range(n):
        print("{:4s}".format("---+"),end="")
    print("")
    for i in range(1,n+1):
        print("{:4d}".format(i),end="")  
    print("")
def generateBombs(board,n):
    #Generating random cell:
    for i in range(2*n):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        if(board[x][y]!='X'):
            board[x][y] = 'X'
            if (y >=0 and y <= n-2) and (x >= 0 and x <= n-1):
                if board[x][y+1] != 'X':
                    board[x][y+1] += 1 # center right
            if (y >=1 and y <= n-1) and (x >= 0 and x <= n-1):
                if board[x][y-1] != 'X':
                    board[x][y-1] += 1 # center left
            if (y >= 1 and y <= n-1) and (x >= 1 and x <= n-1):
                if board[x-1][y-1] != 'X':
                    board[x-1][y-1] += 1 # top left
            if (y >= 0 and y <= n-2) and (x >= 1 and x <= n-1):
                if board[x-1][y+1] != 'X':
                    board[x-1][y+1] += 1 # top right
            if (y >= 0 and y <= n-1) and (x >= 1 and x <= n-1):
                if board[x-1][y] != 'X':
                    board[x-1][y] += 1 # top center
            if (y >=0 and y <= n-2) and (x >= 0 and x <= n-2):
                if board[x+1][y+1] != 'X':
                    board[x+1][y+1] += 1 # bottom right

            if (y >= 1 and y <= n-1) and (x >= 0 and x <= n-2):
                if board[x+1][y-1] != 'X':
                    board[x+1][y-1] += 1 # bottom left

            if (y >= 0 and y <= n-1) and (x >= 0 and x <= n-2):
                if board[x+1][y] != 'X':
                    board[x+1][y] += 1 # bottom center
    return board    
def checkWinCond(playerBoard,board,n):
    for x in range(n):
        for y in range(n):
            if playerBoard[x][y] == ' ' and board[x][y]!='X':
                return False
    return True

def minesweeper():
    print("Welcome to Minesweeper game!")
    while(True):
        n = int(input("Please enter n to make nxn (1<=n<=9): "))
        if(n>9 or n<0):
            print("Choose n between 1 and 9")
        else:
            break

    board=makeBoard(n)
    playerBoard=makePlayerBoard(n)
    board= generateBombs(board,n)
    printBoard(board,n)
    printBoard(playerBoard,n)
    
    while(True):
        x = int(input("Choose x coordinate: "))
        y = int(input("Choose y coordinate: "))
        if(x>n or y>n):
            print("Error: index out of range. Choose again")
        else:
            #  -1 to x and y to let the user choose from 1 to n
            x=x-1
            y=y-1
            if(board[x][y] == 'X'):
                print("You lost!")
                printBoard(board,n)
                break
            if(board[x][y] == playerBoard[x][y]):
                print("You already chose that coordinate, choose again")
            else:
                playerBoard=exposeCells(playerBoard,board,x,y,n) # Recursive function as asked
                if(checkWinCond(playerBoard,board,n)):
                    print("You won!")
                    printBoard(board,n)
                    break
                printBoard(playerBoard,n)
        
        
    
    

if __name__ == "__main__":
    minesweeper()