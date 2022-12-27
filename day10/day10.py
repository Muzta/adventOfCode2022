filePath = './input.txt'

def main():
    partOne = processFile('one')
    partTwo = processFile('two')
    print(f'The sum of the six signal states is {partOne}')
    print(f'\nThe drawing of the second part is:')
    print(partTwo)


def processFile(part):
    file = open(filePath, 'r')
    lines = file.readlines()
    cycle = 0
    xRegister = 1
    # Part one variables
    checkCycles = [20, 60, 100, 140, 180, 220]
    signalStrengths = []
    # Part two variable
    drawing = ''

    def newCycle(part):
        nonlocal cycle, checkCycles, xRegister, signalStrengths, drawing
        if part == 'one':
            cycle += 1
            if cycle in checkCycles: signalStrengths.append(cycle*xRegister)

        else:
            drawing += draw()
            cycle += 1

            if cycle == 40:
                drawing += '\n'
                cycle = 0

    #Drawing function for part two
    def draw():
        nonlocal cycle, xRegister
        if xRegister in (cycle -1, cycle, cycle + 1): return '#'
        else: return '.'

    for line in lines:
        line = line.replace('\n', '').split(' ')

        if line[0] == 'noop': newCycle(part=part)
        else:
            newCycle(part=part)
            newCycle(part=part)
            xRegister += int(line[1])
        
    if part == 'one': return sum(signalStrengths) 
    else: return drawing

if __name__ == "__main__":
    main()