#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
n=int(input())
while n<0:
    n=int(input())
m=1
for i in range(n):
    for i in range(m,m+3):
        print( i, end=" ")
    print("PUM")
    m+=4
