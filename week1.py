a = int(input(print("enter a: ")))
b = int(input(print("enter b: ")))
c = int(input(print("enter c: ")))

if a>0:
    x=a*b
else:
    x=a-b
if c%2==0:
    y = c + x
else:
    y = c - x
if y <0:
    y=-y
print(y)
    


