def solution(dirs):
    answer = 0
    store = set()
    c_x,c_y,dx,dy = 0,0,0,0
    
    for char in dirs:      
        if char == 'U':
            dx,dy = 0, 1
        elif char == 'D':
            dx,dy = 0, -1
        elif char == 'R':
            dx,dy = 1, 0
        else:
            dx,dy = -1, 0
        if (c_x == 5 and char == 'R') or (c_x == -5 and char == 'L') or (c_y == 5 and char == 'U') or (c_y == -5 and char == 'L'):
            continue
        if (c_x,c_y,c_x+dx,c_y+dy) in store or (c_x+dx,c_y+dy,c_x,c_y) in store:  
            pass
        else:
            store.add((c_x,c_y,c_x+dx,c_y+dy))
            store.add((c_x+dx,c_y+dy,c_x,c_y))
            #print(store)
            answer+=1
        c_x += dx
        c_y += dy
    return answer,c_x,c_y


a = solution("LULLLLLLURRLLRRRRRUUUDDDDDDDDDDDLLLLLLLLLLL")

print(a)