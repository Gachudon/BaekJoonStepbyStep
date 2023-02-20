import sys

n=int(sys.stdin.readline())
if n>500000 or n<1 or n%2==0:quit()
arr=[0]*n
avg=0
count_dict={}
max=-4000
min=4000
for i in range(n):
    arr[i]=int(sys.stdin.readline())
    if arr[i]>4000 or arr[i]<-4000:quit()
    avg+=arr[i]
    if arr[i] in count_dict: count_dict[arr[i]]+=1
    else:count_dict[arr[i]]=1
    if max<arr[i]:max=arr[i]
    if min>arr[i]:min=arr[i]
print(int(round(avg/n)))
arr.sort()
print(arr[int(n/2)])
count_list=sorted(count_dict.items(), key=lambda x:x[0])
count_list=sorted(count_list,key=lambda x:x[1],reverse=True)
# 사전의 value 값으로 정렬하는 방법은 sorted 함수를 사용합니다.
# sorted 함수는 key를 받을 수 있는데, 여기서 lambda식을 사용하여 튜블에서
# 1번째 index를 기준으로 정렬하는 것이지요.
if len(count_list)==1:print(count_list[0][0])
elif count_list[0][1]==count_list[1][1]:print(count_list[1][0])
else:print(count_list[0][0])
print(max-min)