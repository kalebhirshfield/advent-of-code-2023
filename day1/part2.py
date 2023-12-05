def main():
    file = open("input", "r")
    lines = file.readlines()
    total = 0

    string_to_digit = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in lines:
        digits = ""
        for key in string_to_digit.keys():
            if key in line:
                digits += str(string_to_digit[key])
        for letter in line:
            if letter in string_to_digit.keys():
                digits += letter
        digit1 = digits[0]
        digit2 = digits[-1]
        num = int(digit1 + digit2)
        total += num

    return total


if __name__ == "__main__":
    print(main())
