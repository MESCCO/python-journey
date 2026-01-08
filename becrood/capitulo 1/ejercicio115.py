#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

while True:
    a,b=map(int,input().split())
    if a!=0 and b!=0:
        if a>0:
            if b>0:
                print("primeiro")
            else:
                print("quarto")
        else:
            if b>0:
                print("segundo")
            else:
                print("terceiro")
    else:
        break

