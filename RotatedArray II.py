class Solution():
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <=right:
            mid = (left + right) // 2

            if nums[mid] == target:
                print(f"Target was found at 1st try")
                return True
            
            if nums[left] == nums[mid] == nums[right]:
                left+=1
                right-=1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1

                else:
                    right = mid - 1

        return False

Sol = Solution()

# Example Usage

print(Sol.search([2,5,6,0,0,1,2], 0))  # True
print(Sol.search([2,5,6,0,0,1,2], 3))  # False
print(Sol.search([4,5,6,6,7,0,1,2,4,4], 0))  # True

            