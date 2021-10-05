def solution(s):
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    i=0
    for num in a:
        s = s.replace(num,str(a.index(num)))
        i+=1
    return int(s)