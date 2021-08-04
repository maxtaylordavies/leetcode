package main

func twoSum(nums []int, target int) []int {
	rm := make(map[int]int)
	var result []int

	for i, num := range nums {
		remainder := target - num
		if j, ok := rm[remainder]; ok {
			result = []int{i, j}
			return result
		}
		rm[num] = i
	}
	return result
}
