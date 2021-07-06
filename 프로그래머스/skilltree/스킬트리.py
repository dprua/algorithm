def solution(skill, skill_trees):
    answer = len(skill_trees)

    for i in range(len(skill_trees)):
        idx = 0 #현재 배워야 하는 스킬
        for j in skill_trees[i]:
            if j in skill: #현재 스킬트리의 스킬이 스킬 순서에 포함되어 있다면
                if j == skill[idx]:
                    idx += 1
                    pass
                else:
                    answer -= 1
                    break
            else:
                continue

    return answer