print('Original price\tDiscount amount\tNew price')
i=4.95
while i<=24.95:
    d_a=round(0.6*i,2)
    n_p=round(i-d_a,2)
    print(f'${i}\t\t${d_a}\t\t${n_p}')
    i=i+5