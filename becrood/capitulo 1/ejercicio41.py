#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

lista=[4,4.5,5,2,1.5]
x,y=map(int, input("").split())
precio=y*(lista[x-1])
print("Total: R$ "+f"{precio:.2f}")