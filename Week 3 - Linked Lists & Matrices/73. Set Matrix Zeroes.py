class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Careful not to turn a row and col into 0 because curr 
        # cell was turned before

        ROWS = len(matrix)
        COLS = len(matrix[0])

        cr = set()
        cz = set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    cr.add(r)
                    cz.add(c)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for r in range(ROWS):
            for c in range(COLS):
                if r in cr or c in cz:
                    matrix[r][c] = 0
