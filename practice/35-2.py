def solution(n, words):
    tmp = words[0][0] # 맨 앞 words의 첫 글자
    used_word= set()

    for idx, word in enumerate(words):
        if (word in used_word) or word[0] != tmp:
            return [(idx%n)+1, (idx//n)+1]
        else:
            tmp = word[-1]
            used_word.add(word)
    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))