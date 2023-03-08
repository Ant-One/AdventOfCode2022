def move(amount, src, dst):
    tmp = []
    for i in range(amount):
        tmp.append(src.pop())
        
    tmp.reverse()
    for i in range(amount):
        dst.append(tmp[i])

    return (src, dst)

def initialize_stacks(stacks):
    file = open("stacks_in", "r")

    n_stacks = int(len(file.readline()) / 4)

    for i in range(n_stacks):
        stacks.append([])

    file.seek(0)

    for line in file:
        stack_index = 0
        for i in range(0, len(line), 4):
            crate = line[i:i+4]
            if crate[0] == " ":
                stack_index += 1
                continue
            else:
                stacks[stack_index] = [crate[1]] + stacks[stack_index]
                stack_index += 1

    file.close()
    return stacks

def parse_moves(stacks):
    with open("moves_in", "r") as file:
        for line in file:
            splitted = line.split(" ")
            amount = int(splitted[1])
            src = int(splitted[3]) - 1
            dst = int(splitted[5]) -1

            print(f"moving from {src} to {dst}, {amount} crates")

            print("\n============================================\n")

            (stacks[src], stacks[dst]) = move(amount, stacks[src], stacks[dst])
            print(stacks)

    return stacks

def main():
    stacks = []
    stacks = initialize_stacks(stacks)
    stacks = parse_moves(stacks)

    top = ""

    for i in range(len(stacks)):
        top = top + stacks[i][-1]

    size = map(lambda x : len(x), stacks)

    print(f"RESULT : max size {max(size)} and top of piles {top}")

    

if __name__ == "__main__":
    main()