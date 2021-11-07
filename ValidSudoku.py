class Solution:
    def getboxIdx(self,i,j):
        return (i//3)*3+(j//3)
    #// floor division
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num.isdigit():
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    
                    if num in col[j]:
                        return False
                    col[j].add(num)
                    
                    boxIdx = self.getboxIdx(i,j)
                    if num in box[boxIdx]:
                        return False
                    box[boxIdx].add(num)
                    
        return True
