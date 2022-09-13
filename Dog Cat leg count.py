# a=int(input("enter the dog  "))
# b=int(input("enter the cat  "))
# c=int(input("enter the leg  "))  
# d=a+b     
# e=d*c
# if e%4==0:
#     print("true")
# else:
#     print("false")
p=int(input())
for i in range(p):
     c,d,l=map(int,input().split())
     total=(c+d)*4
     if(c>(d*2)):
        min_legs=(c-(d*2)+d)*4
     else:
        min_legs=(d*4)
     if l%4==0 and l>=min_legs and l<=total:
         print("yes")
     else:
          print("no")