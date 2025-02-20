#!/usr/bin/env python
import math
import time
import os
import random


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def generateIndexMatrix(colsNum, rowsNum):
    matrix = []
    for r in range(rowsNum):
        matrix.append([])
        for c in range(colsNum):
            if c % 2 == r % 2:
                matrix[-1].append(random.randrange(0, 2))
            else:
                matrix[-1].append(random.randrange(2, 4))
    return matrix


def main():

    # DEFINE TILE SHAPES

    tiles = [
        ["11100", "11000", "10001", "00011", "00111"],
        ["11100", "11110", "11111", "01111", "00111"],
        ["00111", "00011", "10001", "11000", "11100"],
        ["00111", "01111", "11111", "11110", "11100"],
    ]

    foregroundChars = list(map(chr, range(65, 91)))
    backgroundChars = ".,      "

    # TILE PARAMETERS

    tileWidth = len(tiles[0][0])
    tileHeight = len(tiles[0])
    width = 32
    height = 18
    tileColsNum = math.ceil(width / tileWidth)
    tileRowsNum = math.ceil(height / tileHeight)

    # ANIMATION PARAMETERS

    frameCount = 0
    frameRate = 60
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
            print("\033[H")
            print(frame)
            time.sleep(1 / frameRate)

    except KeyboardInterrupt:
        print("\nBye!")


main()
