import functools
import operator

class Node:

    def __init__(self, name):
        self.leaves = []
        self.name = name
    
    def add_leaf(self, leaf):
        self.leaves.append(leaf)
        return leaf

    def compute_size(self):
        return functools.reduce(operator.add, [leaf.compute_size() for leaf in self.leaves])

class Leaf:
    size = 0

    def __init__(self, name, size):
        self.size = size
        self.name = name

    def compute_size(self):
        #print(f"SIZE OF {self.name} IS {self.size}")
        return self.size
    
def create_tree(curr_node):
    file = open("/home/antoine/aoc/day7/input", "r")
    file.readline()
    parse_command(curr_node, file)
    file.close()

def parse_command(curr_node, file):
    fetch_lines = True
    while(fetch_lines):
        fetch_lines = False
        command_ = file.readline().strip()
        if command_ == "":
            return
        command = command_.split(" ")
        match command[0]:
            case '$':
                if command[1] == "cd":
                    if command[2] == "..":
                        return
                    else:
                        parse_command(curr_node.add_leaf(Node(command[2])), file)

                if command[1] == "ls":
                    fetch_lines = True
                
            case 'dir':
                fetch_lines = True

            case _ :
                elem = Leaf(command[1], int(command[0]))
                curr_node.add_leaf(elem)
                fetch_lines = True



def main():
    root_node = Node("/")

    create_tree(root_node)

    print(("TOTAL SIZE IS " + str(root_node.compute_size())))

if __name__ == "__main__":
    main()
