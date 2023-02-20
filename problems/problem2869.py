# a, b, v = map(int,input().split())
# c = v%(a-b)
# if c==0:
#     print(int(v/(a-b)))
# else:
#     v-=c
#     print(int(v/(a-b))+1)

'''
코드 출처: https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4
우리는 k,즉 일수를 최소화시켜야 한다.
따라서 k는 (v-b)/(a-b) 혹은 (v-b)//(a-b)+1이다.
답이 두개인 경우는 (v-b)/(a-b)가 분수인 경우가 있기 때문이다.
예를 들어 (v-b)/(a-b)가 4.0인 경우 k는 4이지만,
(v-b)/(a-b)가 4.1인 경우 k는 5이다(k는 '일수'다. 즉 4.1일은 없다).
따라서 k=(v-b)/(a-b)로 두고, int(k)와 k가 같다면 k는 (v-b)/(a-b),
다르다면 k는 (v-b)/(a-b)+1이다.
'''

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)