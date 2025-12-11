n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if (b<a<c) or (c<a<b):
        medium = a
    elif (a<b<c) or (c<b<a):
        medium = b
    else:
        medium = c
    print(medium)
