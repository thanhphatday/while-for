total = 0
count = 0
value = int(input("Enter a value: "))
if value == 0:
    print("Error: No values were entered.")
else:
    while value != 0:
        total += value
        count += 1
        value = int(input("Enter a value: "))
    average = total / count
    print("The average of the values entered is ", average)