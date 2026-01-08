#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

lista=[]
pro=0
for i in range(1,7):
    a=float(input())
    if a>0:
        pro+=1
        lista.append(a)
print(pro,"valores positivos")
print(f"{sum(lista)/len(lista):.1f}")  