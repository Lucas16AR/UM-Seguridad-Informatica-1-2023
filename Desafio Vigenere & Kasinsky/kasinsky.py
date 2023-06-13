from collections import defaultdict

alphabet = "abcdefghijklmnñopqrstuvwxyz 0123456789"

def encontrar_repeticiones_subcadenas(texto_cifrado, longitud_subcadena):
    repeticiones = defaultdict(list)
    for i in range(len(texto_cifrado) - longitud_subcadena + 1):
        subcadena = texto_cifrado[i:i + longitud_subcadena]
        repeticiones[subcadena].append(i)
    return repeticiones

def encontrar_factores_comunes(distancias):
    factores_comunes = []
    for i in range(len(distancias) - 1):
        for j in range(i + 1, len(distancias)):
            distancia_i = distancias[i]
            distancia_j = distancias[j]
            gcd = encontrar_mcd(distancia_i, distancia_j)
            if gcd > 1:
                factores_comunes.append(gcd)
    return factores_comunes

def encontrar_mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def determinar_longitud_clave(factores_comunes):
    longitud_clave = max(set(factores_comunes), key=factores_comunes.count)
    return longitud_clave

def descifrar_vigenere(texto_cifrado, longitud_clave):
    mensaje_descifrado = ""
    for i, letra in enumerate(texto_cifrado):
        clave_letra = i % longitud_clave
        clave_ord = alphabet.index('a') if letra.islower() else 0
        # descifrado = alphabet[(alphabet.index(letra) - alphabet.index('A') - clave_letra - clave_ord) % len(alphabet)]
        descifrado = chr((ord(letra) - ord('A') - clave_letra - clave_ord) % 38 + ord('A'))
        mensaje_descifrado += descifrado
    return mensaje_descifrado

def main():
    texto_cifrado = input("Ingrese el texto cifrado: ")
    longitud_subcadena = int(input("Ingrese la longitud de las subcadenas: "))
    repeticiones = encontrar_repeticiones_subcadenas(texto_cifrado, longitud_subcadena)

    distancias = []
    for subcadena, posiciones in repeticiones.items():
        if len(posiciones) > 1:
            distancias.extend([posiciones[i] - posiciones[i-1] for i in range(1, len(posiciones))])
    if not distancias:
        print("No se encontraron repeticiones de subcadenas.")
        return
    factores_comunes = encontrar_factores_comunes(distancias)
    if not factores_comunes:
        print("No se encontraron factores comunes entre las distancias.")
        return
    longitud_clave = determinar_longitud_clave(factores_comunes)
    mensaje_descifrado = descifrar_vigenere(texto_cifrado, longitud_clave)

    print("Longitud de la clave encontrada:", longitud_clave)
    print("Mensaje descifrado:", mensaje_descifrado)

if __name__ == "__main__":
    main()