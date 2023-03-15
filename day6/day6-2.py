def main():
    with open("input", "r") as f:
        counter = 0
        chars = [None] * 14
        while True:
            c = f.read(1)
            counter += 1

            chars[counter%14] = c

            char_set = set(chars)
            print(chars)
            
            if len(char_set) == 14 and counter > 14:
                print(f"found at {counter}")
                break

            if not c:
                print("end")
                break



if __name__ == "__main__":
    main()