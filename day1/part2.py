def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    total = 0

    for line in lines:
        digits = ""

        line = (
            line.replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5v")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )

        for letter in line:
            if letter.isdigit():
                digits += letter

        digit1 = digits[0]
        digit2 = digits[-1]
        num = int(digit1 + digit2)
        total += num

    return total


if __name__ == "__main__":
    print(main())
