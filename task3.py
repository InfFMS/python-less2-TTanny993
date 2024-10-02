n=int(input())
i=n%10
if (n>4) and (n<21):
    print('Вам',n,'лет.')
else:
    if i==1:
        print('Вам',n,'год')
    elif i < 5:
        print('Вам',n,'года')
    else:
        print('Вам',n,'лет')