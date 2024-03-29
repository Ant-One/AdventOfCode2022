def main():
    with open("input", "r") as f:
        counter = 0
        chars = [0, 0, 0, 0]
        while True:
            c = f.read(1)
            counter += 1

            chars[counter%4] = c

            char_set = set(chars)
            print(chars)
            
            if len(char_set) == 4 and counter > 4:
                print(f"found at {counter}")
                break

            if not c:
                print("end")
                break



if __name__ == "__main__":
    main()