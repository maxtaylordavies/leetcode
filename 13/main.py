def romanToInt(s):
    numeralMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = s[::-1]

    num = numeralMap[s[0]]
    for i in range(1, len(s)):
        if numeralMap[s[i]] < numeralMap[s[i - 1]]:
            num -= numeralMap[s[i]]
        else:
            num += numeralMap[s[i]]

    return num


def main():
    print(romanToInt("XIV"))


if __name__ == "__main__":
    main()

