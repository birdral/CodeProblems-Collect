class Solution:
    def jumpFloor(self, number):
        # write code here
        list = [1,2]
        if(number == 1):
            return list[0]
        if(number == 2):
            return list[1]
        for i in range(0,number-2):
            step = list[0]+list[1]
            list[0] = list[1]
            list[1] = step
        return step
