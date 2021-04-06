"""
    1.两个数的求和
    A = (input().split()) 
    print(A)
    print((int(A[0])+int(A[1])))
    """
"""2.前n个数相加的和
N = int(input(f"输入一个数："))
i = 0
s = 0
while (i<=N):
    s += i
    i+=1
print(f"前N个数的和为：{s}")
"""
"""3.圆的面积
PI = 3.1415926
R = int(input(f"圆的半径："))
print( f"圆的面积为:{ PI*R*R}")
"""

#斐波那契函数 Fn= Fn-1+Fn-2
"""
n = int(input())
F1 = 1
F2 = 1
i = 1
while (i<=n):
    if i<=3:
        F3=1
    elif   i<=n:
        F3 = F1 +F2
        F2 = F3
        F1 = F2
    i += 1
print(i)
print(F3)
print(F3%1007)
"""
#判断是否为瑞年
"""
year = int(input(f"年份为："))
P1 = year%4
P2 = year%100
P3 = year%400
if (P1==0 and P2!=0) :
    print(f"{year}是闰年")

elif P3==0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
"""
#01子串
"""
for i in range(32):
    print(bin(i)[2:].zfill(5))
#range函数的取值方式  
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)

for i in range(20):
    print(bin(i)[2:].zfill(5))
"""
"""
#  字母图形
list1 = input().split()
list2 = []
#将字符转化为数字
for i in range(len(list1)):
    list1[i]=int(list1[i])
#生成顺序字符串
for i in range(list1[0]):
    for j in range(list1[1]):
        if i>j:
            list2.append(chr(ord('A')+i-j))
        else:
            list2.append(chr(ord('A')+j-i)) 
            
        print(list2[k],end='')
    print()
    #print('\n') #注意这是两个换行
    list2=[]
"""
for i in range(2020):
    