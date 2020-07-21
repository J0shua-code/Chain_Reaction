from typing import Dict, List, Any, Union


class GameLogic:
    def __init__(self):
        pass

    tri_dict_list: list = []
    quad_dict_list, bi_dict_list = [], []

    def logic(self, gameboard, x, y):

        global tri_dict_list
        tri_dict_list = []
        # the four corners
        for i in range(len(gameboard)):
            for j in range((len(gameboard[i]))):
                if (j == 0 or j == len(gameboard[i]) - 1) and (i == 0 or i == len(gameboard) - 1):
                    tri_dict_list.append({"value": gameboard[i][j], "position": [i, j]})

        # print(tri_dict_list)

        global quad_dict_list
        quad_dict_list = []
        # the center square
        for x in range(len(gameboard)):
            for y in range((len(gameboard[i]))):
                if (0 < x < len(gameboard) - 1) and (0 < y < len(gameboard[x]) - 1):
                    quad_dict_list.append({"value": gameboard[x][y], "position": [x, y]})

        # print(quad_dict_list)

        global bi_dict_list
        bi_dict_list = []
        # for the sides
        for x in range(len(gameboard)):
            for y in range((len(gameboard[i]))):
                if (x == 0 or x == len(gameboard) - 1) and (0 < y < len(gameboard[x]) - 1):
                    bi_dict_list.append({"value": gameboard[x][y], "position": [x, y]})
                if (y == 0 or y == len(gameboard[x]) - 1) and (0 < x < len(gameboard) - 1):
                    bi_dict_list.append({"value": gameboard[x][y], "position": [x, y]})
        # print(bi_dict_list)

    def returnOverflownValues(self, grid):
        overflown_positions = []
        for x in tri_dict_list:
            if x["value"] > 1:
                overflown_positions.append(x["position"])

        for x in quad_dict_list:
            if x["value"] > 3:
                overflown_positions.append(x["position"])

        for x in bi_dict_list:
            if x["value"] > 2:
                overflown_positions.append(x["position"])

        return overflown_positions
