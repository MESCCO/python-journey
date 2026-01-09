#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

n=int(input())
if 0<n<1000000:
    dato1=n//100
    dato2=(n%100)//50
    dato3=((n%100)%50)//20
    dato4=(((n%100)%50)%20)//10
    dato5=((((n%100)%50)%20)%10)//5
    dato6=(((((n%100)%50)%20)%10)%5)//2
    dato7=((((((n%100)%50)%20)%10)%5)%2)//1
print(n)           
print(dato1,"nota(s) de R$ 100,00")
print(dato2,"nota(s) de R$ 50,00")
print(dato3,"nota(s) de R$ 20,00")
print(dato4,"nota(s) de R$ 10,00")
print(dato5,"nota(s) de R$ 5,00")
print(dato6,"nota(s) de R$ 2,00")
print(dato7,"nota(s) de R$ 1,00")