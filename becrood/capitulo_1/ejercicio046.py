#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,b=map(int,input("").split())
while a<0 or b<0 or a>24 or b>24:
    a,b=map(int,input("").split())   
if a<b:
    juego=(b-a)
elif a==b:
    juego=24
    
else:
    juego=(b+24)-a
print(f"O JOGO DUROU {juego} HORA(S)")