#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
n=int(input())
while n<0 or n>1000:
    n=int(input())
for i in range(1,n+1):
    k=i
    k2=i**2
    k3=i**3
    print(k,k2,k3)
    print(k,k2+1,k3+1)