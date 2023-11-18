b=input("Enter 8 bits: ")
while b!="":
    if b.count("0") + b.count("1") !=8 or len(b)!=8:
        print("That wasn't 8 bits... Try again")
    else:
        h=b.count("1")
        if h%2==0:
         print("The parity bit should be 0")
        else:
         print("The parity bit should be 1")
    b=input("Enter 8 bits: ")