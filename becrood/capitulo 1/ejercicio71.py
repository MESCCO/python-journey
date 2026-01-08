#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a=int(input())
b=int(input())
lista=[]
if a>b:
    for i in range(b+1,a):
        if i%2==1:
            lista.append(i)
elif b>a:
    for i in range(a+1,b):
        if i%2==1:
            lista.append(i)
else:
    lista=[]
print(sum(lista))
