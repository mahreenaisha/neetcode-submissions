class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m log n) 
        # performing BS on every row
        for row in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1
            for col in range(len(matrix[0])):
                while left <= right:
                    mid = (left + right) // 2

                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1

        return False

                
