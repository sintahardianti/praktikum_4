print("program mengurutkan data")
a = int(input("bilangan ke-1: "))
b = int(input("bilangan ke-2: "))
c = int(input("bilangan ke-3: "))

if a>b and a>c:
        if b>c:
            print("urutan bilangan: " ,c, b, a)
        else:
            print("urutan bilangan: " ,b, c, a)
elif b>a and b>c:
        if a>c:
            print("urutan bilangan: " ,c, a, b)
        else:
            print("urutan bilangan: " ,a, c, b)
else:
    if a>b:
            print("urutan bilangan: " ,b, a, c)
    else:
            print("urutan bilangan: " ,a, b, c)
