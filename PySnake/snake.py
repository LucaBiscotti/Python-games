from cmath import rect
from turtle import width
from numpy import True_
from pygame.locals import *
from time import sleep
from tracemalloc import Snapshot
import pygame
from sqlalchemy import false
from board import Board

class Game:
    def __init__(self):
        self.boardsize = (w,w)
        self.screen = pygame.display.set_mode(self.boardsize)
        pygame.display.set_caption('Snake')

        font = pygame.font.SysFont(pygame.font.get_default_font(), 55)
        for i in range(3):
            if (i == 0):
                text = font.render("Loading.", 1, (255,255,255))
            if (i == 1):
                text = font.render("Loading..", 1, (255,255,255))
            if (i == 2):
                text = font.render("Loading...", 1, (255,255,255))
            self.screen.fill("black")
            rect = text.get_rect()
            rect.center = self.boardsize[0]/2, self.boardsize[1]/2
            self.screen.blit(text, rect)
            pygame.display.update(rect)
            sleep(0.3)
    
    def start(self):
        self.b = Board(20,20)
        head = [10,10]
        self.b.start(1,head)
        self.body = []
        self.body.append(head)
        self.size = 1
        self.grow = 1
        self.drawBoard()
        self.loop()
        if self.end() == 0:
            self.start()
    

    def drawBoard(self):
        xi = 0
        yi = 0

        row = self.b.row
        col = self.b.col

        self.screen.fill((0,0,0))

        for x in range(row):
            pygame.draw.line(self.screen,(255,255,255),(xi,0),(xi,w))
            pygame.draw.line(self.screen,(255,255,255),(0,yi),(w,yi))
            xi = xi + row + space
            yi = yi + col + space
        self.drawSnake(row,col)
        self.drawApple(row,col)

    def drawSnake(self,row,col):
        self.snake = pygame.Surface((row + space,col + space))  #Size of snake
        self.snake.fill((8,235,23))

        xi = 0

        for x in range(row):
            yi = 0
            for y in range(col):
                if(self.b.board[x,y] == self.b.gerry):
                    self.screen.blit(self.snake,(xi,yi))
                yi = yi + col + space
            xi = xi + row + space

    def drawApple(self,row,col):
        self.apple = pygame.Surface((row + space,col + space))  #Size of snake
        self.apple.fill((255,255,255))

        xi = 0

        for x in range(row):
            yi = 0
            for y in range(col):
                if(self.b.board[x,y] == self.b.apple):
                    self.screen.blit(self.apple,(xi,yi))
                yi = yi + col + space
            xi = xi + row + space

    def movePlayer(self,dir):
        if self.grow:
            self.b.board[self.b.tail[0],self.b.tail[1]] = self.b.void
        else:
            l = 1
        for i in range(self.size -1):
            self.body[-(i+1)] = self.body[-(i+2)].copy()
        if(dir == 'u'):
            self.body[0][1] -= 1
        if(dir == 'd'):
            self.body[0][1] += 1
        if(dir == 'l'):
            self.body[0][0] -= 1
        if(dir == 'r'):
            self.body[0][0] += 1
        
        self.b.head[0] = self.body[0][0]
        self.b.head[1] = self.body[0][1]
        self.b.tail[0] = self.body[-1][0]
        self.b.tail[1] = self.body[-1][1]

        if self.checkDeath():
            return False
        self.checkApple()
        self.b.board[self.b.head[0],self.b.head[1]] = self.b.gerry
        return True

        
    def checkDeath(self):
        if (self.outOfBoard(self.b.head)):
            return True
        if(self.b.board[self.b.head[0],self.b.head[1]] == self.b.gerry):
            return True
        return False

    def outOfBoard(self,head):
        if(head[0] < 0 or head[0] > self.b.row - 1 or head[1] < 0 or head[1] > self.b.col - 1):
            return True
        return False

    def checkApple(self):
        head = self.b.head
        tail = self.b.tail
        if (self.b.board[head[0],head[1]] == self.b.apple):
            self.size += 1
            self.grow = 0
            self.body.append(tail)
            self.b.generateApple(1)
        else:
            self.grow = 1


    def loop(self):
        self.clock = pygame.time.Clock()
        self.keep_going = 1
        dir = 'n'
        while self.keep_going:
            self.clock.tick(8)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.keep_going = 0
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_ESCAPE]:
                    self.keep_going = 0
                if keys[pygame.K_r]:
                    dir = 'n'
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    if dir != 'u' or self.size == 1:
                        dir = 'd'
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    if dir != 'd' or self.size == 1:
                        dir = 'u'
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    if dir != 'r' or self.size == 1:
                        dir = 'l'
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    if dir != 'l' or self.size == 1:
                        dir = 'r'
            if not self.movePlayer(dir):
                self.keep_going = 0
            else:
                self.drawBoard()
            pygame.display.update()

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 0
            if event.key == pygame.K_ESCAPE:
                return 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rectl.collidepoint(x,y):
                    return 0
                if self.rectr.collidepoint(x,y):
                    return 2
        return 1
        
    def end(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 55)
        font2 = pygame.font.SysFont(pygame.font.get_default_font(), 35)
        self.screen.fill("black")
        pygame.display.update()
        
        text = font.render("You Lost", 1, "red")
        rect = text.get_rect()
        rect.center = self.boardsize[0]/2, self.boardsize[1]/3
        self.screen.blit(text, rect)
        pygame.display.update(rect)

        text = font2.render("Your score was: {}".format(self.size-1), 1, "white")
        score = text.get_rect()
        score.center = self.boardsize[0]/2, self.boardsize[1]/2.5
        self.screen.blit(text, score)
        pygame.display.update(score)

        leftb = font2.render("Try Again", 1, "white")
        self.rectl = leftb.get_rect()
        self.rectl.center = self.boardsize[0]/3, self.boardsize[1]/2
        self.screen.blit(leftb, self.rectl)
        pygame.display.update(self.rectl)

        rightb = font2.render("Exit", 1, "white")
        self.rectr = rightb.get_rect()
        self.rectr.center = self.boardsize[0]/1.5, self.boardsize[1]/2
        self.screen.blit(rightb, self.rectr)
        pygame.display.update(self.rectr)

        goOn = 1
        while(goOn == 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                goOn = self.click(event)
        return goOn


if __name__ == '__main__':
    global w, space
    w = 500
    space = w/100
    pygame.init()
    g = Game()
    g.start()