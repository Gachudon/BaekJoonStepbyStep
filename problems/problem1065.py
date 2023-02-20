'''
자릿수의 등차수열에서 가장 큰 값은 0-9 혹은 9-0
왜 빼냐? 두 수의 차이를 구해야하기 때문.
1~99까지는 등차수열이다. 왜? 1~9는 수열의 원소가 1개 뿐이고, 10~99까지 수열의 원소가 2개뿐이라 직관적으로 등차수열로 볼 수 있다.
100~999는 어떻게 계산할까?
첫째 자리와 둘째 자리를 뺀다. 둘째 자리와 셋째 자리를 빼서 그 두값이 같다면 등차수열이다.
'''

n = int(input())
if n>1000 or n<1:quit()
elif n<100:
    print(n)
    quit()
else:
    cnt=0
    for i in range(100,n+1):
        tmp=10
        tmp1=set()
        for num in str(i):
            if tmp>9:tmp=int(num)
            else:
                tmp1.add(tmp-int(num))
                tmp=int(num)
        if len(tmp1) == 1:cnt+=1
    print(cnt+99)
        