#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

A,B,C =map(float,input().split())
triangulo=A*C/2
circulo=3.14159*C**2
trapezio=((A+B)*C)/2
cuadrado=B**2
rectangulo=A*B
print("TRIANGULO: "+"{:.3f}".format(triangulo).strip())
print("CIRCULO: "+"{:.3f}".format(circulo).strip())
print("TRAPEZIO: "+"{:.3f}".format(trapezio).strip())
print("QUADRADO: "+"{:.3f}".format(cuadrado).strip())
print("RETANGULO: "+"{:.3f}".format(rectangulo).strip())