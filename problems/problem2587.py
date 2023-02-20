ary=[]
avg=0
minmax=0
middle=0
for i in range(5):
    ary.append(int(input()))
    if ary[i]<=0:quit()
    avg+=ary[i]
    if minmax<ary[i]:minmax=ary[i]
avg=int(avg/5)
# dev=[]
# for i in range(5):
#     dev.append((ary[i]-avg)**2)
#     if minmax>dev[i]:
#         minmax=dev[i]
#         middle=i
ary.sort()
print(avg)
print(ary[2])

'''
Can we get the median from the mean and variance?
'''