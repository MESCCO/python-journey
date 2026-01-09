#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

N=float(input())
if 0<=N and N<=1000000.00 :
    dato1=N//100
    dato2=(N%100)//50
    dato3=((N%100)%50)//20
    dato4=(((N%100)%50)%20)//10
    dato5=((((N%100)%50)%20)%10)//5
    dato6=(((((N%100)%50)%20)%10)%5)//2
    dato7=((((((N%100)%50)%20)%10)%5)%2)//1
    dato8=(N-(N//1))//0.50
    dato9=((N-(N//1))%0.50)//0.25
    dato10=(((N-(N//1))%0.50)%0.25)//0.10
    dato11=((((N-(N//1))%0.50)%0.25)%0.10)//0.05
    dato12=(((((N-(N//1))%0.50)%0.25)%0.10)%0.05)//0.01
    print("NOTAS:")
    print(int(dato1),"nota(s) de R$ 100.00")
    print(int(dato2),"nota(s) de R$ 50.00")
    print(int(dato3),"nota(s) de R$ 20.00")
    print(int(dato4),"nota(s) de R$ 10.00")
    print(int(dato5),"nota(s) de R$ 5.00")
    print(int(dato6),"nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(int(dato7),"moeda(s) de R$ 1.00")
    print(int(dato8),"moeda(s) de R$ 0.50")
    print(int(dato9),"moeda(s) de R$ 0.25")
    print(int(dato10),"moeda(s) de R$ 0.10")
    print(int(dato11),"moeda(s) de R$ 0.05")
    print(int(dato12),"moeda(s) de R$ 0.01")
else:
    print("error")
    