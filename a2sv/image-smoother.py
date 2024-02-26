class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        opp = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        new_img = deepcopy(img)
        for row in range(len(img)):
            for col in range(len(img[row])):
                opp_value = 0
                len_opp = 0
                cell_point = img[row][col]
                for x, y in opp:
                    if row + x >= 0 and col + y >= 0 and col + y < len(img[row]) and row + x < len(img):
                        opp_value += img[row + x][col + y]
                        len_opp += 1
                new_img[row][col] = int((opp_value+img[row][col])/(len_opp + 1))

        return new_img
