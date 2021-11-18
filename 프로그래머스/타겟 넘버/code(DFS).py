def solution(numbers, target):
    answer = 0
    depth = 0
    answer = DFS(numbers, target, depth, len(numbers))
    return answer

def DFS(numbers, target, depth, t_depth):
    if depth == t_depth:
        num = sum(numbers)
        if num == target:
            return 1
        else:
            return 0
    else:
        plus = DFS(numbers, target, depth+1, t_depth)
        numbers[depth] *= -1
        minus = DFS(numbers, target, depth+1, t_depth)
        return plus + minus