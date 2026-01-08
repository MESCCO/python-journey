#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

lista_Total=[]
while True:
    a,b=map(int,input().split())
    if a>0 and b>0:
        if a>b:
            c=b
            b=a
            a=c
        lista=[]
        for i in range(a,b+1):
            lista.append(i)
        lista_Total.append(lista)    
    else:
       break
for i in range(len(lista_Total)):
    print(*lista_Total[i],f"Sum={sum(lista_Total[i])}")       

