def open_and_parse():
    file = open("input", "r")

    elves = []

    tmp = 0
    
    for line in file:
        if line == "\n":
            elves.append(tmp)
            tmp = 0
        else:
            tmp = tmp + int(line)
    file.close()
    return elves

def print_e(elves):
    for elem in elves:
        print(elem)


def main():
    best = []
    l = open_and_parse()
    for i in range(3):
        best.append(max(l))
        l.pop(l.index(max(l)))

    print(sum(best))
    


if __name__ == "__main__":
    main()
