def LeerEntero(min,max,texto):
    N= int(input(texto))
    while N<min or N>max:
        print("Error...... ,Burro..... digete un numero entre",min,"y",max)
        N= int(input(texto))
    return N


