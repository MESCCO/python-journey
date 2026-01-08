#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
a=int(input())
b=int(input())
contador=0
if a>b:
    c=b
    b=a
    a=c
for i in range(a,b+1):
    if i%13!=0:
        contador+=i
print(contador)