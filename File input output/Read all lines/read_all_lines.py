with open("input.txt", "r") as infile:
    # TODO: read all lines from input.txt into the list called lines_list
    lines_list = []
    for line in infile:
        lines_list.append(line)

if __name__ == "__main__":
    print(lines_list)
