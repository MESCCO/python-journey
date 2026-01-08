#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

m=1
nota=[]
while m==1:
    n=float(input())
    if 0<=n<=10:
            nota.append(n)
    else:
            print("nota invalida")
    if len(nota)==2:
        print(f"media = {sum(nota)/2:.2f}")
        print("novo calculo (1-sim 2-nao)")
        m=int(input())
        while 1>m or m>2:
             print("novo calculo (1-sim 2-nao)")
             m=int(input())
        nota=[]   
    
    