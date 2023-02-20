from sys import stdin
input=stdin.readline
'''
코드 출처: https://pacific-ocean.tistory.com/230
문자열로 입력받은 뒤 for문을 통해 (,),[,], 그러니까 괄호들을 찾는다.
여는 괄호를 찾았을 땐 스택에 여는 괄호를 그대로 넣어준다.
닫는 괄호를 찾았을 땐 스택이 비었는 지, 스택의 마지막이 자기자신과 짝이 맞는 지
검사를 해주어 스택을 비워나간다. 만약 닫는 괄호를 찾았을 때 스택이 비워져 있거나
마지막이 짝이 안 맞는다면 temp를 False로 바꿔주고 break해준다. 마지막에 temp가
True이거나 스택이 비워져 있으면 yes를 출력해주고 그렇지 않으면 no를 출력해준다.
'''
while True:
    s=input().rstrip()
    if s=='.':
        break
    stk=[]
    temp=True
    for i in s:
        if i=='('or i=='[':
            stk.append(i)
        elif i==')':
            if not stk or stk[-1]=='[':
                temp=False
                break
            elif stk[-1]=='(':
                stk.pop()
        elif i==']':
            if not stk or stk[-1]=='(':
                temp=False
                break
            elif stk[-1]=='[':
                stk.pop()
    if temp and not stk:
        print('yes')
    else:
        print('no')

# 참조: https://somjang.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack
# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def push(self,data):
#         self.stack.append(data)

#     def pop(self):
#         pop_object = None
#         if not self.isEmpty():
#             pop_object=self.stack.pop()
        
#         return pop_object
#     def top(self):
#         top_object=None
#         if not self.isEmpty():
#             top_object=self.stack[-1]
        
#         return top_object
    
#     def isEmpty(self):
#         is_empty=False
#         if len(self.stack)==0:
#             is_empty=True

#         return is_empty
    
#     def getStack(self):
#         get_stack=self.stack
#         return get_stack
    
#     def clear(self):
#         self.stack=[]

# stack=Stack()

# ans=[]
# while(True):
#     s=input().rstrip()
#     if s=='.':break
#     is_unbalance=False
#     for i in s:
#         if i=='(' or i=='[':
#             stack.push(i)
#         elif i==')':
#             if stack.isEmpty():
#                 ans.append('no')
#                 is_unbalance=True
#                 break
#             if stack.top()=='[':
#                 ans.append('no')
#                 is_unbalance=True
#                 break
#             stack.pop()
#         elif i == ']':
#             if stack.isEmpty():
#                 ans.append('no')
#                 is_unbalance=True
#                 break
#             if stack.top()=='(':
#                 ans.append('no')
#                 is_unbalance=True
#                 break
#             stack.pop()
#     if is_unbalance:
#         stack.clear()
#         continue
#     if stack.isEmpty:ans.append('yes')
#     else:
#         stack.clear()
#         ans.append('no')

# for i in ans:
#     print(i)