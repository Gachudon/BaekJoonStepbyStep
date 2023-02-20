'''
1:     2sec
2:ABC  3sec
3:DEF  4sec
4:GHI  5sec
5:JKL  6sec
6:MNO  7sec
7:PQRS 8sec
8:TUV  9sec
9:WXYZ 10sec
'''
dial={3:"ABC",4:"DEF",5:"GHI",6:"JKL",7:"MNO",8:"PQRS",9:"TUV",10:"WXYZ"}
apb=input()
apb=apb.upper()
time=0
for i in apb:
    for j in dial:
        if i in dial.get(j):
            time+=j
print(time)