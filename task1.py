n=int(input())
if n==1:
    print("Время начала урока: 8:30 ","Время окончания урока: 9:15")
else:
    x1=(510+(55*(n-1)-10))//60
    x2=(510+(55*n-10))//60
    y1=(510+(55*(n-1)-10))%60
    y2=(510+(55*n-10))%60
    print("Время начала урока: ",x1,":",y1,"Время окончания урока: ",x2,":",y2)
