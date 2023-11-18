n=str(input(''))
palindrome=True
i=1
while i<=(len(n)//2+1):    
    if n[i]==n[-i-1]: palindrome=True
    else: palindrome=False
    i=i+1
if palindrome==True: print(n,'is palindrome')
else: print(n,'is not palindrome')