class Solution():
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        return nums[left]
    
Sol = Solution()

# Example Usage
print(Sol.findMin([4,5,6,7,0,1,2]))
print(Sol.findMin([3,4,5,1,2]))
print(Sol.findMin([11,13,15,17]))