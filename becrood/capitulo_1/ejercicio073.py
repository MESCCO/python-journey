#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n= int(input())
while (-10)**7>=n or n>=(10)**7:
    n =int(input)
lista=[]
for i in range(1,n+1):
    a=int(input())
    lista.append(a)
for a in lista:
    if a>0:
        if a%2==1:
            print("ODD POSITIVE")
        else:
            print("EVEN POSITIVE")
    elif a<0:
        if a%2==-1:
            print("ODD NEGATIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        print("NULL")   
