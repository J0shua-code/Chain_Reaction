from typing import Dict, List, Any, Union

class GameLogic:

    def __init__(self):
        self.values_list = []

    def logic(self, gameboard):

        self.values_list = [[0] * len(gameboard[0]) for i in range(len(gameboard))]
        corners_dict_list = []
        # the four corners
        for i in range(len(gameboard)):
            for j in range((len(gameboard[i]))):
                if (j == 0 or j == len(gameboard[i]) - 1) and (i == 0 or i == len(gameboard) - 1):
                    self.values_list[i][j] = 1

        # the center square
        for x in range(len(gameboard)):
            for y in range((len(gameboard[i]))):
                if (0 < x < len(gameboard) - 1) and (0 < y < len(gameboard[x]) - 1):
                    self.values_list[x][y] = 3

        # for the sides
        for x in range(len(gameboard)):
            for y in range((len(gameboard[i]))):
                if (x == 0 or x == len(gameboard) - 1) and (0 < y < len(gameboard[x]) - 1):
                    self.values_list[x][y] = 2
                if (y == 0 or y == len(gameboard[x]) - 1) and (0 < x < len(gameboard) - 1):
                    self.values_list[x][y] = 2
        


    def returnNeighbours(self, grid, x, y):
        neighbours_list = []
        not_available = ["","","",""]
        
        # check the missing neighbours 
        
        if(x + 1 > len(grid) -1 ):
            not_available[0] = "x"
        if(x - 1 < 0):
            not_available[1] = "x" 
        if(y + 1 > len(grid) - 1):
            not_available[2] = "x"
        if(y - 1 < 0):
            not_available[3] = "x"
        

        
        if(not_available[0] != "x"):
            neighbours_list.append([x + 1, y])
        if(not_available[1] != "x"):
            neighbours_list.append([x - 1, y])
        if(not_available[2] != "x"):
            neighbours_list.append([x, y + 1])
        if(not_available[3] != "x"):
            neighbours_list.append([x, y - 1])
        
        return neighbours_list

    def getMaximum(self, x, y):
        
        return self.values_list[x][y]


