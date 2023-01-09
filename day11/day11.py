from monkey import Monkey
import math

filePath = './input.txt'


def main():
    partOne = processFile(topMonkeyBusiness=2, rounds=20, part='one')
    partTwo = processFile(topMonkeyBusiness=2, rounds=10000, part='two')
    print(f'The level of monkey business in part one is {partOne}')
    print(f'The level of monkey business in part two is {partTwo}')


def processFile(topMonkeyBusiness: int, rounds: int, part: str) -> int:
    monkeys = []

    # Create all the monkeys and its start data from the file
    with open(filePath, 'r') as f:
        lines = f.readlines()
        # Monkey data lines
        monkeyLines = []

        for i in range(len(lines)):
            line = lines[i].strip()
            # End of data of the same monkey
            if not line:
                monkeys.append(Monkey(*monkeyLines))
                monkeyLines = []

            else:
                monkeyLines.append(line)
                # When last line, append the monkey too
                if i == (len(lines) - 1):
                    monkeys.append(Monkey(*monkeyLines))

    # Common multiple of all divisibility checks, and took the modulus of the new worry level with it before throwing the item so there is no overflow errorfor big integers
    leastCommonMultiple = 1
    if part == 'two':
        leastCommonMultiple = math.lcm(
            *[monkey.divisibleBy for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            # Which monkey throw the item to
            [trueMonkey, falseMonkey] = [
                monkey.trueStatementToMonkey, monkey.falseStatementToMonkey]

            [trueItems, falseItems] = monkey.getTrueFalseRoundResults(
                part=part, leastCommonMultiple=leastCommonMultiple)

            [monkey.setNewItems(trueItems)
             for monkey in monkeys if monkey.name == trueMonkey]
            [monkey.setNewItems(falseItems)
             for monkey in monkeys if monkey.name == falseMonkey]

    monkeysInspectionTime = [monkey.inspectedItems for monkey in monkeys]
    monkeysInspectionTime.sort(reverse=True)
    monkeyBusiness = 1

    # Multiply the given number of top monkeys inspected items
    for i in range(topMonkeyBusiness):
        monkeyBusiness = monkeyBusiness * monkeysInspectionTime[i]

    return monkeyBusiness


if __name__ == "__main__":
    main()
