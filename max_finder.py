n=int(input())
list=map(int,input().split())
max=0
for i in list:
    if i>max:
        max=i
print(max)