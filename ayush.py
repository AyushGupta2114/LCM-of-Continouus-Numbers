n=int(input())
i=1
first=2254
while(i==1):
    count=0
    for j in range(2,n+1):
        if(first%j!=0):
            break
        else:
            count+=1
    if(count==n-1):
        i=0
    first+=1
print(first-1)
