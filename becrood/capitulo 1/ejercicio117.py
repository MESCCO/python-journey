#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

nota=[]
while True: 
    if len(nota)==2:
        break    
    else:
        n=float(input())
        if 0<=n<=10:
            nota.append(n)
        else:
            print("nota invalida")
print(f"media = {sum(nota)/2:.2f}")