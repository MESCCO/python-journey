#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

nombre = input("")
venta = float(input())
pago = float(input())
salario = pago*0.15 + venta
num ="TOTAL = R$ "+"{:.2f}".format(salario).strip()
print(num)