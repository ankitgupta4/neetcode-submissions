class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictA = defaultdict(int)
        dictB = defaultdict(int)
        for i in range(9):
            for j in range(9):
                if board[i][j]!="." and dictA[board[i][j]]==1:
                        return False
                dictA[board[i][j]]=1
                if board[j][i]!="." and dictB[board[j][i]]==1:
                        return False
                dictB[board[j][i]]=1
            
            dictA = defaultdict(int)
            dictB = defaultdict(int)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dictC = defaultdict(int)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l]!="." and dictC[board[k][l]]==1:
                                return False
                        dictC[board[k][l]]=1
                dictC = defaultdict(int)
                        
                
        return True

        