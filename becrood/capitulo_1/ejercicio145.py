#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b = map(int, input().split())
contador = 0
if 1<a<20 and a<b<100000:
    for i in range (1,b+1):
        contador+=1
        if a==contador:
            print(i)
            contador=0
        else:
            print(i,end=" ")

    