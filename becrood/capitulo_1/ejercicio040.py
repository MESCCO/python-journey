#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b,c,d=map(float,input("").split())
promedio=(a*2 + b*3+c*4+d*1)/10
if promedio>=5:
    if promedio>7:
        print(f"Media: {promedio:.1f}")
        print("Aluno aprovado.")
    else:
        print(f"Media: {promedio:.1f}")
        print("Aluno em exame.")
        susti=float(input(""))
        mf=(susti+promedio)/2 
        print(f"Nota do exame: {susti:.1f}")
        if mf <=4.9:
            print("Aluno reprovado.")
            print(f"Media final: {mf:.1f}")
        else:
            print("Aluno aprovado.")
            print(f"Media final: {mf:.1f}")
else:
    print(f"Media: {promedio:.1f}")
    print("Aluno reprovado.")