#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

linea1=input().split()
linea2=input().split()
codigo1, cantidad1, precio1=int(linea1[0]), int(linea1[1]), float(linea1[2])
codigo2, cantidad2, precio2=int(linea2[0]), int(linea2[1]), float(linea2[2])
total=(precio1*cantidad1) + (precio2*cantidad2)
num="VALOR A PAGAR: R$ {:.2f}".format(total)
print(num)