#!/usr/bin/env python3
import math
import time
import os
import random


def clearScreen():
    # https://stackoverflow.com/a/2084628
    os.system("cls" if os.name == "nt" else "clear")


def p5map(n, fromMin, fromMax, toMin, toMax):
    return (n - fromMin) / (fromMax - fromMin) * (toMax - toMin) + toMin


def main():

    foregroundPixels = list(map(chr, range(65, 91)))
    # backgroundPixels = ".,:;`'\""
    backgroundPixels = ".,"

    colsNum = 32
    rowsNum = 32
    frameCount = 0
    loopFramesNum = 128
    aspectRatio = colsNum / rowsNum
    frameRate = 60

    centerX = colsNum / 2 / aspectRatio
    centerY = rowsNum / 2
    minRadius = rowsNum / 16
    maxRadius = rowsNum / 3

    try:
        clearScreen()
        while True:
            frameCount += 1
            radius = p5map(
                math.sin(math.pi * 2 * frameCount / loopFramesNum),
                -1,
                1,
                minRadius,
                maxRadius,
            )
            rows = []
            for y in range(rowsNum):
                row = []
                for x in range(colsNum):
                    backgroundPixel = random.choice(backgroundPixels)
                    foregroundPixel = random.choice(foregroundPixels)
                    x /= aspectRatio
                    dist = math.sqrt(
                        (x - centerX) * (x - centerX) + (y - centerY) * (y - centerY)
                    )
                    pixel = foregroundPixel if dist < radius else backgroundPixel
                    row.append(pixel)
                rows.append(" ".join(row))

            frame = "\n".join(rows)
            # https://stackoverflow.com/a/50560686
            print("\033[H")
            print(frame)
            time.sleep(1 / frameRate)

    except KeyboardInterrupt:
        print("\nBye!")


main()
