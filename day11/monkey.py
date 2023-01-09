class Monkey():

    def __init__(self, nameLine, itemsLine, operationLine, divisibleByLine, trueStatementToMonkeyLine, falseStatementToMonkeyLine):
        self.name = self._setMonkeyName(nameLine)
        self.items = self._setStartingItems(itemsLine)
        self.operation = self._setOperation(operationLine)
        self.divisibleBy = self._setDivisibleBy(divisibleByLine)
        self.trueStatementToMonkey = self._setTestMonkey(trueStatementToMonkeyLine)
        self.falseStatementToMonkey = self._setTestMonkey(falseStatementToMonkeyLine)
        self.inspectedItems = 0

    def setNewItems(self, items):
        self.items.extend(items)

    def getTrueFalseRoundResults(self, part: str, leastCommonMultiple: int = None):
        trueItems = []
        falseItems = []

        for item in self.items:
            self.inspectedItems += 1
            newWorryLevel = self._getNewWorryLevel(oldWorryLevel=str(item))
            if part == 'one': newWorryLevel = newWorryLevel // 3
            # Taking the module of the lcm will not affect the future operations 
            else: newWorryLevel = newWorryLevel % leastCommonMultiple

            if self._getTest(newWorryLevel): trueItems.append(newWorryLevel)
            else: falseItems.append(newWorryLevel)

        self.items = []
        return [trueItems, falseItems]

    def _getTest(self, worryLevel):
        return worryLevel % self.divisibleBy == 0

    def _getNewWorryLevel(self, oldWorryLevel):
        operation = self.operation
        # Replace the word 'old' by the specific worry level
        operation = operation.replace('old', oldWorryLevel).split(' ')

        if operation[1] == '*': return int(operation[0]) * int(operation[2])
        else: return int(operation[0]) + int(operation[2])

    def _setMonkeyName(self, line):
        line = line.split('Monkey ')[1]
        line = line.split(':')[0]
        return int(line)

    def _setStartingItems(self, line):
        line = line.replace(' ','').split(':')[1]

        return line.split(',')

    def _setOperation(self, line):
        line = line.split('= ')[1].strip()
        return line

    def _setDivisibleBy(self, line):
        line = line.split('by ')[1]
        return int(line)

    def _setTestMonkey(self, line):
        line = line.split('monkey ')[1]
        return int(line)

    def __repr__(self):
        return 'Monkey ' + str(self.name) + ' items: ' + str(self.items)