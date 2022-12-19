filePath = './input.txt'


def main():
    partOne = processFile('one')
    partTwo = processFile('two')
    print(f'Top crates in part one are {partOne}')
    print(f'Top crates in part two are {partTwo}')


def processFile(part):
    file = open(filePath, 'r')
    lines = file.readlines()

    isLineOfStack = True

    stackLines = []  # List of lines before sorting the stack
    # List of list for each column of the stack, being the first element the index of the column
    stackColumns = []

    for line in lines:
        line = line.replace('\n', '')
        isBlankLine = (line == '')
        if isBlankLine:
            isLineOfStack = False  # When the empty line is found, the stack can be finally mounted
            stackColumns = createStackColumns(stackLines)

        if isLineOfStack:
            stackLines.append(line)
        else:
            if isBlankLine:
                continue
            instructions = getInstructionsPerLine(line)
            if part == 'one':
                stackColumns = doInstructionsPartOne(
                    stackColumns=stackColumns, moveQuantity=instructions[0], moveFrom=instructions[1], moveTo=instructions[2])
            else:
                stackColumns = doInstructionsPartTwo(
                    stackColumns=stackColumns, moveQuantity=instructions[0], moveFrom=instructions[1], moveTo=instructions[2])


    file.close()
    topCratesOfStack = [stack[-1] for stack in stackColumns]
    return ''.join(topCratesOfStack)


def createStackColumns(stackLines: list):
    stackLines.reverse()
    stackColumns = []
    # The line which contains the indexes of the stack
    columnPositions = stackLines[0]
    listOfElementsIndex = [columnPositions.index(
        x) for x in columnPositions if x.isnumeric()]

    for i in listOfElementsIndex:
        newStackColumn = []

        for line in stackLines:
            # If there's element in the line, add it
            if line[i] != ' ':
                newStackColumn.append(line[i])

        stackColumns.append(newStackColumn)

    return stackColumns


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
