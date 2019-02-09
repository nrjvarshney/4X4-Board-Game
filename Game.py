
# coding: utf-8

# In[4]:


class Tree(object):
    def __init__(self):
        self.min= None# 1 is min node else 2
        self.child = []
        self.utility = None
        self.child_no=None


# In[2]:


def checkHorizontal():
    for row in range(gameSize[0]):
        for col in range(gameSize[1]-2):
            if(GameBoard[row][col]!=0  and GameBoard[row][col] == GameBoard[row][col+1] == GameBoard[row][col+2]):
                return GameBoard[row][col]
    return 0

def checkVertical():
    for col in range(gameSize[1]):
        for row in range(gameSize[0]-2):
            if(GameBoard[row][col]!=0  and GameBoard[row][col] == GameBoard[row+1][col] == GameBoard[row+2][col]):
                return GameBoard[row][col]
    return 0

def checkDiagonal():
    for row in range(gameSize[0]-2):
        for col in range(0, gameSize[1]-2):
            if(GameBoard[row][col] != 0 and GameBoard[row][col] == GameBoard[row+1][col+1] == GameBoard[row+2][col+2]):
                return GameBoard[row][col]
        for col in range(2, gameSize[1]):
            if(GameBoard[row][col] != 0 and GameBoard[row][col] == GameBoard[row+1][col-1] == GameBoard[row+2][col-2]):
                return GameBoard[row][col]
    return 0

def winner():
    winner = checkHorizontal()
    if(winner != 0):
        return winner
    
    winner = checkVertical()
    if(winner != 0):
        return winner
    return checkDiagonal()

def printState():
    print(GameBoard)
    print(rowIndexForcol)
    
def computeUtility(node , col , turn):
    GameBoard[rowIndexForcol[col]][col] = turn
    rowIndexForcol[col] += 1
    
    winnerOfGame = winner()
    if(winnerOfGame != 0):
        if(winnerOfGame == 1):
            node.utility = 1
        else:
            node.utility = -1;
        rowIndexForcol[col] -= 1
        GameBoard[rowIndexForcol[col]][col] = 0
        return
    next_turn = 2
    if(turn == 2):
        next_turn = 1
    
    for column in range(gameSize[1]):
        if(rowIndexForcol[column] == gameSize[1]):
            node.child.append(Tree())
            node.child[column].utility = 0
            continue
        
        node.child.append(Tree())
        computeUtility (node.child[column] , column, next_turn)
            
        if(turn == 2 and node.child[column].utility == 1):# validated
            node.utility = 1;
            node.child_no = column
            break
        
        if(turn == 1 and node.child[column].utility == -1):# validated
            node.utility = -1;
            node.child_no = column;
            break
    
    if(node.utility is None):
        min_utility=2
        max_utility=-2
        child_number=0
        for colt in range(gameSize[1]):
            if(turn==2):
                #max
                if(max_utility<node.child[colt].utility):
                    max_utility=node.child[colt].utility
                    child_number=colt
            else:
                #min
                if(min_utility>node.child[colt].utility):
                    min_utility=node.child[colt].utility
                    child_number=colt
        if(turn==2):
            node.utility=max_utility
            node.child_no=child_number
            
        else:
            node.utility=min_utility
            node.child_no=child_number  
            
    rowIndexForcol[col] -= 1
    GameBoard[rowIndexForcol[col]][col] = 0
    


# In[5]:


import numpy as np

gameSize =  (4, 4);
GameBoard = np.zeros(gameSize)
rootNode = Tree()
BotTurn = 1
HumanTurn = 2
rowIndexForcol = np.zeros(gameSize[1])
rowIndexForcol = rowIndexForcol.astype(int)

for coln in range(gameSize[1]):
    rootNode.child.append(Tree())
    computeUtility (rootNode.child[coln] , coln, BotTurn)
    if(rootNode.child[coln].utility == 1):
        rootNode.utility = 1
        rootNode.child_no = coln
        break
       


# In[10]:


game_over = 0
currentNode = rootNode
rowIndexForcol = np.zeros(gameSize[1])
rowIndexForcol = rowIndexForcol.astype(int)
gameSize =  (4, 4);
GameBoard = np.zeros(gameSize)

while(game_over == 0):
    child_no = currentNode.child_no
    currentNode = currentNode.child[child_no]
    GameBoard[rowIndexForcol[child_no]][child_no] = 1 
    rowIndexForcol[child_no] += 1
    print("\n")
    print(GameBoard)
    winnerOfGame = winner()
    if(winnerOfGame != 0):
        if(winnerOfGame == 1):
            print("You Lost")
        else:
            print("You Won. Looks like there is some bug in the code!!!")
        break
    colHuman = input("\nEnter Column ")
    print("\n")
    GameBoard[rowIndexForcol[colHuman]][colHuman] = 2
    rowIndexForcol[colHuman] += 1
    
    currentNode = currentNode.child[colHuman]
    print("\n")
    print(GameBoard)
    winnerOfGame = winner()
    if(winnerOfGame != 0):
        if(winnerOfGame == 1):
            print("You Lost")
        else:
            print("You Won. Looks like there is some bug in the code!!!")
        break

