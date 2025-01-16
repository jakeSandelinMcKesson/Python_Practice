class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        RowCheck = defaultdict(set)
        ColCheck = defaultdict(set)
        SquareCheck = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in RowCheck[x]
                    or board[x][y] in ColCheck[y] 
                    or board[x][y] in SquareCheck[x//3,y//3]):
                    return False

                RowCheck[x].add(board[x][y])
                ColCheck[y].add(board[x][y])
                SquareCheck[x//3,y//3].add(board[x][y])

        return True

