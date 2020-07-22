import sys
import logic
import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLOCK_SIZE = 70
WINDOW_HEIGHT = 0
WINDOW_WIDTH = 0


def main():
    nl = logic.GameLogic()

    print("Enter grid size row x col")
    ROW = int(input())
    COL = int(input())
    grid = [[0] * COL for i in range(ROW)]
    WINDOW_HEIGHT = BLOCK_SIZE * ROW + 40
    WINDOW_WIDTH = BLOCK_SIZE * COL
    global SCREEN
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chain Reaction")
    SCREEN.fill(BLACK)

    while True:
        drawGrid(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("click")
                pos = pygame.mouse.get_pos()
                x, y = pos[1] // BLOCK_SIZE, pos[0] // BLOCK_SIZE
                grid[x][y] += 1
                print(grid, x, y)
                nl.logic(grid)
                nl.returnNeighbours(grid, x, y)
                # ofv = nl.returnOverflownValues(44)
                # if len(ofv) != 0:
                #     grid[x][y] = 0
                #     try:
                #         grid[x - 1][y] += 1
                #         grid[x + 1][y] += 1
                #         grid[x][y - 1] += 1
                #         grid[x][y + 1] += 1
                #     except:
                #         pass
                    # while len(ofv) != 0:
                    #     for x in ofv:
                    #         grid[x[0]][x[1]] = 0
                    #         grid[x[0] - 1][x[1]] += 1
                    #         grid[x[0] + 1][x[1]] += 1
                    #         grid[x[0]][x[1] - 1] += 1
                    #         grid[x[0]][x[1] + 1] += 1
                    #         ofv = nl.returnOverflownValues(grid)


        pygame.display.update()


def drawGrid(grid):
    font = pygame.font.SysFont('Comic Sans MS', 35)
    i, j = 0, 0
    SCREEN.fill(BLACK)
    for col in grid:
        i = 0
        for row in col:
            rect = pygame.Rect(i, j, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            text = font.render(str(row), False, (0, 255, 0))
            SCREEN.blit(text, (i + int(BLOCK_SIZE / 3), j + int(BLOCK_SIZE / 5)))
            i = i + BLOCK_SIZE

        j = j + BLOCK_SIZE


if __name__ == "__main__":
    pygame.init()
    main()
