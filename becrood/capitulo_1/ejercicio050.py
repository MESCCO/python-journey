#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

A=int(input())
conjunto={61:"Brasilia",
          71:"Salvador",
          11:"Sao Paulo",
          32:"Juiz de Fora",
          19:"Campinas",
          27:"Vitoria",
          21:"Rio de Janeiro"}
if A in conjunto:
    print(conjunto[A])
else:
    print("DDD nao cadastrado")