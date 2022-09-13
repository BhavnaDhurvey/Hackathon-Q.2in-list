list = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
poss_count=0
nag_count = 0
i=0
while i<len(list):
    if list[i] >= 0:
        poss_count += 1
    else:
        nag_count=nag_count+list[i]
    i=i+1
print("possitive numbers in the list: ", poss_count)
print("nagetive numbers in the list: ",nag_count)




# output=[10,-65]
# possitivi count=10
# nagetive sum=-65

