def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    total = 0

    for line in lines:
        line = line.split(":")
        line.remove(line[0])
        line = "".join(line)
        line = line.replace(";", ",").replace(" ", "").replace("\n", "").split(",")

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

        line_power = max(red) * max(green) * max(blue)
        total += line_power

    return total


if __name__ == "__main__":
    print(main())
