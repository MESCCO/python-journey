#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

P1=input().split()
P2=input().split()
X1, Y1=float(P1[0]),float(P1[1])
X2, Y2=float(P2[0]),float(P2[1])
distancia= ((X2-X1)**2 + (Y2-Y1)**2)**0.5
print("{:.4f}".format(distancia).strip())