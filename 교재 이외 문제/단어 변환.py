def issame1(begin, word):
    n= len(begin)
    cnt= 0
    for idx, b in enumerate(begin):
        if word[idx] == b:
            cnt+=1
    if cnt == n-1:
        return True
    return False

def issame2(begin, word): # zip 함수 !!!
    cnt= 0
    for b, w in zip(begin, word):
        if b==w:
            cnt+=1
    if cnt == len(word)-1:
        return True
    return False

def solution(begin, target, words):
    visited= [False for _ in range(len(words))]
    results= []
    def dfs(begin, target, cnt):
        if begin == target:
            results.append(cnt)
            return

        for idx, word in enumerate(words):
            if visited[idx] == False and issame1(begin, word) == True:
                visited[idx]= True
                dfs(word, target, cnt+1)
                visited[idx]= False
        return results

    dfs(begin, target, 0)
    if len(results)==0:
        results.append(0)
    return min(results)

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))