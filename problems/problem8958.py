number_of_case = int(input())
test_case =[]
for i in range(number_of_case):
    test_case.append(input())
    if len(test_case[i])>=80 or len(test_case[i])<=0:quit()


sum = [0]*number_of_case
for i in range(number_of_case):
    cnt=0
    for j in range(len(test_case[i])):
        if test_case[i][j]=='O':cnt+=1
        elif test_case[i][j]=='X':cnt=0
        else:break
        sum[i]+=cnt
    print(sum[i])