#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

rango=0
contador=0
while rango<6:
    a=float(input())
    if a>0:
        contador+=1
    else:
        contador+=0
    rango+=1
print(f"{contador} valores positivos")