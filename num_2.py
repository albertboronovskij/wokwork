
n=(input('введите n '))
counter=1
b=[]
i=0
j=0
while i<int(n) :
    b.append(counter)
    i=i+1
    counter=counter+1
print (b) 
m=(input('введите нужное вам число  '))
if 0<int(m)<=int(n)+1:
     print('самое близкое к вашему числу это ',m)
elif int(m)>len(n):
    print('самое близкое к вашему числу это ',max(b))
elif int(m)<b[0] :
    print ('самое близкое к вашему числу это ',b[0])

    

 

