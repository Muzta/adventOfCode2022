from directory import Directory
filePath = './input.txt'


def main():
    partOne = processFile('one')
    partTwo = processFile('two')
    print(f'The sum of the total sizes is {partOne}')
    print(f'The smallest directory size is {partTwo}')


def processFile(part):
    file = open(filePath, 'r')
    lines = file.readlines()
    root = Directory('/')
    currentDirectory = root

    for line in lines[1:]:
        line = line.replace('\n', '').split(' ')
        if line[0] == '$':
            if line[1] == 'ls':
                continue
            else:
                if line[2] == '..':
                    currentDirectory = currentDirectory.parentDirectory

                else:
                    for directory in currentDirectory.childDirectories:
                        if directory.name == line[2]:
                            currentDirectory = directory
                            break

        else:
            if line[0].isnumeric():
                currentDirectory.directSize += int(line[0])
            else:
                newChildDirectory = Directory(line[1], currentDirectory)
                currentDirectory.addChildDirectory(newChildDirectory)

    if part == 'one':
        return getSumOfAtMostSubdirectories(root)
    else:
        filesystemSize = 70000000
        requiredSize = 30000000
        rootSize = root.getTotalSize()
        unusedSize = filesystemSize - rootSize
        minimumDirSizeRequired = requiredSize - unusedSize
        return partTwo(directory=root, smallestDirectorySizeRequired=minimumDirSizeRequired, smallestDirectorySizeFound=rootSize)


def getSumOfAtMostSubdirectories(directory):
    sumSizes = 0

    for subdirectory in directory.childDirectories:
        dirSize = subdirectory.getTotalSize()
        if dirSize <= 100000:
            sumSizes += dirSize

        sumSizes += getSumOfAtMostSubdirectories(subdirectory)

    return sumSizes


def partTwo(directory, smallestDirectorySizeRequired, smallestDirectorySizeFound):
    for dir in directory.childDirectories:
        dirSize = dir.getTotalSize()

        if dirSize > smallestDirectorySizeRequired:
            if dirSize < smallestDirectorySizeFound:
                smallestDirectorySizeFound = dirSize

        smallestDirectorySizeFound = partTwo(directory=dir, smallestDirectorySizeRequired=smallestDirectorySizeRequired,
                               smallestDirectorySizeFound=smallestDirectorySizeFound)
    return smallestDirectorySizeFound


if __name__ == "__main__":
    main()
