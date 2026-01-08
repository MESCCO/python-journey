#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197
gremio=0
inter=0
empates=0
while True:
    a,b=map(int,input().split())
    if a>b:
        inter+=1
    elif a==b:
        empates+=1
    else:
        gremio+=1
    
    print("Novo grenal (1-sim 2-nao)")
    m=int(input())
    while 1>m or m>2:
        print("Novo grenal (1-sim 2-nao)")
        m=int(input())
    
    if m==2:
        break
        
print(f"{inter+empates+gremio} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empates}")
if gremio>inter:
    print("Gremio venceu mais")
elif gremio==inter:
    print("Não houve vencedor")
else:
    print("Inter venceu mais")


    