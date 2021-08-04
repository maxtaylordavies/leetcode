def twoSum(nums, target):
    remainderDict = {}
    for i in range(len(nums)):
        num = nums[i]
        remainder = target - num
        if remainder in remainderDict:
            return i, remainderDict[remainder]
        remainderDict[num] = i
