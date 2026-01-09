#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if (a==0 and b==0)or(b==0):
        print("divisao impossivel")
    else:
        print(f"{a/b:.1f}")
