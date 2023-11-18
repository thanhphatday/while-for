pi=3
a=1
b=2
for i in range(1,16,1):
    pi=pi+a*(4/(b*(b+1)*(b+2)))
    a=a*(-1)
    b=b+2
    print('Approximation',i,'=',pi)