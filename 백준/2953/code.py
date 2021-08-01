max_score = 0
max_idx = 0
for i in range(5):
    info = list(map(int,input().split(" ")))
    if sum(info) >= max_score:
        max_score = sum(info)
        max_idx = i+1

print(max_idx,max_score)