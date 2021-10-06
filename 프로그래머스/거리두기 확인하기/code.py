def solution(places):

    def judge(place,x,y):#x=0,y=1 -> -1,1//1,1//0,0//0,2
        dist_1 = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx,dy in dist_1:
            n_x = dx+x
            n_y = dy+y
            if valid(n_x,n_y) and place[n_x][n_y] == 'P':
                return 0
            elif valid(n_x,n_y) and place[n_x][n_y] == 'O':
                dist_2 = [(-1,0),(1,0),(0,-1),(0,1)] # 0,0 // -1,0//1,0//0,-1//0,1
                for tx,ty in dist_2:       
                    t_x = n_x + tx
                    t_y = n_y + ty
                    if(t_x,t_y) == (x,y) : continue
                    if valid(t_x,t_y):
                        if place[t_x][t_y] == 'P':
                            return 0
        return 1
    
    def valid(x,y):
        return x>=0 and x<=4 and y>=0 and y<=4
    
    answer = [] 
    
    for place in places:       
        state = 1
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    state = judge(place,i,j)
                    if state == 0:
                        answer.append(state)
                        flag = False
                        break
            if state == 0:
                break
        if flag:
            answer.append(state)
        
    
    return answer