print(" *****Temperature Converter*****")
print("|-------------------------------|")
print("| \tCelsius\t| Fahrenheit\t|")
print("|-------------------------------|")

for i in range(101):
        if(i%10==0):
            f=(i*(9/5))+32
            print("|\t",i,"\t|\t",f,"\t|")
print("|-------------------------------|")

