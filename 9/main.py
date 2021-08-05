def reverse(x):
    if x == 0:
        return 0

    reversed = 0
    while x > 0:
        reversed = (10 * reversed) + (x % 10)
        x //= 10
    return reversed


def isPalindrome(x):
    if x < 0:
        return False

    return x == reverse(x)


def main():
    print(isPalindrome(10))


if __name__ == "__main__":
    main()
