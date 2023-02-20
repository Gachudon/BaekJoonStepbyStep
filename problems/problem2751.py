# def merge_sort(ary):
#     if len(ary)<2:
#         return ary
    
#     mid = len(ary)//2
#     low_arr= merge_sort(ary[:mid])
#     high_arr=merge_sort(ary[mid:])

#     merged_arr=[]
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l+=1
#         else:
#             merged_arr.append(high_arr[h])
#             h+=1
#     merged_arr+=low_arr[l:]
#     merged_arr+=high_arr[h:]
#     return merged_arr

# n=int(input())
# if n >1000000 or n<1:quit()
# arr=[]
# for i in range(n):
#     tmp = int(sys.stdin.readline())
#     if tmp in arr or tmp>1000000 or tmp<-1000000:quit()
#     arr.append(tmp)
# arr.sort()
# result=merge_sort(arr)

# count_dict={}

# for num in arr:
#     if num in count_dict:
#         count_dict[num]+=1

#     else:
#         count_dict[num]=1

# result=[]

# for num in range(max(arr)+1):
#     while num in count_dict and count_dict[num] !=0:
#         result.append(num)
#         count_dict[num]-=1

# for i in arr:
#     print(i)
import sys

n = int(input())
num=[]
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)