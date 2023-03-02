numeroIngresadoPorElUsuario = 0
numeroAEncontrar = 7

while numeroIngresadoPorElUsuario != numeroAEncontrar:
    numeroIngresadoPorElUsuario = int(input("Adivina cuál número está registrado como variable: "))

    if numeroIngresadoPorElUsuario < numeroAEncontrar:
        print("El número que estás buscando es mayor al que ingresaste")

    elif numeroIngresadoPorElUsuario > numeroAEncontrar:
        print("El número que estás buscando es menor al que ingresaste")
    
    else:
        print("El número que ingresaste es correcto")
