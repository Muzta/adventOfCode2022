import numpy as np

filePath = './input.txt'

SANDSTARTPOSITON = (500, 0)
NMAPROWS = 200
NMAPCOLUMNS = 700
FLOORBELOWLASTHORIZONTALROCK = 2

# To work faster with int, '#' will be substituted by 1 and the sand 'o' with 2

def main():
    partOne = processFile(part='one')
    partTwo = processFile(part='two')
    print(f'{partOne} units of sand come to rest before flowing into the abyss')
    print(f'{partTwo} units of sand come to rest in part two')


def processFile(part):
    caveMatrix = np.zeros((NMAPROWS, NMAPCOLUMNS), dtype=int)
    caveMatrix[SANDSTARTPOSITON[1], SANDSTARTPOSITON[0]] = 5
    # Useful for the second part of the problem
    maxHorizontalRock = 0

    # Build the cave map
    with open(filePath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            coordinatesList = line.strip().split(' -> ')
            for i in range(len(coordinatesList) - 1):
                [xFirstCoord, yFirstCoord] = list(map(int, coordinatesList[i].split(',')))
                [xSecondCoord, ySecondCoord] = list(map(int, coordinatesList[i + 1].split(',')))

                # If the y coordinate is greater, save it as the new floor
                maxYCoord = max(yFirstCoord, ySecondCoord)
                if maxYCoord > maxHorizontalRock: maxHorizontalRock = maxYCoord

                 # Vertical Line of rocks
                if maxYCoord != min(yFirstCoord, ySecondCoord):
                    for y in range(min(yFirstCoord, ySecondCoord), maxYCoord + 1):
                        caveMatrix[y, xFirstCoord] = 1

                # Horizontal line of rocks
                else:
                    for x in range(min(xFirstCoord, xSecondCoord), max(xFirstCoord, xSecondCoord) + 1):
                        caveMatrix[yFirstCoord, x] = 1

        # If it's part two, draw a rock horizontal line as the floor
        if part == 'two':
            for x in range(NMAPCOLUMNS):
                caveMatrix[maxHorizontalRock + FLOORBELOWLASTHORIZONTALROCK, x] = 1

    if part == 'one':
        nSandResting = getNSandResting(caveMatrix=caveMatrix, startPosition=SANDSTARTPOSITON)
    else:
        nSandResting = getNSandResting(caveMatrix=caveMatrix, startPosition=SANDSTARTPOSITON, bottom=maxHorizontalRock + FLOORBELOWLASTHORIZONTALROCK)

    return nSandResting

# Find every spot of resting sand. Bottom will be defined only on the second part of the problem as the y coord of the floor
def getNSandResting(caveMatrix, startPosition, bottom = None) -> int:
    nSandResting = 0

    while True:
        newSandRest = newSand(caveMatrix=caveMatrix, startPosition=startPosition, bottom=bottom)
        
        # If the function return bool, sand has started to flow into the abyss, stop the loop
        if newSandRest == True: break
        # Else, the sand has found a rest spot
        else:
            caveMatrix[newSandRest[1], newSandRest[0]] = 2
            nSandResting += 1
        
        # It's the second part of the problem
        if bottom:
            if newSandRest == startPosition: break

    return nSandResting

def newSand(caveMatrix, startPosition, bottom = None):
    currentPosition = startPosition
    # Undefined loop that only stop wether sand falls forever or the sand can't move again

    while True:
        # If it's first part of the problem, first check if the sand falls forever
        if not bottom:
            if fallsForever(caveColumn=caveMatrix[currentPosition[1]:, currentPosition[0]]): return True
            
        # Move the sand wherever it can, or return its coordinates to draw a sand
        if caveMatrix[currentPosition[1] + 1, currentPosition[0]] == 0:
            currentPosition = (currentPosition[0], currentPosition[1] + 1)
        elif caveMatrix[currentPosition[1] + 1, currentPosition[0] - 1] == 0:
            currentPosition = (currentPosition[0] - 1, currentPosition[1] + 1)
        elif caveMatrix[currentPosition[1] + 1, currentPosition[0] + 1] == 0:
            currentPosition = (currentPosition[0] + 1, currentPosition[1] + 1)
        else:
            return currentPosition

# Pass the cave column from the current sand position and check if there's any rock or sand below
def fallsForever(caveColumn) -> bool:
    return not any([1, 2]) in caveColumn

if __name__ == "__main__":
    main()