a,b=map(int,input().split())
if a<=0 or b<=0:quit()
print("%d"%(a+b))
# print (type(a),type(b))
# print(type(a+b))

'''
C의 경우 값이 2147483647 보다 클 경우 정수형 계산이 불가능하다.
하지만 파이썬의 경우 정수형 범위에 제한이 없으므로 계산이 가능하다.
'''