filePath = './input.txt'
shapeMap = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
            'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
winnerShapes = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

def main():
    totalScoreOne = processFile('one')
    totalScoreTwo = processFile('two')
    print(f'Your total score in part one is {totalScoreOne}')
    print(f'Your total score in part two is {totalScoreTwo}')

def processFile(part):
    totalScore = 0
    file = open(filePath, 'r')
    lines = file.readlines()

    for line in lines:
        line = line.strip().split(' ')
        firstPosition = line[0]
        secondPosition = line[1]

        opponent = shapeMap[firstPosition]
        if part == 'one': you = shapeMap[secondPosition]
        else: you = partTwoGuessShape(opponent, roundResult=secondPosition)

        roundPoints = thisRoundPoints(opponent, you)
        totalScore += roundPoints

    file.close()
    return totalScore

def partTwoGuessShape(opponent, roundResult):
    if roundResult == 'Y': return opponent
    else:
        if roundResult == 'X': return winnerShapes[opponent]
        else:
            winnerList = list(winnerShapes.keys())
            loserList = list(winnerShapes.values())
            opponentPositionInLoserList = loserList.index(opponent)
            return winnerList[opponentPositionInLoserList]


def thisRoundPoints(opponent, you):
    shapePoints = pointsForShape(you)
    winnerPoints = pointsForWinning(opponent, you)
    roundPoints = shapePoints + winnerPoints

    return roundPoints

def pointsForShape(you):
    if you == 'rock': return 1
    elif you == 'paper': return 2
    else: return 3

def pointsForWinning(opponent, you):
    if opponent == you: return 3
    else:
        if winnerShapes[you] == opponent: return 6
        else: return 0

if __name__ == "__main__":
    main()