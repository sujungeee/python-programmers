# 내가 짠 코드 + 교재
def solution(enrolls, referral, sellers, amount):
    answer= {enroll: 0 for enroll in enrolls}

    pc= dict(zip(enrolls, referral))

    for i in range(len(sellers)):
        profit= amount[i]*100
        seller= sellers[i]

        while seller!= '-' and profit>0:
            answer[seller] += profit- profit//10
            seller= pc[seller]
            profit//= 10

    return [value for _, value in answer.items()]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#                ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#                ["sam", "emily", "jaimie", "edward"],
#                [2, 3, 5, 4]))