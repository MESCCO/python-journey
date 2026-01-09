#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

numeros=input().split()
A, B, C=float(numeros[0]), float(numeros[1]), float(numeros[2])
#ecuacion dada es AX**2 + BX + C
discriminate= (B**2) - 4*(A)*(C)
if discriminate >= 0 and A!=0 :
    raiz1= (-B+(discriminate)**0.5)/(2*A)
    raiz2= (-B-(discriminate)**0.5)/(2*A)
    print("R1 = "+"{:.5f}".format(raiz1).strip())
    print("R2 = "+"{:.5f}".format(raiz2).strip())
else:
    print("Impossivel calcular")
