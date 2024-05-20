def solution(answers):
    scores= [0]*3
    patterns=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if(answer==pattern[i % len(pattern)]): # 정답 길이가 답안 길이보다 짧은 경우 고려
                scores[j] += 1
    max_score= max(scores)
    highest_scores= []
    for i,score in enumerate(scores):
        if(max_score == score):
            highest_scores.append(i+1)
    return highest_scores

print(solution([1,3,2,4,2]))