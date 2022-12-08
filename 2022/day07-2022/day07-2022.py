with open('input_day07-2022.txt', 'r') as f:
    lines = f.readlines()


class Disk():
    def __init__(self, name='', size=0, parent=None):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent


root = Disk(name='/')

current_dir = root

i = 1
while i < len(lines):
    if lines[i].strip() == '$ ls':
        i += 1
        while i < len(lines) and lines[i][0] != '$':
            name = lines[i].split()[1]
            if name in current_dir.children:
                i += 1
                continue
            if lines[i].split()[0] == 'dir':
                current_dir.children.append(
                    Disk(name=name, parent=current_dir)
                )
            else:
                size = int(lines[i].split()[0])
                current_dir.children.append(Disk(name=name,
                                                 size=size,
                                                 parent=current_dir))
            i += 1
    elif lines[i].strip() == '$ cd ..':
        current_dir = current_dir.parent
        i += 1
    elif lines[i].strip()[:4] == '$ cd':
        name = lines[i].split()[2]
        for child in current_dir.children:
            if child.name == name:
                current_dir = child
                break
        i += 1


def get_sizes(root):
    if root.children:
        for child in root.children:
            root.size += get_sizes(child)
    return root.size


get_sizes(root)

TOTAL = 70000000
NEED = 30000000
TO_DELETE = NEED - (TOTAL - root.size)

small_dirs = []
big_enough = []


def scan_tree(root):
    if root.children and root.size <= 100000:
        small_dirs.append(root.size)
    if root.children and root.size >= TO_DELETE:
        big_enough.append(root.size)
    for child in root.children:
        scan_tree(child)


scan_tree(root)
big_enough.sort()

print(sum(small_dirs))
print(big_enough[0])
