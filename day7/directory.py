class Directory():
    def __init__(self, name, parentDirectory = None):
        self.name = name
        self.parentDirectory = parentDirectory
        self.childDirectories = []
        self.directSize = 0

    def getTotalSize(self):
        directSize = self.directSize
        indirectSize = sum(x.getTotalSize() for x in self.childDirectories)
        totalSize = directSize + indirectSize
        return totalSize

    def addChildDirectory(self, directory):
        self.childDirectories.append(directory)

    def __repr__(self):
        parent = self.parentDirectory
        if parent: name = parent.name 
        else: name = 'root' 

        return (f'Directory "{self.name}" (parent: {name}, children:{self.childDirectories})')