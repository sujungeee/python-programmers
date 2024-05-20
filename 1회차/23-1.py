# 내가 짠 코드
def solution(genres, plays):
    answer = []
    genreDic= {}

    # 1. 장르의 총 재생 횟수 구하기
    for i in range(len(genres)):
        if genres[i] in genreDic:
            genreDic[genres[i]]+= plays[i]
        else:
            genreDic[genres[i]]= plays[i]

    # 2. 재생 횟수가 많은 장르부터
    for genre, count in sorted(genreDic.items(), key=lambda x: x[1], reverse=True):
        playDic= {}
        # 3. 장르의 고유 번호 정렬
        for i in range(len(genres)):
            if genres[i] == genre:
                playDic[i]= plays[i]
        top= sorted(playDic.items(),key=lambda x: (-x[1], x[0]))[:2]
        answer += [item[0] for item in top]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "dance"], [500, 600, 150, 800, 2500, 100]))