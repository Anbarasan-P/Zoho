class Solution():
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from Top to Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse from Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

    matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]


sol = Solution()
matrix = [[1,2,3],[6,9,8],[7,4,5]]
print(sol.spiralOrder(matrix))
# Output: [1,2,3,6,9,8,7,4,5]
