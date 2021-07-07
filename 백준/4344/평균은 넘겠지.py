case = int(input())

for i in range(case):
    case_list = list(map(int, input().split()))
    SUM = 0
    avg = 0.0
    for j in range(case_list[0]):
        SUM += case_list[j+1]
    avg = float(SUM / case_list[0])
    cnt = 0
    for score in case_list[1:]:
        if(score > avg):
            cnt += 1
    rate = (cnt / case_list[0]) * 100

    print("{:.3f}%".format(rate))
