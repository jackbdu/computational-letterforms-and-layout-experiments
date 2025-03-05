#!/usr/bin/env python3
import math
import time
import os
import random


def clearScreen():
    # https://stackoverflow.com/a/2084628
    os.system("cls" if os.name == "nt" else "clear")


def generateIndexMatrix(colsNum, rowsNum):
    matrix = []
    for r in range(rowsNum):
        matrix.append([])
        for c in range(colsNum):
            matrix[-1].append(random.randrange(2))
    return matrix


def main():

    # DEFINE TILE SHAPES

    tiles = [
        ["00100", "01000", "10001", "00010", "00100"],
        ["00100", "00010", "10001", "01000", "00100"],
    ]

    foregroundChars = list(map(chr, range(65, 91)))
    backgroundChars = ".,"

    # TILE PARAMETERS

    tileWidth = len(tiles[0][0])
    tileHeight = len(tiles[0])
    width = 32
    height = 18
    tileColsNum = math.ceil(width / tileWidth)
    tileRowsNum = math.ceil(height / tileHeight)

    # ANIMATION PARAMETERS

    frameCount = 0
    frameRate = 12
    patternIntervalFramesNum = frameRate

    try:
        clearScreen()

        while True:
            frameCount += 1

            if frameCount % patternIntervalFramesNum == 1:
                tileIndexMatrix = generateIndexMatrix(tileColsNum, tileRowsNum)

            charRows = []
            for y in range(height):
                charRow = []
                for x in range(width):
                    backgroundChar = random.choice(backgroundChars)
                    foregroundChar = random.choice(foregroundChars)
                    tileC = math.floor(x / tileWidth)
                    tileR = math.floor(y / tileHeight)
                    tileX = x % tileWidth
                    tileY = y % tileHeight
                    tileIndex = tileIndexMatrix[tileR % tileRowsNum][
                        tileC % tileColsNum
                    ]
                    tile = tiles[tileIndex]
                    character = (
                        foregroundChar if tile[tileY][tileX] == "1" else backgroundChar
                    )
                    charRow.append(character)
                charRows.append(" ".join(charRow))
            frame = "\n".join(charRows)
            # https://stackoverflow.com/a/50560686
            print("\033[H")
            print(frame)
            time.sleep(1 / frameRate)

    except KeyboardInterrupt:
        print("\nBye!")


main()
