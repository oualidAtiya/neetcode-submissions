
class Solution:


    def row_valid(self, y, board: List[List[str]]) -> bool:
        seen = set()
        x = 0
        width = len(board[0])
        while x < width:
            n = board[y][x]
            if n == ".":
                x += 1
                continue
            if n in seen:
                return False
            seen.add(n)
            x += 1
        return True

    def box_valid(self, x: int, y: int, board: List[List[str]]) -> bool:
        start_x = x
        of_x, of_y = 0, 0
        seen = set()
        while True:
            n = board[y][x]
            if n != '.':
                if n in seen:
                    return False
                seen.add(n)
            if of_x == 2 and of_y == 2:
                break
            if of_x == 2:
                of_x = 0
                x = start_x
                of_y += 1
                y += 1
            else:
                of_x += 1
                x += 1
        return True
            

    def column_valid(self, x, board: List[List[str]]) -> bool:
        seen = set()
        y = 0
        height = len(board)
        while y < height:
            n = board[y][x]
            if n == ".":
                y += 1
                continue
            if n in seen:
                return False
            seen.add(n)
            y += 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x, y = 0, 0
        height, width = len(board), len(board[0])
        # check rows
        for y in range(height):
            if not self.row_valid(y, board):
                return False
        # check columns
        for x in range(width):
            if not self.column_valid(x, board):

                return False
        # check boxes
        x, y = 0, 0
        while True:
            if not self.box_valid(x, y, board):
                return False
            if x == 6 and y == 6:
                break
            if x == 6:
                y += 3
                x = 0
            else:
                x += 3
        return True