def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    for line in lines:
        line = line.split(":")
        line.remove(line[0])
        line = "".join(line)
        line = line.split(";")
        line = ",".join(line)
        line = line.replace(" ", "")
        line = line.split(",")
        print(line)


if __name__ == "__main__":
    main()
