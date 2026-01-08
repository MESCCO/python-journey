#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n= int(input())
lista=[]
for i in range(1,n+1):
    a,b,c=map(float,input().split())
    date=(a*2+b*3+c*5)/10
    lista.append(date)
for i in lista:
    print(f"{i:.1f}")




    