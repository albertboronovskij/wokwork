n=input('введите н ')
a=[1,2,3,4,5,6,6,7,8,9]
print(a)
print(n)
count=0
i=0
while i<len(a) :
    if a[i]==int(n):
        count=count+1
        i=i+1
    else:
        i=i+1
        
print('->',count)