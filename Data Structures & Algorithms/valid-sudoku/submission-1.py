class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        NULL = "."
        NROWS = 9
        NCOLS = 9
        #Scan every row, check
        for row in board:
            visited = [False] * len(row)
            for char in row:
                if char == NULL:
                    continue
                if visited[int(char)-1]:
                    return False

                visited[int(char)-1] = True        
            
        #Scan every col, check
        for i in range(NCOLS):
            column = [row[i] for row in board]
            visited = [False] * len(column)
            for char in column:
                if char == NULL:
                    continue
                if visited[int(char)-1]:
                    return False
                
                visited[int(char)-1] = True

        
        #Scan every square
        square = [0] * 9
        for i in range(3):
            for j in range(3):
                lRowIdx = i * 3
                rRowIdx = (i+1) * 3

                uColIdx = j * 3
                bColIdx = (j+1) * 3

                rows = board[uColIdx:bColIdx]
                square = []
                for row in rows:
                    square.extend(row[lRowIdx:rRowIdx])
                
                visited = [False] * len(square)
                for char in square:
                    if char == NULL:
                        continue

                    if visited[int(char)-1]:
                        return False
                    visited[int(char)-1] = True

        return True