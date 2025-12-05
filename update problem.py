#problem 1
n = int(input())
if n%2 == 0:
    print ("even")
else:
    print ("odd")
#problem 2
a = int(input())
b = int(input())
if  a>b :
    print (a-b)
else:
    print (a+b)
#problem 3
x = int(input())
y = int(input())
z = int(input())
if x>0:
    k = x*y
else:
    k = x-y
if z%2==0:
    print (k+z)
else:
    print (z-k)
if z<0:
    z = -z
#problem 4
t = int(input())
if t<0:
    print(-t)
else:
    print (t)




