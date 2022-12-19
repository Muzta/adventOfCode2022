import string

filePath = './input.txt'
lettersList = list(string.ascii_lowercase)
lettersList.extend(list(string.ascii_uppercase))

def main():
    sumOfPrioritiesOne = processFile('one')
    sumOfPrioritiesTwo = processFile('two')
    print(f'The sum of priorities in part one is {sumOfPrioritiesOne}')
    print(f'The sum of priorities in part two is {sumOfPrioritiesTwo}')

def processFile(part):
    file = open(filePath, 'r')
    lines = file.readlines()
    numberOfLines = len(lines)
    sumOfPriorities = 0

    for i in range(numberOfLines):
        line = lines[i].replace('\n','')

        if part == 'one':
            elementPriority = partOne(line)
            sumOfPriorities += elementPriority

        else:
            isLastLine = (i == len(lines) - 1)

            if i % 3 == 0 or isLastLine:
                if isLastLine: elvesGroup.append(line)
                
                if i != 0:
                    elementPriority = commonElementPriority(elvesGroup)
                    sumOfPriorities += elementPriority
                
                elvesGroup = [] #Reset the list after each 3rd line
            elvesGroup.append(line)

        i += 1

    file.close()
    return sumOfPriorities

def partOne(line):
    halfLine = int(len(line) / 2)
    firstHalf = line[:halfLine]
    secondHalf = line[halfLine:]
    bothHalfs = [firstHalf, secondHalf]
    elementPriority = commonElementPriority(bothHalfs)
    return elementPriority

def commonElementPriority(lines: list):
    elementInCommonAsSet = findElementInCommon(lines)
    elementInCommon = list(elementInCommonAsSet)[0]
    elementPriority = lettersList.index(elementInCommon) + 1
    return elementPriority

def findElementInCommon(lines : list):
    # Get the common element in a list of lists
    commonElement = set(lines[0]).intersection(*lines)
    return commonElement

if __name__ == "__main__":
    main()