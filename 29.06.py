'''
numbers=[2,5,134,-1,-4]
for i in numbers:
    if i<0:
        print(i)



numbers=[23,5,7,234,-12,-13]
for i in range(len(numbers)):
    if numbers[i]<0:
        numbers[i]*=-1
    print(numbers)



marks=[2,5,7,-1,-3]
for i in range(len(marks)//2):
    marks[i], marks(len(marks))
'''
'''
names=["Kate","John","Dasha"]
flag=True
for i in range (1,len(names)):
    if len(names[i])!=len(names[0]):
        flag=False
        break
print(flag)
'''
'''
student=["Kate","john","Ann"]
for i in student:
    if i[len(i)-1]="n":
print(i)
'''

'''
students=[[5,3,2],
          [4,4,5],
          [5,2,4]]
for i in range (len(students)):
    print(f"Студент{i+1}: ", end="")
    summa=0
    for j in students[i]:
        summa+=j
        print(j, end="")
    print("|", summa/len(students[i]))
 '''

students=[[5,3,2],
          [4,4,5],
          [5,2,4]]
for i in range(len(students)):
    summa=0
    for j in students[i]:
        summa+=j
        print(j, end="\t")
    print("|", summa)
    print("---------------")
    result=0
for i in range(len(students[0])):
    summa=0
    for j in range (len(students)):
        summa+=students[j][i]
    print(summa,end="\t")
    result+=summa
print("|", result, end="")