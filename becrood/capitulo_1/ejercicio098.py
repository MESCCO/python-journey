#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

p=0
while p<=2:
    if p==0 or p==1 or p>=1.9:
        for i in range(1,4):
            print(f"I={p:.0f} J={p+i:.0f}")
    else:
        for i in range(1,4):
            print(f"I={p:.1f} J={p+i:.1f}")
    p+=0.2