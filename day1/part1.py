def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    total = 0

    for line in lines:
        digits = ""

        for letter in line:
            if letter.isnumeric():
                digits += letter

        digit1 = digits[0]
        digit2 = digits[-1]
        num = int(digit1 + digit2)
        total += num

    return total


if __name__ == "__main__":
    print(main())
