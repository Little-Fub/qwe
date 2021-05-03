# 打印三角形图样
n=int(input('请输入整数：'))
for i in range(n):
    print('*'*i,end='\n')
print('------'*5)
for i in range(0,n):
    print(' '*(n-i),'*'*i,end='\n')
print('------'*5)
import math
i=1
medium=math.ceil(n/2)
for raw in range(int(medium-1),0,-1):
    print(' '*raw,'*'*(2*i-1),end='\n')
    i+=1
