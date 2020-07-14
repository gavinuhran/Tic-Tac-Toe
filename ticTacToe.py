import pygame
import os
import time
import random

pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 500

START_IMG = pygame.image.load(os.path.join("images", "start.png"))
X_WINS_IMG = pygame.image.load(os.path.join("images", "x_wins.png"))
O_WINS_IMG = pygame.image.load(os.path.join("images", "o_wins.png"))
DRAW_IMG = pygame.image.load(os.path.join("images", "draw.png"))
BOARD_IMG = pygame.image.load(os.path.join("images", "board.jpg"))
X_IMG = pygame.image.load(os.path.join("images", "x.png"))
O_IMG = pygame.image.load(os.path.join("images", "o.png"))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

SQUARES_POS = [(33,29), (193,29), (349,29), (33,189), (193,189), (349,189), (33,346), (193,346), (349,346)]

class X:
    IMG = X_IMG

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

class O:
    IMG = O_IMG

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def draw(self, win):
        win.blit(self.IMG, (self.x, self.y))

def get_square(pos):
    x = pos[0]
    y = pos[1]

    if x > 15 and x < 172 and y > 15 and y < 169:
        return 0
    elif x > 176 and x < 331 and y > 15 and y < 169:
        return 1
    elif x > 335 and x < 485 and y > 15 and y < 169:
        return 2
    elif x > 15 and x < 172 and y > 173 and y < 327:
        return 3
    elif x > 176 and x < 331 and y > 173 and y < 327:
        return 4
    elif x > 335 and x < 485 and y > 173 and y < 327:
        return 5
    elif x > 15 and x < 172 and y > 331 and y < 485:
        return 6
    elif x > 176 and x < 331 and y > 331 and y < 485:
        return 7
    elif x > 335 and x < 485 and y > 331 and y < 485:
        return 8
    
def checkWin(squares, num):
    if squares[0] == num and squares[1] == num and squares[2] == num:
        return True
    if squares[3] == num and squares[4] == num and squares[5] == num:
        return True
    if squares[6] == num and squares[7] == num and squares[8] == num:
        return True
    if squares[0] == num and squares[3] == num and squares[6] == num:
        return True
    if squares[1] == num and squares[4] == num and squares[7] == num:
        return True
    if squares[2] == num and squares[5] == num and squares[8] == num:
        return True
    if squares[0] == num and squares[4] == num and squares[8] == num:
        return True
    if squares[2] == num and squares[4] == num and squares[6] == num:
        return True
    return False

def xHasTwo(squares):
    if squares[0] == 1 and squares[1] == 1:
        return True
    if squares[1] == 1 and squares[2] == 1:
        return True
    if squares[3] == 1 and squares[4] == 1:
        return True
    if squares[4] == 1 and squares[5] == 1:
        return True
    if squares[6] == 1 and squares[7] == 1:
        return True
    if squares[7] == 1 and squares[8] == 1:
        return True
    if squares[0] == 1 and squares[3] == 1:
        return True
    if squares[3] == 1 and squares[6] == 1:
        return True
    if squares[1] == 1 and squares[4] == 1:
        return True
    if squares[4] == 1 and squares[7] == 1:
        return True
    if squares[2] == 1 and squares[5] == 1:
        return True
    if squares[5] == 1 and squares[8] == 1:
        return True
    if squares[0] == 1 and squares[4] == 1:
        return True
    if squares[4] == 1 and squares[8] == 1:
        return True
    if squares[2] == 1 and squares[4] == 1:
        return True
    if squares[4] == 1 and squares[6] == 1:
        return True
    return False
    
def checkForTwo(squares, num):

    # TOP ROW
    if squares[0] == 0 and squares[1] == num and squares[2] == num:
        return True, 0
    if squares[0] == num and squares[1] == 0 and squares[2] == num:
        return True, 1
    if squares[0] == num and squares[1] == num and squares[2] == 0:
        return True, 2
    # MIDDLE ROW
    if squares[3] == 0 and squares[4] == num and squares[5] == num:
        return True, 3
    if squares[3] == num and squares[4] == 0 and squares[5] == num:
        return True, 4
    if squares[3] == num and squares[4] == num and squares[5] == 0:
        return True, 5
    # BOTTOM ROW
    if squares[6] == 0 and squares[7] == num and squares[8] == num:
        return True, 6
    if squares[6] == num and squares[7] == 0 and squares[8] == num:
        return True, 7
    if squares[6] == num and squares[7] == num and squares[8] == 0:
        return True, 8
    # LEFT COLUMN
    if squares[0] == 0 and squares[3] == num and squares[6] == num:
        return True, 0
    if squares[0] == num and squares[3] == 0 and squares[6] == num:
        return True, 3
    if squares[0] == num and squares[3] == num and squares[6] == 0:
        return True, 6
    # MIDDLE COLUMN
    if squares[1] == 0 and squares[4] == num and squares[7] == num:
        return True, 1
    if squares[1] == num and squares[4] == 0 and squares[7] == num:
        return True, 4
    if squares[1] == num and squares[4] == num and squares[7] == 0:
        return True, 7
    # RIGHT COLUMN
    if squares[2] == 0 and squares[5] == num and squares[8] == num:
        return True, 2
    if squares[2] == num and squares[5] == 0 and squares[8] == num:
        return True, 5
    if squares[2] == num and squares[5] == num and squares[8] == 0:
        return True, 8
    # TOP-LEFT TO BOTTOM-RIGHT DIAGNOL
    if squares[0] == 0 and squares[4] == num and squares[8] == num:
        return True, 0
    if squares[0] == num and squares[4] == 0 and squares[8] == num:
        return True, 4
    if squares[0] == num and squares[4] == num and squares[8] == 0:
        return True, 8
    # TOP-RIGHT TO BOTTOM-LEFT DIAGNOL
    if squares[2] == 0 and squares[4] == num and squares[6] == num:
        return True, 2
    if squares[2] == num and squares[4] == 0 and squares[6] == num:
        return True, 4
    if squares[2] == num and squares[4] == num and squares[6] == 0:
        return True, 6
    return False, -1

def checkForO(squares):
    for i in range(len(squares)):
        if squares[i] == 2:
            return True, i
    return False, -1

def bestSquare(squares, index):
    # Check vertical
    if squares[2] == 2 and squares[4] == 2 and squares[6] == 0:
        return True
    
    # Check horizontal
    if index % 3 == 0: 
        if squares[index + 1] == 0 and squares[index + 2] == 0:
            return index + 2
    if index % 3 == 1:
        if squares[index - 1] == 0 and squares[index + 1] == 0:
            return index - 1
    if index % 3 == 2:
        if squares[index - 2] == 0 and squares[index - 1] == 0:
            return index - 2

    # Check diagnols
    if index == 0 and squares[4] == 0 and squares[8] == 0:
        return 8
    if index == 4 and squares[0] == 0 and squares[8] == 0:
        return 0
    if index == 8 and squares[0] == 0 and squares[4] == 0:
        return 0
    if index == 2 and squares[4] == 0 and squares[6] == 0:
        return 6
    if index == 4 and squares[2] == 0 and squares[6] == 0:
        return 2
    if index == 6 and squares[2] == 0 and squares[4] == 0:
        return 2

    # Supply any open square
    for i in range(len(squares)):
        if squares[i] == 0:
            return i
            
def anyCorner():
    corners = [0,2,6,8]
    return corners[random.randint(0,3)]

def playO(squares):
    # Check if O can win
    oHasTwo, winningSquare = checkForTwo(squares, 2)
    if oHasTwo and squares[winningSquare] == 0:
        return winningSquare

    # Check if X can be blocked
    xHasTwo, blockSquare = checkForTwo(squares, 1)
    if xHasTwo and squares[blockSquare] == 0:
        return blockSquare
    
    # If O has played before, advance a path, or start a new one
    oHasPlayed, index = checkForO(squares)
    if oHasPlayed:
        return bestSquare(squares, index)
    
    # If O has not played before, pick middle, or corner if middle is not available
    if squares[4] == 0:
        return 4
    else:
        return anyCorner()    

def checkForDraw(squares):
    for square in squares:
        if square == 0:
            return False
    return True

def draw_start_window(win):
    win.blit(START_IMG, (0,0))
    pygame.display.update()

def draw_play_window(win, x_list, o_list):
    win.blit(BOARD_IMG, (0,0))

    for x in x_list:
        x.draw(win)

    for o in o_list:
        o.draw(win)

    pygame.display.update()

def draw_x_won_window(win):
    win.blit(X_WINS_IMG, (0,0))
    pygame.display.update()

def draw_o_won_window(win):
    win.blit(O_WINS_IMG, (0,0))
    pygame.display.update()  

def draw_draw_window(win):
    win.blit(DRAW_IMG, (0,0))
    pygame.display.update()

def main():
    state = 'start'
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True

    # Variables for state 'play'
    squares = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0=Empty    1=X     2=O
    x_list = []
    o_list = []
    userTurn = True
    
    while run:
        clock.tick(30) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # CHECK FOR QUIT
                run = False
                pygame.quit()
                quit()
        # Start screen
        if state == 'start':
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # CHECK FOR QUIT
                    run = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 162 and pos[0] <= 338 and pos[1] >= 278 and pos[1] <= 335:
                        state = 'play'
                        squares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        x_list = []
                        o_list = []
                        userTurn = True
            draw_start_window(win)

        # Gameplay
        if state == 'play':
            clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # CHECK FOR QUIT
                    run = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP and userTurn: # CHECK FOR USERS MOVE
                    square = get_square(pygame.mouse.get_pos())
                    if squares[square] == 0:
                        squares[square] = 1
                        x = X(SQUARES_POS[square])
                        x_list.append(x)
                        if checkWin(squares, 1):
                            state = 'x won'
                        if checkForDraw(squares):
                            state = 'draw'
                        userTurn = False
                elif not userTurn:
                    time.sleep(0.75)
                    square = playO(squares)
                    if squares[square] == 0:
                        squares[square] = 2
                        o = O(SQUARES_POS[square])
                        o_list.append(o)
                        if checkWin(squares, 2):
                            state = 'o won'
                        userTurn = True     
            draw_play_window(win, x_list, o_list)

        # Endgame screen
        if state == 'x won' or state == 'o won' or state == 'draw':
            clock.tick(5)
            tempState = state
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # CHECK FOR QUIT
                    run = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0] >= 51 and pos[0] <= 227 and pos[1] >= 278 and pos[1] <= 335:
                        tempState = 'start'
                    elif pos[0] >= 274 and pos[0] <= 449 and pos[1] >= 278 and pos[1] <= 335:
                        run = False
                        pygame.quit()
                        quit()
            if state == 'x won':
                draw_x_won_window(win)
            elif state == 'o won':
                draw_o_won_window(win)
            elif state == 'draw':
                draw_draw_window(win)
            state = tempState
main()
