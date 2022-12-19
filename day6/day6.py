filePath = './input.txt'


def main():
    partOne = processFile('one')
    partTwo = processFile('two')
    print(f'Number of characters processed in part one is {partOne}')
    print(f'Number of characters processed in part two is {partTwo}')


def processFile(part):
    file = open(filePath, 'r')
    line = file.readline()

    if part == 'one': nDistinctCharacters = 4
    else: nDistinctCharacters = 14
        
    charactersProcessed = getCharactersProcessed(line, nDistinctCharacters)
    
    file.close()
    return charactersProcessed


def getCharactersProcessed(line, nDistinctCharacters: int):
    indexFirstEleWindow = 0
    indexLastEleWindow = nDistinctCharacters - 1
    markerWasFound = False
    
    while not markerWasFound:
        setOfCharacters = set(line[indexFirstEleWindow : indexLastEleWindow + 1])

        if len(setOfCharacters) == nDistinctCharacters:
            markerWasFound = True
        
        indexFirstEleWindow += 1
        indexLastEleWindow += 1
    
    return indexLastEleWindow


def getInstructionsPerLine(line):
    line = line.replace('move ', '').replace(
        ' from ', '-').replace(' to ', '-')
    moveFromTo = line.split('-')
    return moveFromTo


def doInstructionsPartOne(stackColumns, moveQuantity, moveFrom, moveTo):
    columnFrom = stackColumns[int(moveFrom) - 1]
    columnTo = stackColumns[int(moveTo) - 1]

    for i in range(int(moveQuantity)):
        columnTo.append(columnFrom[-1])
        del columnFrom[-1]

    return stackColumns

def doInstructionsPartTwo(stackColumns, moveQuantity, moveFrom, moveTo):
    columnFrom = stackColumns[int(moveFrom) - 1]
    columnTo = stackColumns[int(moveTo) - 1]

    # Add the 'moveQuantity' last elements from one column to another
    columnTo.extend(columnFrom[- int(moveQuantity):])
    del columnFrom[- int(moveQuantity):]

    return stackColumns


if __name__ == "__main__":
    main()
