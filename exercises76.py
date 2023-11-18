n=int(input('Enter an integer (2 or greater): '))
factor=2
while factor<=n:
    if n%factor==0: 
        print(factor)
        n=n//factor
    else: 
        factor=factor+1
    