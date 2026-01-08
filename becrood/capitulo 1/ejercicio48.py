#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

salario=float(input())
if salario>2000:
    aumento=0.04

elif 1200<salario:
    aumento=0.07
    
elif 800<salario:
    aumento=0.1
    
elif 400<salario:
    aumento=0.12

else:
    aumento=0.15
    
A=aumento*salario  + salario
B=aumento*salario
C=aumento*100
print(f"Novo salario: {A:.2f}")
print(f"Reajuste ganho: {B:.2f}")
print(f"Em percentual: {int(C)} %")