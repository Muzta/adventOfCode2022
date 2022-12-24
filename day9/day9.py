filePath = './input.txt'
tailPositionsVisited = []

def main():
    partOne = processFile(numberOfKnots=2)
    partTwo = processFile(numberOfKnots=10)
    print(f'The tail has visited {partOne} positions in part one')
    print(f'The tail has visited {partTwo} positions in part two')


def processFile(numberOfKnots):
    global tailPositionsVisited

    file = open(filePath, 'r')
    lines = file.readlines()
    ropeKnots = [[0,0] for x in range(numberOfKnots)]
    tailPositionsVisited = []

    for line in lines:
        line = line.replace('\n', '').split(' ')

        direction = line[0]
        steps = int(line[1])

        ropeKnots = followSteps(direction, steps, ropeKnots)
    
    return len(tailPositionsVisited)

def followSteps(direction, steps, ropeKnots):
    global tailPositionsVisited

    for n in range(steps):
        # Move the head (1st knot of the rope) to the correct direction
        if direction == 'R': ropeKnots[0][0] += 1
        elif direction == 'L': ropeKnots[0][0] -= 1
        elif direction == 'U': ropeKnots[0][1] += 1
        else: ropeKnots[0][1] -= 1

        for i in range(len(ropeKnots) - 1):
            htDistanceX = ropeKnots[i][0] - ropeKnots[i+1][0]
            htDistanceY = ropeKnots[i][1] - ropeKnots[i+1][1]

            # Any coordinate bigger than 2, must move tail
            if max(abs(htDistanceX), abs(htDistanceY)) == 2:
                # It's a diagonal
                if min(abs(htDistanceX), abs(htDistanceY)) >= 1:
                    # Move the tail left or right
                    ropeKnots[i+1][0] = ropeKnots[i+1][0] + 1 if htDistanceX > 0 else ropeKnots[i+1][0] - 1
                    # Move the tail up or down
                    ropeKnots[i+1][1] = ropeKnots[i+1][1] + 1 if htDistanceY > 0 else ropeKnots[i+1][1] - 1

                # It's same row/column, move wherever it's needed
                else:
                    # It's in the same row
                    if htDistanceX != 0: ropeKnots[i+1][0] += int(htDistanceX / 2)
                    # It's in the same column
                    else: ropeKnots[i+1][1] += int(htDistanceY / 2)

            # Only when its the last knot
            if (i == len(ropeKnots) - 2):
                if ropeKnots[i+1] not in tailPositionsVisited:
                    tailPositionsVisited.append(ropeKnots[i+1][:])    #A copy of the tail position, not a reference

    return ropeKnots

if __name__ == "__main__":
    main()