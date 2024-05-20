def calculate(x,y,dir):
    if dir=='U':
        y+=1
    elif dir=='D':
        y-=1
    elif dir=='L':
        x-=1
    elif dir=='R':
        x+=1
    return x,y

def is_valid(ux,uy):
    return -5<=ux<=5 and -5<=uy<=5

def solution(dirs):
    ans= set()
    x,y=0,0
    for dir in dirs:
        ux,uy= calculate(x,y,dir)
        if not is_valid(ux,uy):
            continue
        ans.add((x,y,ux,uy))
        ans.add((ux,uy,x,y))
        x,y= ux,uy
    return int(len(ans)/2)

print(solution('ULURRDLLU'))