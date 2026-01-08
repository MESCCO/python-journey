#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a, b, c=map(int, input().split())
MaiorAB=m=(a+b+abs(a-b))/2
MaiorAC=n=(a+c+abs(a-c))/2
MaiorMN=(m+n+abs(m-n))/2
print("{:.0f}".format(MaiorMN).strip(),"eh o maior")
