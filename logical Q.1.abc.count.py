

# s=float(input("enter the number   "))
# b=input("enter the simble   ")
# if b =="+" :
#     print("true")
# else:
#     print("false")
    
# def fun(p):
#     if p==float:
#         print("true")
#     else:
#         print("false")
# p=input("enter the number   ")
# fun(p)

# str=input("enter your name.......")
# i=0

# while i<len(str):
#     if str[i]=="a":
#         print(str.upper())
#         break
#     elif str[i]=="A":
#         print(str.lower())
#         # break
#     i=i+1
  

 


# str="aabbbccde"
# i=0
# a=[]
# p=[]
# k=[]
# while i<len(str):
#     if str[i]  in "b" :
#         a.append(str[i])
#     if str[i]  in "a" :
#         p.append(str[i])
#     if str[i]  in "c" :
#         k.append(str[i])
#     i+=1
# print("b",len(a))
# print("a",len(p))
# print("c",len(k))



str="aabbbccde"
a=[]
p=[]
k=[]
for i in range(0,9):
    if str[i]  in "b" :
        a.append(str[i])
    if str[i]  in "a" :
        p.append(str[i])
    if str[i]  in "c" :
        k.append(str[i])
print("b",len(a))
print("a",len(p))
print("c",len(k))