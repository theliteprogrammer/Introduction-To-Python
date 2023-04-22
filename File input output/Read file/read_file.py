with open("input.txt", "r") as f:
    # Iterate over the lines
    for line in f:
        # print each line
        print(line)


with open("input1.txt", "r") as f1:
    # print only first line of f1
    print(f1.readline())

