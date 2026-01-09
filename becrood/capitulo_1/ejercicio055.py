#UNIVERSIDAD DE SAN ANTONIO ABAB DEL CUSCO
#ALUMNO: TRISANO MESCCO CONDE
#CODIGO: 246197

dia_i=int(input().split()[1])
hh1,mm1,ss1=map(int,input().split(" : "))
dia_f=int(input().split()[1])
hh2,mm2,ss2=map(int,input().split(" : "))

if ss2<ss1:
    mm2-=1
    ss2+=60
if mm2<mm1:
    hh2-=1
    mm2+=60
if hh2<hh1:
    dia_f-=1
    hh2+=24

if dia_i<=dia_f:
    segundo=ss2-ss1
    minuto=mm2-mm1
    hora=hh2-hh1
    dia=dia_f-dia_i
print(dia,"dia(s)")
print(hora,"hora(s)")
print(minuto,"minuto(s)")
print(segundo,"segundo(s)")