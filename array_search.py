class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        len_row = len(array)
        len_column = len(array[0])
        row = len(array)-1
        column = 0
        while (row >= 0 and column < len_column):
            if (target == array[row][column]):
                return True
            if (column == len_column -1 or row == 0):
                return False
            if (target > array[row][column]):
                column = column + 1
                if(target == array[row][column]):
                    return True
            if (target < array[row][column]):
                row = row - 1
                if(target == array[row][column]):
                    return True
        return False
