class Solution():
    def triangularSum(self, nums):
        while len(nums) > 1:
            nums = [ (nums[i] + nums[i+1])% 10 for i in range(len(nums)-1)]
            
        return nums[0]
    
print(Solution().triangularSum([1, 2, 3, 4, 5]))  # Output: 8
print(Solution().triangularSum([5]))             # Output: 5
print(Solution().triangularSum([9, 9, 9, 9]))     # Output: 6
print(Solution().triangularSum([2, 5, 7, 9]))