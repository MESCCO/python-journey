#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b,c=map(float,input().split())
while (0>=a)or (0>=b) or (0>=c):
    a,b,c=map(float, input().split())
lista=[a,b,c]
lista.sort()
a=lista[2] 
b=lista[1] 
c=lista[0]
if a<b+c and b<a+c and c<b+a:
    if a**2==b**2 +c**2:
        print("TRIANGULO RETANGULO")
    elif a**2>b**2 +c**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif a==b or a==c or b==c:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")