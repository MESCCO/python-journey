#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n=int(input())
conejo=0
rata=0
sapo=0
for i in range(1,n+1):
    entrada=input().split()
    a=int(entrada[0])
    b=entrada[1]
    if b=="C":
        conejo+=a
    elif b=="R":
        rata+=a
    else:
        sapo+=a
total=conejo+sapo+rata
print(f"Total: {conejo+rata+sapo} cobaias")
print(f"Total de coelhos: {conejo}")
print(f"Total de ratos: {rata}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {conejo/total*100:.2f} %")
print(f"Percentual de ratos: {rata/total*100:.2f} %")
print(f"Percentual de sapos: {sapo/total*100:.2f} %")


        
        


