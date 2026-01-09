#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b=map(float,input("").split())
if a>0 and b>0:
    print("Q1")
elif a<0 and b>0: 
    print("Q2")
elif a<0 and b<0:
    print("Q3")
elif a>0 and b<0:
    print("Q4")
elif a==0 and b!=0:
    print("Eixo Y")
elif b==0 and a!=0:
    print("Eixo X")
else:
    print("Origem")