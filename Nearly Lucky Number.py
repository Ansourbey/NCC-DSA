n = input() 
count = 0
for i in n:
    if i == '4' or i == '7':
        count += 1
is_lucky = True
for i in str(count):
    if i != '4' and i != '7':
        is_lucky = False
        break
if count > 0 and is_lucky:
    print("YES")
else:
    print("NO")