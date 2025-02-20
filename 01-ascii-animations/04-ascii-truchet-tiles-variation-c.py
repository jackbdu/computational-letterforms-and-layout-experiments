#!/usr/bin/env python
import math
import time
import os
import random


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def generateIndexMatrix(colsNum, rowsNum, optionsNum):
    matrix = []
    for r in range(rowsNum):
        matrix.append([])
        for c in range(colsNum):
            matrix[-1].append(random.randrange(optionsNum))
    return matrix


def main():

    # DEFINE TILE SHAPES

    # https://nedbatchelder.com/blog/202208/truchet_images.html

    tiles = [
        ["00100", "01000", "10001", "00010", "00100"],  # diagonal arcs 1
        ["00100", "00010", "10001", "01000", "00100"],  # diagonal arcs 2
        # ["00100", "00000", "11111", "00000", "00100"],  # horizontal line
        # ["00100", "00100", "10001", "00100", "00100"],  # vertical line
        # ["00100", "00000", "10001", "00000", "00100"],  # four points
        # ["00100", "01110", "11111", "01110", "00100"],  # filled cross
        ["00100", "00100", "11111", "00100", "00100"],  # cross
        # ["00100", "00010", "10001", "00000", "00100"],  # arc and two points 1
        # ["00100", "00000", "10001", "00010", "00100"],  # arc and two points 2
        # ["00100", "00000", "10001", "01000", "00100"],  # arc and two points 3
        # ["00100", "01000", "10001", "00000", "00100"],  # arc and two points 4
        # ["00100", "01110", "11111", "00000", "00100"],  # small person up
        # ["00100", "00110", "10111", "00110", "00100"],  # small person left
        # ["00100", "00000", "11111", "01110", "00100"],  # small person down
        # ["00100", "01100", "11101", "01100", "00100"],  # small person right
    ]

    foregroundChars = list(map(chr, range(65, 91)))
    backgroundChars = ".,                    "

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
                tileIndexMatrix = generateIndexMatrix(
                    tileColsNum, tileRowsNum, len(tiles)
                )

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
