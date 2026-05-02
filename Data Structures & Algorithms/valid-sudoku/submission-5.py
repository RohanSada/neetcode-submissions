class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows, cols = len(board), len(board[0])
        row_dict, col_dict, sub_dict = defaultdict(list), defaultdict(list), defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                val = board[i][j]
                if val == '.':
                    continue
                if val in row_dict[i]:
                    return False
                elif val in col_dict[j]:
                    return False
                elif val in sub_dict[(i//3, j//3)]:
                    return False
                row_dict[i].append(val)
                col_dict[j].append(val)
                sub_dict[(i//3, j//3)].append(val)
        return True
                


        