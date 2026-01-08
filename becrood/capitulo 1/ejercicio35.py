#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

num = list(map(int, input().split()))
A, B, C, D = num
if B>C and D>A and C+D>A+B and 0<C and 0<D and A%2==0:
 print("Valores aceitos")
else:
 print("Valores nao aceitos")   