#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
alcohol=0
gasolina=0
diesel=0
while True:
    n=int(input())
    while n<0 or n>4:
        n=int(input())

    if n==1:
        alcohol+=1
    elif n==2:
        gasolina+=1
    elif n==3:
        diesel+=1
    else:
        break
print("MUITO OBRIGADO")
print(f"Alcool:",alcohol)
print(f"Gasolina:",gasolina)
print(f"Diesel:",diesel)


