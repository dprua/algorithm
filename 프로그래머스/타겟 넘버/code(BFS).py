def solution(numbers, target):
    answer = 0
    layer = [numbers[0],-numbers[0]]
    for num in numbers[1:]:
        temp = []
        for node in layer:
            temp.append(node + num)
            temp.append(node - num)
        layer = temp
    
    for node in layer:
        if node == target:
            answer+=1
            
    return answer