def solution(record):
    answer = []
    db = []
    nickname_info = {}
    for long_comm in record:
        if long_comm[:5] == 'Enter':
            comm,uid,nickname = long_comm.split(" ")
            nickname_info[uid] = nickname
            db.append(['E',uid])
        elif long_comm[:5] == 'Leave':
            comm,uid = long_comm.split(" ")
            db.append(['L',uid])
        else:
            comm,uid,nickname = long_comm.split(" ")
            nickname_info[uid] = nickname
            
    for log in db:
        if log[0] == 'E':
            data = nickname_info[log[1]] + '님이 들어왔습니다.'
        else:
            data = nickname_info[log[1]] + '님이 나갔습니다.'
            
        answer.append(data)
        
    return answer