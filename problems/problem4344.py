c = int(input())
student=[]
student.append(list())
student[0].append(1)
rate = []
for i in range(c):
    avg=0
    tmp=list(map(int,input().split()))
    n = tmp[0]
    student.append(list())
    for j in range(1,len(tmp)):
        student[i].append(tmp[j])
    for j in range(n):
        avg += student[i][j]
    avg/=n
    cnt=0
    for j in range(n):
        if(avg<student[i][j]):cnt+=1
    rate.append(cnt/n*100)
for i in range(c):
    print("%.3f%%"%rate[i])