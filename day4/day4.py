filePath = './input.txt'
numberOfPairs = 0

def main():
    numberOfPairsOne = processFile('contains')
    numberOfPairsTwo = processFile('overlap')
    print(f'The sum of priorities in part one is {numberOfPairsOne}')
    print(f'The sum of priorities in part two is {numberOfPairsTwo}')


def processFile(comparisonType):
    global numberOfPairs
    numberOfPairs = 0

    file = open(filePath, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip().split(',')
        firstPosition = line[0]
        secondPosition = line[1]

        if setsComparison(range1 = firstPosition, range2 = secondPosition, comparison = comparisonType): numberOfPairs += 1

    file.close()
    return numberOfPairs

def setsComparison(range1, range2, comparison):
    range1 = range1.split('-')
    firstPositionRangeOne = int(range1[0])
    secondPositionRangeOne = int(range1[1])
    firstRange = set(range(firstPositionRangeOne, secondPositionRangeOne + 1))

    range2 = range2.split('-')
    firstPositionRangeTwo = int(range2[0])
    secondPositionRangeTwo = int(range2[1])
    secondRange = set(range(firstPositionRangeTwo, secondPositionRangeTwo + 1))

    meetsComparison = False

    if comparison == 'contains':
        if firstRange.issubset(secondRange) or secondRange.issubset(firstRange): meetsComparison = True

    else:
        overlappedSet = firstRange.intersection(secondRange)
        if len(overlappedSet) > 0: meetsComparison = True
    
    return meetsComparison

if __name__ == "__main__":
    main()