def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    allowed_games = []

    for line in lines:
        original_line = line
        line = line.split(":")
        line.remove(line[0])
        line = "".join(line)
        line = line.split(";")
        line = ",".join(line)
        line = line.replace(" ", "")
        line = line.replace("\n", "")
        line = line.split(",")

        red = []
        green = []
        blue = []

        for colour in line:
            num = ""
            if "red" in colour:
                for letter in colour:
                    if letter.isdigit():
                        num += letter
                        red.append(int(num))

            elif "green" in colour:
                for letter in colour:
                    if letter.isdigit():
                        num += letter
                        green.append(int(num))

            elif "blue" in colour:
                for letter in colour:
                    if letter.isdigit():
                        num += letter
                        blue.append(int(num))

        if int(max(red)) <= 12 and int(max(green)) <= 13 and int(max(blue)) <= 14:
            allowed_games.append(lines.index(original_line) + 1)

        total = sum(allowed_games)

    return total


if __name__ == "__main__":
    print(main())
