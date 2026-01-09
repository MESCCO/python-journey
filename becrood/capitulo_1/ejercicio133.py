#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
a=int(input())
b=int(input())
while a<0 or b<0:
    a=int(input())
    b=int(input())
if a>b:
    c=b
    b=a
    a=c
for i in range(a+1,b):
    if i%5==2 or i%5==3:
        print(i)
