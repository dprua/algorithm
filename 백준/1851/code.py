class Node:
    def __init__(self,idx,data):
        self.idx = idx
        self.data = data

def inner_cycle(cur_pos):
    info['m_sum'] = 0
    info['m_min'] = 10000001
    info['cnt'] = 0
    while True:
        chk[cur_pos]=1
        info['cnt']+=1
        info['m_sum'] += storage[cur_pos].data
        info['m_min'] = min(storage[cur_pos].data,info['m_min'])
        next_pos = storage[cur_pos].idx
        if chk[next_pos]:
            break
        cur_pos = next_pos
n = int(input())
storage = []
chk = []
info = {'m_sum' : 0, 'm_min' : 1000001, 'cnt': 0}
total_min = 1000001
result = 0
for i in range(n):
    val = int(input())
    storage.append(Node(i,val))
    chk.append(0)
    total_min = min(val,total_min)

# for i in range(n):
#     print(storage[i].idx,storage[i].data)

storage = sorted(storage, key=lambda s: s.data)

# for i in range(n):
#     print(storage[i].idx,storage[i].data)

for i in range(n):
    if chk[i] == 0 and storage[i].idx != i: #현재 노드가 방문이 안됐고, 사이클이 존재하면!
        inner_cycle(i)#여길 빠져나오면
        result += min((info['m_sum'] - info['m_min'])+info['m_min']*(info['cnt']-1), (info['m_sum']+info['m_min']) + (info['cnt']+1)*total_min)

print(result)

