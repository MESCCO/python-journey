#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n=int(input())
lista=[]
suma=0
sumas=0
for i in range(1,n+1):
    a=int(input())
    lista.append(a)
for i in lista:
    if i in range(10,20):
        suma+=1
    else:
        sumas+=1
print(suma,"in")
print(sumas,"out")