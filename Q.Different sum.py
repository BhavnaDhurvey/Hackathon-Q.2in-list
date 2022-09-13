a=int(input())
b=int(input())
sum=0
sum1=0
i=1
while i<=b:
    if i%a==0:
        sum=sum+i
    else: 
        sum1=sum1+i
    i+=1

c=sum1-sum       
print(c)