new_base = 2 
num = int(input("Enter a non-negative integer: "))
result = ""
q = num 
r = q % new_base
result = str(r) + result
q = q // new_base
while q > 0:
  r = q % new_base
  result = str(r) + result
  q = q // new_base

print(f"{num} in Decimal is {result} in Binary")