class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_col = 0
        for col in range(len(strs[0])):
            col_str = []
            for row in range(len(strs)):
                col_str.append(strs[row][col])
            sorted_col = "".join(sorted(col_str))
            if sorted_col != "".join(col_str):
                deleted_col += 1
        return deleted_col
