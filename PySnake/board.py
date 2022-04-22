import random

from pyrfc3339 import generate

class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = {}
        self.void = 0
        self.gerry = 1
        self.apple = -1

        self.head = [0,0]
        self.tail = [0,0]

        for x in range(self.row):
            for y in range(self.col):
                cell = self.void
                self.board[x,y] = cell
    
    def start(self, apples, pos):
        self.board[pos[0],pos[1]] = self.gerry
        self.head[0] = pos[0]
        self.head[1] = pos[1]
        self.tail[0] = pos[0]
        self.tail[1] = pos[1]
        self.generateApple(apples)

    def generateApple(self,apples):
        while apples != 0:
            x = random.randint(0,self.row-1)
            y = random.randint(0,self.col-1)
            if(self.board[x,y] == self.void):
                self.board[x,y] = self.apple
                apples -= 1
