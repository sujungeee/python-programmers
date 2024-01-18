# 리스트
list1 = [-3, 1, 5, 8, -2]

list1 = sorted(list1, key = abs)
print(list1) # [1, -2, -3, 5, 8]

list1 = sorted(list1, key = abs, reverse = True)
print(list1) # [8, 5, -3, -2, 1]

# 딕셔너리
dictNum = {"1":32, "2":12, "3":19, "4":3}

# 키에 대한 오름차순 정렬
dictResult= sorted(dictNum)
print(dictResult) # ['1', '2', '3', '4']

# 키에 대한 내림차순 정렬, items()를 적용하여 tuple 형태로 출력
dictResult= sorted(dictNum.items(), key = lambda x: x[0], reverse = True)
print(dictResult) # [('4', 3), ('3', 19), ('2', 12), ('1', 32)]

# 값에 대한 오름차순 정렬, items()를 적용하여 tuple 형태로 출력
dictResult = sorted(dictNum.items(), key = lambda x: x[1])
print(dictResult) # [('4', 3), ('2', 12), ('3', 19), ('1', 32)]

# 값에 대한 내림차순 정렬을 적용하여 키 값을 출력
dictResult = sorted(dictNum, key = lambda x: dictNum[x], reverse = True)
print(dictResult) # ['1', '3', '2', '4']

print(dictNum) # {'1': 32, '2': 12, '3': 19, '4': 3}

dict2= {}
dict2[0] = 1
dict2[1] = 2
dict2[2] = 2
print(dict2)

# 같은 값에 대해서는 작은 수의 키 먼저 출력됨
result= sorted(dict2, key=lambda x: dict2[x], reverse=True)
print(result)