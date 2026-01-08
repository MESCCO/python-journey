#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

while True:
    a, b = map(int, input().split())
    if a == b:
        break
    if a > b:
        print("Decrescente")
    else:
        print("Crescente")
