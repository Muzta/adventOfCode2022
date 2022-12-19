filePath = './input.txt'
numberOfElves = 3
maxCounter = [0] * numberOfElves

def main():
    processFile()
    print(f'The sum of the top 3 elves calories is {sum(maxCounter)}')

def processFile():
    file = open(filePath, 'r')
    lines = file.readlines()
    lastLine = lines[-1]
    temporalCounter = 0 #Acumulative counter until break line
    sortNumberOfLines = 0   #To order array for 'numberOfElves' iterations

    for line in lines:
        line = line.strip()
        isEmptyLine = not line

        if not isEmptyLine:
            temporalCounter += int(line)
            if line == lastLine: 
                checkIfIsTopCalories(temporalCounter)

        else:
            # Put the first 3 counter in the array, skipping the sort
            if sortNumberOfLines < numberOfElves:
                maxCounter[sortNumberOfLines] = temporalCounter
                sortNumberOfLines += 1
            
            else:
                checkIfIsTopCalories(temporalCounter)
            
            temporalCounter = 0

    file.close()

# Replace the lower number in the counter
def checkIfIsTopCalories(temporalCounter):
    maxCounter.sort()
    for i in range(numberOfElves):
        if temporalCounter > maxCounter[i]:
            maxCounter[i] = temporalCounter
            break

if __name__ == "__main__":
    main()