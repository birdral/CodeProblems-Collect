class Solution:
    def printMatrix(self, matrix):
        # write code here
        len_row = len(matrix)
        len_column = len(matrix[0])
        print_list = []
        if(len_row == 0):
            return print_list
        for i in range(0,(min(len_row,len_column)-1)/2+1):#圈数
            #四条边打印+终止检测
            #注意打印个数处理即可
            for j in range(i,len_column-i):
                print_list.append(matrix[i][j])
            for j in range(i+1,len_row-i):
                print_list.append(matrix[j][len_column-i-1])
            if (len_row-1-i == i):
                return print_list
            for j in range(i+1,len_column-i):
                print_list.append(matrix[len_row-i-1][len_column-j-1])
            if (len_column-1-i == i):
                return print_list
            for j in range(i+1,len_row-i-1):
                print_list.append(matrix[len_row-j-1][i])
        return print_list
