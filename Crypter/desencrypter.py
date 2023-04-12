def descifrado_cesar(texto_encriptado, desplazamiento):
    resultado = ""
    # Iteramos a través de cada caracter en el texto encriptado
    for caracter in texto_encriptado:
        # Convertimos el caracter a su valor ASCII
        ascii_valor = ord(caracter)
        # Aplicamos el desplazamiento inverso al valor ASCII
        nuevo_ascii_valor = ascii_valor - desplazamiento
        # Verificamos si el caracter es una letra mayúscula
        if caracter.isupper():
            # Si el valor ASCII desplazado es mayor que Z (90),
            # comenzamos desde A (65) de nuevo
            if nuevo_ascii_valor < 65:
                nuevo_ascii_valor = nuevo_ascii_valor + 26
            # Si el valor ASCII desplazado es menor que A (65),
            # comenzamos desde Z (90) de nuevo
            elif nuevo_ascii_valor > 90:
                nuevo_ascii_valor = nuevo_ascii_valor - 26
        # Verificamos si el caracter es una letra minúscula
        elif caracter.islower():
            # Si el valor ASCII desplazado es mayor que z (122),
            # comenzamos desde a (97) de nuevo
            if nuevo_ascii_valor < 97:
                nuevo_ascii_valor = nuevo_ascii_valor + 26
            # Si el valor ASCII desplazado es menor que a (97),
            # comenzamos desde z (122) de nuevo
            elif nuevo_ascii_valor > 122:
                nuevo_ascii_valor = nuevo_ascii_valor - 26
        # Convertimos el nuevo valor ASCII en su caracter correspondiente
        nuevo_caracter = chr(nuevo_ascii_valor)
        # Agregamos el nuevo caracter al resultado
        resultado += nuevo_caracter
    return resultado

texto_encriptado = "Krod, ¿frpr hvwð?"
desplazamiento = 3
texto_desencriptado = descifrado_cesar(texto_encriptado, desplazamiento)
print(texto_desencriptado)