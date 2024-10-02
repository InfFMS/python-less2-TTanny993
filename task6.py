for i in range (100,1000):
    a=i%10*100
    b=i%100//10*10
    c=i//100
    m=a**3+b**3+c**3
    if i==m:
        print(i)