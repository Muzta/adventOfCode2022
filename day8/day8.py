filePath = './input.txt'

def main():
    partOne = processFile('one')
    partTwo = processFile('two')
    print(f'There are {partOne} visible trees from outside the grind')
    print(f'The highest scenic score is {partTwo}')


def processFile(part):
    file = open(filePath, 'r')
    lines = file.readlines()
    treesMap = []

    for line in lines:
        treesLine = list(line.replace('\n', ''))
        treesMap.append(treesLine)

    treesMapRowSize = len(treesMap)
    treesMapColumnSize = len(treesMap[0])

    if part == 'one':
        nVisibleTrees = countVisibleTrees(treesMap, treesMapRowSize, treesMapColumnSize)
        return nVisibleTrees
    else:
        highestScenicScore = partTwo(treesMap, treesMapRowSize, treesMapColumnSize)
        return highestScenicScore

def countVisibleTrees(treesMap, mapRowSize, mapColumnSize):
    edgeTrees = 2*mapColumnSize + 2*mapRowSize - 4
    numberVisibleTrees = edgeTrees
    
    for row in range(1, mapRowSize - 1):
        for column in range(1, mapColumnSize - 1):
            isVisible = checkVisibility(treesMap=treesMap, treeRow=row, treeColumn=column)
            if isVisible: numberVisibleTrees += 1

    return numberVisibleTrees

def checkVisibility(treesMap, treeRow, treeColumn):
    treesMapRowSize = len(treesMap)
    treesMapColumnSize = len(treesMap[0])
    treeBeingChecked = treesMap[treeRow][treeColumn]

    # Check top
    for row in range(treeRow):
        if treesMap[row][treeColumn] >= treeBeingChecked:
            break
        else:
            if row == (treeRow - 1): return True

    # Check left
    for column in range(treeColumn):
        if treesMap[treeRow][column] >= treeBeingChecked: 
            break
        else:
            if column == (treeColumn - 1): return True

    # Check down
    for row in range(treeRow + 1, treesMapRowSize):
        if treesMap[row][treeColumn] >= treeBeingChecked: 
            break
        else:
            if row == (treesMapRowSize - 1): return True

    # Check right
    for column in range(treeColumn + 1, treesMapColumnSize):
        if treesMap[treeRow][column] >= treeBeingChecked: 
            break
        else:
            if column == (treesMapColumnSize - 1): return True

    return False

def partTwo(treesMap, mapRowSize, mapColumnSize):
    highestScenicScore = 0

    for row in range(1, mapRowSize - 1):
        for column in range(1, mapColumnSize - 1):
            if getScenicScore(treesMap, row, column) > highestScenicScore: 
                highestScenicScore = getScenicScore(treesMap, row, column)

    return highestScenicScore

def getScenicScore(treesMap, treeRow, treeColumn):
    treesMapRowSize = len(treesMap)
    treesMapColumnSize = len(treesMap[0])
    treeHouseSpot = treesMap[treeRow][treeColumn]

    nTopVisibleTrees = 0
    nLeftVisibleTrees = 0
    nDownVisibleTrees = 0
    nRightVisibleTrees = 0

    # Check top
    for row in reversed(range(treeRow)):
        currentTree = treesMap[row][treeColumn]
        nTopVisibleTrees += 1
        if currentTree >= treeHouseSpot: break

    # Check left
    for column in reversed(range(treeColumn)):
        currentTree = treesMap[treeRow][column]
        nLeftVisibleTrees += 1
        if currentTree >= treeHouseSpot: break

    # Check down
    for row in range(treeRow + 1, treesMapRowSize):
        currentTree = treesMap[row][treeColumn]
        nDownVisibleTrees += 1
        if currentTree >= treeHouseSpot: break

    # Check right
    for column in range(treeColumn + 1, treesMapColumnSize):
        currentTree = treesMap[treeRow][column]
        nRightVisibleTrees += 1
        if currentTree >= treeHouseSpot: break

    scenicScore = nTopVisibleTrees * nLeftVisibleTrees * nDownVisibleTrees * nRightVisibleTrees
    return scenicScore

if __name__ == "__main__":
    main()