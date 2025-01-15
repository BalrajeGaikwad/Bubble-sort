"""def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp

num=[3,6,4,1,7]
sort(num)
print(num)
"""


"""num=[3,6,4,1,7]
for i in range(len(num)-1,0,-1):
    for j in range(i):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp

print(num)
"""



num=[5,6,8,2,4,5,6,7]
for i in range(len(num)-1,0,-1):
    for j in range(i):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp

print(num)