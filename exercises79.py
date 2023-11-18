import random
max=random.randint(1,100)
i=1
count=0
print(max)
while i<=100:
  x=random.randint(1,100)
  print(x)
  if x>max:
    max=x
    print('=>Update')
    count=count+1
  i=i+1
print('The maximun value found was=',max)
print('The maximun value was updated',count,'times')
    