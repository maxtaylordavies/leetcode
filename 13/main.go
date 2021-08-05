package main

import "fmt"

func romanToInt(s string) int {
	numeralMap := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}

	num := numeralMap[string(s[len(s)-1])]

	for i := len(s) - 2; i >= 0; i-- {
		if numeralMap[string(s[i])] < numeralMap[string(s[i+1])] {
			num -= numeralMap[string(s[i])]
		} else {
			num += numeralMap[string(s[i])]
		}
	}

	return num
}

func main() {
	fmt.Println(romanToInt("XIV"))
}
