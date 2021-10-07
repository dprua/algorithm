def solution(n, k, cmd):
    
    answer = ''
    
    linked_list = {i:[i-1,i+1] for i in range(1,n-1)}
    linked_list[0] = [None,1]
    linked_list[n-1] = [n-2,None]
    
    del_info = [] #들어가는 형태 : [idx,prev,next]
    
    state = ['O' for _ in range(n)]
    
    for command in cmd:
        if command[0] == 'U':
            for i in range(int(command[2:])):
                prev,_ = linked_list[k]
                k = prev
            
        elif command[0] == 'D':
            for i in range(int(command[2:])):
                _,nxt = linked_list[k]
                k = nxt
            
        elif command[0] == 'C':
            
            prev,nxt = linked_list[k] #현재 노드(삭제할)정보 추출
            del_info.append([k,prev,nxt]) #삭제정보스택에 삭제된 노드 정보 추가
            state[k] = 'X'
            
            if nxt == None: #마지막 노드를 삭제한 경우
                k = prev
                linked_list[prev][1] = None
            elif prev == None: #맨 처음 노드를 삭제하는 경우
                k = nxt
                linked_list[nxt][0] = prev
            else:
                k = nxt
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
        
        elif command[0] == 'Z':
            
            idx,prev,nxt = del_info.pop()
             
            state[idx] = 'O'
            if prev == None: #맨 처음 노드가 사라졌다고 붙는경우
                linked_list[nxt][0] = idx 
            elif nxt == None: #맨 끝 노드가 사라졌다가 붙는경우
                linked_list[prev][1] = idx
            else:
                linked_list[prev][1] = idx
                linked_list[nxt][0] = idx   

    
    answer = "".join(state)
    return answer