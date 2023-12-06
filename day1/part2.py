def main():
    file = open("input", "r")
    lines = file.readlines()
    total = 0

    string_to_digit = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5v",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for line in lines:
        digits = ""

        for i in range(len(string_to_digit)):
            line = line.replace(
                list(string_to_digit.keys())[i],
                str(list(string_to_digit.values())[i]),
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
