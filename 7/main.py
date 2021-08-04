import math


def reverse(self, x: int) -> int:
    if x == 0:
        return 0

    reversed = 0
    sign = int(x / abs(x))
    x = abs(x)

    while x > 0:
        if abs(reversed) > 214748364.8:
            return 0
        reversed = (10 * reversed) + (x % 10)
        x //= 10
    return sign * reversed


def main():
    print(reverse(-123))


if __name__ == "__main__":
    main()
