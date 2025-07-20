# class Solution():
#     def maxSum(self, grid):
#         m, n = len(grid), len(grid[0])
#         max_sum = float("-inf")

#         for i in range(m - 2):
#             for j in range(n - 2):
#                 topGrid = grid[i][j] + grid[i][j+1] + grid[i][j+2]
#                 middleGrid = grid[i+1][j+1]
#                 bottomGrid = grid[i+2][j] + grid[i+2][j+2] + grid[i+2][j+2]

#                 hourGlass = topGrid+middleGrid+bottomGrid

#                 max_sum = max(max_sum, hourGlass)

#         return max_sum
    
# Sol = Solution()

# grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
# print(Sol.maxSum(grid))  # Output: 30

# grid = [[1,2,3],[4,5,6],[7,8,9]]
# print(Sol.maxSum(grid))  # Output: 35


class Solution():
    def max_hourglass_sum(self, grid):
        m, n = len(grid), len(grid[0])
        max_sum = float('-inf')  # Initialize with negative infinity

        for i in range(m - 2):
            for j in range(n - 2):
                top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                middle = grid[i+1][j+1]
                bottom = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                hourglass = top + middle + bottom
                max_sum = max(max_sum, hourglass)

        return max_sum

    
Sol = Solution()

grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
print(Sol.max_hourglass_sum(grid))  # Output: 30

grid = [[1,2,3],[4,5,6],[7,8,9]]
print(Sol.max_hourglass_sum(grid))  # Output: 35