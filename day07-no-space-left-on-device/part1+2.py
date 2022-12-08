#!python3

class File:
    def __init__(self, name, parent, size):
        self.name = name
        self.size = size
        self.parent = parent

class Dir(File):
    def __init__(self, name, parent):
        super().__init__(name=name, parent=parent, size=0)
        self.files = {}
        self.dirs = {}

    def alter_size(self, delta):
        self.size += delta
        if self.parent:
            self.parent.alter_size(delta)

    def add_file(self, file):
        self.files[file.name] = file
        self.alter_size(delta=file.size)

    def add_dir(self, directory):
        self.dirs[directory.name] = directory
        self.alter_size(delta=directory.size)



with open('input.txt') as file:
    history = file.read()

blocks = [
    block[:-1].split() for block in history.split('$ ')[1:]
]
blocks.pop(0)  # First line redundant

root = Dir('/', None)
current = root
register = [
    root
]

for block in blocks:
    cmd = block.pop(0)
    if cmd == 'cd':
        target_dir_name = block.pop(0)
        if target_dir_name == '..':
            current = current.parent
        elif target_dir_name == '/':
            current = root
        else:
            # if not target_dir_name in current.dirs.keys():
            #     target_dir = Dir(name=target_dir_name, parent=current)
            #     current.add_dir(directory=target_dir)
            current = current.dirs[target_dir_name]
    if cmd == 'ls':
        while block:
            size_or_type, name = block[:2]
            del block[:2]
            if size_or_type == 'dir':
                if not name in current.dirs.keys():
                    target_dir = Dir(name=name, parent=current)
                    current.add_dir(directory=target_dir)
                    register.append(target_dir)
            else:
                size = int(size_or_type)
                if not name in current.files.keys():
                    target_file = File(name=name, parent=current, size=size)
                    current.add_file(file=target_file)

result1 = sum([ d.size for d in register if d.size <= 100000 ])
print(f'Result - part 1: {result1}')

to_be_freed = root.size - 40000000
result2 = min([ d.size for d in register if d.size >= to_be_freed ])
print(f'Result - part 2: {result2}')
