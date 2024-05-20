# 프로그래머스 다른 사람 코드
# https://school.programmers.co.kr/learn/courses/30/lessons/42579/solution_groups?language=python3
def solution(genres, plays):
    answer = []
    dic = {} # 키: 장르, 값: 총 재생 횟수
    album_list = [] # album(장르, 재생횟수, 고유 번호)
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    # 총 재생 횟수가 많은 장르부터 정렬
    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    # 재생 횟수가 많은 앨범부터 정렬
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0: # 장르가 다 없어질 때까지
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track
        
    # 객체 간의 비교를 위한 메소드, play를 기준으로 비교 진행
    # sorted() 할 때 밑을 참고
    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play


print(solution(["classic", "pop", "classic", "classic", "pop", "dance"], [500, 600, 150, 800, 2500, 100]))