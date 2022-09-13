# import re

# class Main():
#     def _init_(self):
#         self.n = int(input())
        
#         for i in range(self.n):
#             self.s = input()
#             print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
# if _name_ == '_main_':
#     obj = Main()


import string


count=int(input().strip())
for _ in range(count):
    ans=False              
    try:
        string=input().strip()
        number=float(string)
        ans=True    
        number1=int(string)
        ans=False              
    except:
        pass               
    print(ans)