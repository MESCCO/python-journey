#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

lista=[]
for i in range(1,6):
    a= int(input())
    lista.append(a)
par=0
impar=0
posi=0
nega=0
for i in lista:
    if i%2==0:
        par+=1
    else:
        impar+=1
    if i>0:
        posi+=1
    else:
        if i<0:
            nega+=1
print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(posi,"valor(es) positivo(s)")
print(nega,"valor(es) negativos(s)")
