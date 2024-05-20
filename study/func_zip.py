a= ['Alice', 'Bob']
b= [True, False, True]
print(list(zip(a,b)))
arr= []
for items in zip(a,b):
    arr.append(list(items))

print(arr)