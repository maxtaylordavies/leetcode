package main

import "math"

func reverse(x int) int {
	reversed := 0

	if x == 0 {
		return reversed
	}

	abs := int(math.Abs(float64(x)))
	sign := x / abs

	for abs > 0 {
		if float64(reversed) > 214748364.8 {
			return 0
		}
		reversed = (reversed * 10) + (abs % 10)
		abs = int(math.Floor(float64(abs / 10)))
	}

	return sign * reversed
}

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	return x == reverse(x)
}
