class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        m=len(board[0])
        rows=[ set() for _ in range(9)]
        columns=[set() for _ in range(9)]
        box =[set() for _ in range(9)]
        for i in range(n):
            for j in range(m):
                if board[i][j]==".":
                    continue
                num=board[i][j]

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in columns[j]:
                    return False
                columns[j].add(num)  

                box_index = (i//3)*3+(j//3)

                if num in box[box_index]:
                    return False
                box[box_index].add(num)
        return True
