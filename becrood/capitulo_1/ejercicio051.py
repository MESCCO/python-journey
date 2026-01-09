#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

salario= float(input(""))
if salario>4500:
    impuesto=350 + (salario-4500)*0.28
    print(f"R$ {impuesto:.2f}")
elif salario>3000:
    impuesto=80 +(salario-3000)*0.18
    print(f"R$ {impuesto:.2f}")
elif salario>2000:
    impuesto= (salario-2000)*0.08
    print(f"R$ {impuesto:.2f}")
else:
    print("Isento")
