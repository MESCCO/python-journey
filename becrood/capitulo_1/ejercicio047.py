#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

a,c,b,d=map(int,input("").split())
while not (0 <= a <= 24 and 0 <= b <= 24 and 0 <= c <= 60 and 0 <= d <= 60):
    a,c,b,d=map(int,input("").split())   
if a<b:
    hora=(b-a)
elif a==b:
    if c>=d:
        hora=24
    else:
        hora=0
    
else:
    hora=(b+24)-a
    
if c<=d:
    minuto=d-c
else:
     minuto=(d+60)-c
     hora=hora-1

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")