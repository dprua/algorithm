class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = date.split('-')
        info = [31,28,31,30,31,30,31,31,30,31,30,31]
        flag = False
        day_sum = 0

        if int(y)%4 == 0:
            if int(y) % 100 == 0:
                if int(y) % 400 == 0:
                    flag = True
                else:
                    flag = False
            else:
                flag = True

        if flag: #윤년이면
            info[1] +=1

        for i in range(1,int(m)):
            day_sum += info[i-1]

        day_sum += int(d)

        return day_sum