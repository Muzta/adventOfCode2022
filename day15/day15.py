filePath = './input.txt'

ROWTOSEARCH = 2000000
COORDINATENOTLONGERTHAN = 4000000
MULTIPLYTUNNINGFREQUENCY = 4000000

def main():
    partOne = processFile(part='one')
    partTwo = processFile(part='two')
    print(f'{partOne} positions cannot contain a beacon')
    print(f'Its tuning frequency is {partTwo}')

def processFile(part):
    setPositionsCannotExist = set()
    # List of beacon at the searched row
    beaconsSearchedRow = []
    # Variable for the second part, dict of sensors coordinate and its manhattan distance
    dictManhattanDistanceSensors = {}

    # Build the cave map
    with open(filePath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            sensor, beacon = getSensorBeaconCoordFromLine(line)

            if part == 'one':
                # If beacon height is the same as the searched row, add it to the list if not already
                if beacon[1] == ROWTOSEARCH: 
                    if beacon not in beaconsSearchedRow: beaconsSearchedRow.append(beacon)
                # If the searched row is inside the signal power, add the positions not yet registered which are contained in that row
                distanceToRow = edgeDistanceToRow(sensor=sensor, beacon=beacon, row=ROWTOSEARCH)

                if distanceToRow: 
                    minEdgeDistante, maxEdgeDistance = (distanceToRow[0], distanceToRow[1])
                    for pos in range(minEdgeDistante, maxEdgeDistance + 1):
                        setPositionsCannotExist.add(pos)

            else:
                dictManhattanDistanceSensors[sensor] = getManhattanDistance(sensor, beacon)
                
    if part == 'one':
        # Return the list of position in that row that cannot be minus the number of beacons positioned there
        return len(setPositionsCannotExist) - len(beaconsSearchedRow)

    else:
        frequencyTunning = None
        coord = findNoDetectedCoord(dictManhattanDistanceSensors)
        frequencyTunning = coord[0] * MULTIPLYTUNNINGFREQUENCY + coord[1]
        return frequencyTunning

def getSensorBeaconCoordFromLine(line):
    line = line.strip().split(':')

    sensor = line[0]
    sensor = sensor.split(',')
    sensor = ( int(sensor[0].split('=')[1]) , int(sensor[1].split('=')[1]) )

    beacon = line[1]
    beacon = beacon.split(',')
    beacon = ( int(beacon[0].split('=')[1]) , int(beacon[1].split('=')[1]) )

    return sensor, beacon

# Find every spot of resting sand. Bottom will be defined only on the second part of the problem as the y coord of the floor
def getManhattanDistance(sensor, beacon) -> int:
    manhattanDistance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return manhattanDistance

def edgeDistanceToRow(sensor, beacon, row):
    manhattanDistance = getManhattanDistance(sensor, beacon)
    yDifferenceSensorRow = abs(sensor[1] - row)
    # If the searched row isn't contained in the manhattan distance, return False
    if manhattanDistance < yDifferenceSensorRow: return False

    # Else, return the min and max edges of that row
    leftManhattanDistance = manhattanDistance - yDifferenceSensorRow
    return ( sensor[0] - leftManhattanDistance, sensor[0] + leftManhattanDistance )

def findNoDetectedCoord(dictManhattanDistanceSensors):
    for element in dictManhattanDistanceSensors.items():
        sensor = element[0]
        manhattanDistance = element[1]

        # Check if the signal area is above the row 0 and take number of potential spots of its side on that line
        if sensor[1] - manhattanDistance < 0: nextXCoord = manhattanDistance - sensor[1]
        else: nextXCoord = 0
        
        top = sensor[1] - manhattanDistance - 1
        if 0 <= top <= COORDINATENOTLONGERTHAN:
            if checkEmptySlot((sensor[0], top), dictManhattanDistanceSensors):
                return (sensor[0], top)

        bottom = sensor[1] + manhattanDistance + 1
        if 0 <= bottom <= COORDINATENOTLONGERTHAN:
            if checkEmptySlot((sensor[0], bottom), dictManhattanDistanceSensors):
                return (sensor[0], bottom)

        for y in range(max(0, sensor[1] - manhattanDistance), min(sensor[1] + manhattanDistance + 1, COORDINATENOTLONGERTHAN + 1)):
            left = sensor[0] - nextXCoord - 1
            if 0 <= left <= COORDINATENOTLONGERTHAN:
                if checkEmptySlot((left, y), dictManhattanDistanceSensors):
                    return (left, y)
            
            right = sensor[0] + nextXCoord + 1
            if 0 <= right <= COORDINATENOTLONGERTHAN:
                if checkEmptySlot((right, y), dictManhattanDistanceSensors):
                    return (right, y)

            # Check whether the signal pyramid area is getting greater or lower, and update the next x coord
            if y < sensor[1]: nextXCoord += 1
            else: nextXCoord -= 1

    return None
            
def checkEmptySlot(coordinate, dictManhattanDistanceSensors):
    for element in dictManhattanDistanceSensors.items():
        if getManhattanDistance(sensor=element[0], beacon=coordinate) <= element[1]:
            return False
    return True

if __name__ == "__main__":
    main()