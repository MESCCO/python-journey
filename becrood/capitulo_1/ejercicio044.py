#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b=map(int, input("").split())
if (a%b==0) or (b%a==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")