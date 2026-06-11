'''
a=int(input())
b=int(input())
sum=0
while a<=b:
    sum+=a
    a+=1
    print(sum)





a=int(input())
b=int(input())
if a>b: a,b=b,a
while b>=a:
    print (b, end="")
    b-=1
    print()



minimum=0
while True:
    num=int(input())
    if num=0:
        break
    if minimum=0 or minimum>num:
            minimum=num
print(minimum)
'''
'''
min1=int(input())
max1=int(input())
min2=int(input())
max2=int(input())
if min1>max1: min1,max1=max1,min1
if min2>max2: min2,max2=max2,min2
if min1>min2:
    min=min1
else:
    min=min2
if max1<max2:
    max=max1
else:
    max=max2
while min<=max:
    print (min)
    min+=1


num=int(input())
print(num%2 and "нечетное" or "четное")
'''
'''
a=int(input())
b=int(input())
if a>b: a,b=b,a
for i in range(a,b+1,1):
    print(i)
    
min=int(input())
max=int(input())
print((min+max)/2)


a=int(input())
b=int(input())
for i in range(a,b+1,3)
    print (i)
    
a=int(input())
b=int(input())
mult=1
for i in range (a,b+1)
    mult*=i
    print(i)
 '''

num=int(input())
maximum=num
for i in range(4):
    num=int(input())
    if maximum<num:
        maximum=num
print(maximum)



n=int(input("Введите цифры:"))
for i in range(n):
    num=int(input())
    if num%2=0:
        print(num)





