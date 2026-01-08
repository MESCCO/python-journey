#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

lista=[]
contador=0
while contador<10: 
    a=int(input())
    if a>0:
        lista.append(a)
        contador+=1
mayor,pos=lista[0],0
for i in range(1,len(lista)):
    if lista[i]>mayor:
        mayor,pos=lista[i],i
print(mayor)
print(pos+1)


