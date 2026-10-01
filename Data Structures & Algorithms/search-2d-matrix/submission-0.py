class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l = 0
        h = ROWS - 1

        while l <= h:
            mid = (l + h) // 2
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        row = h
        l = 0
        h = COLS - 1

        while l <= h:
            mid = (l + h) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False
