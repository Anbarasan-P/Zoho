# https://leetcode.com/problems/two-sum/

# Hash Map(optimized) Method
# Fast and efficient - time complexity is O(n)
# Works great even for large arrays
# But uses extra spaces for dictionary O(n) space
class Solution():
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            total = target - num
            if total in num_map:
                return [num_map[total], i]
            num_map[num] = i

# Brute Force Method
# Simple to understand and implement.
# low for large inputs — time complexity is O(n²).
# Not efficient in real-world applications.

    # def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]



# Example Usage
Sum = Solution()
print(Sum.twoSum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(Sum.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(Sum.twoSum([3, 3], 6))           # Output: [0, 1]
