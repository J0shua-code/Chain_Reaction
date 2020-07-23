import sys
import logic
import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLOCK_SIZE = 70
WINDOW_HEIGHT = 0
WINDOW_WIDTH = 0

class Ball:
    def __init__(self, neighbours, maximum, value, position):
        self.color      = ""            # String : "Green" or "Red"
        self.neighbours = neighbours    # List   : positions of neighbours 
        self.maximum    = maximum       # int    : Maximum value
        self.value      = value         # int    : Current value
        self.position   = position      # list   : position of the ball
        self.visible    = False         # Bool   : True or false initially set to false
    
    def updateValue(self):
        
        if(self.value + 1 <= self.maximum):
            self.visible     = True
            self.value      += 1
            return True
        else:
            self.visible    = False
            self.value      = 0
            self.color      = ""
            return False
    
    def isVisible(self):
        return self.visible

    def updateColor(self, color):
        self.color = color

    def getNeighbours(self):
        return self.neighbours
    
    def getValue(self):
        return self.value

    def getColor(self):
        return self.color


class GameOver(Exception):
    pass


class ChainReaction:

    def __init__(self, row, col):
        pygame.init()
        self.ROW = row
        self.COL = col
        self.grid = [[0] * self.COL for i in range(self.ROW)]
        self.gl = logic.GameLogic()
        self.gl.logic(self.grid)
        self.balls_list = [[Ball] * self.COL for i in range(self.ROW)]
        for x in range(row):
            for y in range(col):
                neighbours = self.gl.returnNeighbours(self.grid, x, y)
                ball = Ball(neighbours, self.gl.getMaximum(x, y), 0, [x, y])
                self.balls_list[x][y] = ball

    def main(self):

        WINDOW_HEIGHT = BLOCK_SIZE * self.ROW + 40
        WINDOW_WIDTH = BLOCK_SIZE * self.COL

        global SCREEN
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chain Reaction")
        SCREEN.fill(BLACK)

        TURN_COUNTER = 0
        while True:
            self.drawGrid(self.grid)
            for event in pygame.event.get():

                # To Quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    # sys.exit(0)
                
                # Mousebutton click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = pos[1] // BLOCK_SIZE, pos[0] // BLOCK_SIZE

                    color = ""
                    if TURN_COUNTER == 0:
                        color = "green"
                        
                    else:
                        color = "red"
                        
                    if (color == self.balls_list[x][y].getColor() or self.balls_list[x][y].getColor() == ""):
                        # Update turn counter
                        if TURN_COUNTER == 1:
                            TURN_COUNTER = 0
                        else:
                            TURN_COUNTER = 1

                        self.updateGrid(x, y, color)              
            pygame.display.update()

    def isGameOver(self, color):
        count = 0
        red   = -1
        green = -1
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if(self.balls_list[row][col].getColor() == "red"):
                    red += 1
                if(self.balls_list[row][col].getColor() == "green"):
                    green += 1
                if(self.balls_list[row][col].isVisible()):
                    count += 1
        if count < 3:
            return False
        if(red == -1 and color != "red"):
            print("red game over")
            self.display_gameover_screen("green")
            raise GameOver
            # return True
        if(green == -1 and color != "green"):
            print("green game over")
            self.display_gameover_screen("red")
            raise GameOver
            # return True

    def updateGrid(self, x, y, color):
        
        self.balls_list[x][y].updateColor(color)
        result      = self.balls_list[x][y].updateValue()
        neighbours  = self.balls_list[x][y].getNeighbours()
        self.grid[x][y] = self.balls_list[x][y].getValue()

        if not self.isGameOver(color):
            if result:
                pass
            else:
                for i in range(len(neighbours)):
                    self.updateGrid(neighbours[i][0], neighbours[i][1], color)

    def display_gameover_screen(self, winner):
        global SCREEN
        WINDOW_HEIGHT = BLOCK_SIZE * self.ROW + 40
        WINDOW_WIDTH = BLOCK_SIZE * self.COL
        font = pygame.font.SysFont('Comic Sans MS', 35)
        text = font.render( winner.capitalize() + "  Won !!", False, (0, 255, 0))
        
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        SCREEN.fill((255,255,255))
        SCREEN.blit(text, (10, (int(WINDOW_HEIGHT // 2) - 40)))
        pygame.display.update()


    def drawGrid(self, grid):
        
        font = pygame.font.SysFont('Comic Sans MS', 35)
        i, j = 0, 0
        SCREEN.fill(BLACK)
        for row in range(len(grid)):
            i = 0
            for col in range(len(grid[0])):
                rect = pygame.Rect(i, j, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
                
                # Blank box for default
                text = font.render(str(""), False, (0, 0, 0))
                SCREEN.blit(text, (i + int(BLOCK_SIZE / 3), j + int(BLOCK_SIZE / 5)))

                #red and green
                if(self.balls_list[row][col].isVisible()):
                    if(self.balls_list[row][col].getColor() == "green"):

                        # text = font.render(str(grid[row][col]), False, (0, 255, 0))
                        # SCREEN.blit(text, (i + int(BLOCK_SIZE / 3), j + int(BLOCK_SIZE / 5)))

                        if(self.balls_list[row][col].getValue() == 1):
                            pygame.draw.circle(SCREEN, (0, 255, 0), (i + int(BLOCK_SIZE / 2), j + int(BLOCK_SIZE / 2)), 10)

                        if(self.balls_list[row][col].getValue() == 2):
                            pygame.draw.circle(SCREEN, (0, 255, 0),  (i + int(BLOCK_SIZE / 2) - int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)
                            pygame.draw.circle(SCREEN, (25, 215, 4), (i + int(BLOCK_SIZE / 2) + int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)

                        if(self.balls_list[row][col].getValue() == 3):
                            pygame.draw.circle(SCREEN, (0, 255, 0),  (i + int(BLOCK_SIZE / 2), j + int(BLOCK_SIZE / 3)), 10)
                            pygame.draw.circle(SCREEN, (25, 215, 4), (i + int(BLOCK_SIZE / 2) - int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)
                            pygame.draw.circle(SCREEN, (19, 164, 3), (i + int(BLOCK_SIZE / 2) + int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)

                    if(self.balls_list[row][col].getColor() == "red"):

                        # text = font.render(str(grid[row][col]), False, (255, 0, 0))
                        # SCREEN.blit(text, (i + int(BLOCK_SIZE / 3), j + int(BLOCK_SIZE / 5)))

                        if(self.balls_list[row][col].getValue() == 1):
                            pygame.draw.circle(SCREEN, (255, 0, 0), (i + int(BLOCK_SIZE / 2), j + int(BLOCK_SIZE / 2)), 10)

                        if(self.balls_list[row][col].getValue() == 2):
                            pygame.draw.circle(SCREEN, (255, 0, 0), (i + int(BLOCK_SIZE / 2) - int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)
                            pygame.draw.circle(SCREEN, (210, 5, 5), (i + int(BLOCK_SIZE / 2) + int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)

                        if(self.balls_list[row][col].getValue() == 3):
                            pygame.draw.circle(SCREEN, (255, 0, 0), (i + int(BLOCK_SIZE / 2), j + int(BLOCK_SIZE / 3)), 10)
                            pygame.draw.circle(SCREEN, (210, 5, 5), (i + int(BLOCK_SIZE / 2) - int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)
                            pygame.draw.circle(SCREEN, (164, 5, 5), (i + int(BLOCK_SIZE / 2) + int(BLOCK_SIZE / 8), j + int(BLOCK_SIZE / 2)), 10)
                i = i + BLOCK_SIZE

            j = j + BLOCK_SIZE



if __name__ == "__main__":

    print("Enter grid size row x col")
    row = int(input())
    col = int(input())

    while True:
        cr = ChainReaction(row, col)
        try:
            cr.main()
        except:
            del cr
        print("Play again ? y/n")   
        choice = input()
        if choice.lower() == "y":
            pass
        else:
            exit()


    


    
