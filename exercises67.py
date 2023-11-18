S=0
while True:
    age=input('The age of the guest: ')
    if age=='': break
    age=int(age)
    if age<=2: S=S
    elif 3<=age<=12: S=S+14.00
    elif age>=65: S=S+18.00
    else: S=S+23.00
print('$',S,sep='')
    
    

