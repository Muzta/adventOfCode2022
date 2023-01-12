import json

filePath = './input.txt'

def main():
    partOne = processFile(part='one')
    partTwo = processFile(part='two')
    print(f'The sum of the indices of sorted pairs is {partOne}')
    print(f'The decoder key for the distress signal is {partTwo}')


def processFile(part):
    # Variables for first 
    if part == 'one':
        index, indicesSum = 1, 0
    # Variables for second part
    else:
        smallerThanTwo, smallerThanSix = 1, 2

    with open(filePath, 'r') as f:
        lines = f.readlines()
        if part == 'one':
            leftPacket, rightPacket = None, None

        for i in range(len(lines)):
            if part == 'one':
                if i % 3 == 0:  leftPacket = json.loads(lines[i])   # Load the line as a list, not as a string
                elif i % 3 == 1:
                    rightPacket = json.loads(lines[i])
                    # If it's the last line, check lines after saving the packages
                    if (i == len(lines) - 1):
                        if checkPackets(leftPacket, rightPacket) == True: indicesSum += index
                else:
                    if checkPackets(leftPacket, rightPacket) == True: indicesSum += index
                    index += 1
                
            else:
                # Only packets smaller than the searched have to be counted
                if not lines[i].strip(): continue     # Pass the empty lines
                if checkPackets(json.loads(lines[i]), [[2]]) == True: smallerThanTwo += 1
                if checkPackets(json.loads(lines[i]), [[6]]) == True: smallerThanSix += 1

    if part == 'one': return indicesSum
    else: return (smallerThanTwo * smallerThanSix)

def checkPackets(packetOne: list, packetTwo: list) -> bool:
    # If first packet is empty and is shorter than second packet, there're no elements, so it's sorted
    if (len(packetOne) == 0) & (len(packetTwo) != 0): return True

    for i in range(len(packetOne)):
        try:
            leftItem, rightItem = packetOne[i], packetTwo[i]

        except IndexError: # The first packet is greater
            return False

        # If only one element is a list, convert both to list
        if type(leftItem) != type(rightItem):
            if isinstance(leftItem, int): leftItem = [leftItem]
            else: rightItem = [rightItem]
            
        # If there are two lists, recursive call to find inner order
        if isinstance(leftItem, list):
            checkSubpackets = checkPackets(leftItem, rightItem)
            if checkSubpackets is not None: return checkSubpackets

        # If left item is greater, its not sorted, if it's smaller, it is
        else:
            if leftItem > rightItem: return False
            elif leftItem < rightItem: return True

        # If limit of first package is found but second one is longer, it's sorted
        if (i == (len(packetOne) - 1)):
            if (len(packetOne) < len(packetTwo)): return True

if __name__ == "__main__":
    main()