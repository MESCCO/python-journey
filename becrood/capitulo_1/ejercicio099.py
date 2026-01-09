#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n= int(input())
lista=[]
for k in range(n):
    a,b=map(int,input().split())
    if a-b!=0:
        suma=0
        if a>b:
            c=b
            b=a
            a=c
        for i in range(a+1,b):
            if i%2==1:
                suma+=i
        lista.append(suma)
    else:
        lista.append(0)
for i in lista:
    print(i)
        