ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def traductor(k,m,o):
    traduccion = []
    indice_clave = 0
    clave = k.upper()
    m = m.replace(" ", "")  # Convertir a minúsculas y eliminar espacios en blanco

    for caracter in m:
        num=ABC.find(caracter.upper())
        if num != -1:
            if o == 1:
                num += ABC.find(clave[indice_clave])
            elif o == 2:
                num -= ABC.find(clave[indice_clave])
            num %= len(ABC)
            if caracter.isupper():
                traduccion.append(ABC[num])
            elif caracter.islower():
                traduccion.append(ABC[num].lower())
            indice_clave += 1
            if indice_clave == len(clave):
                indice_clave = 0
        else:
            traduccion.append(caracter)
    return ('').join(traduccion)

def cifrar(k, m):
    return traductor(k,m,1)
    
def decifrar(k,m):
    return traductor(k,m,2)

def main():
    mensaje = input("Mensaje: ")
    key = input("Key: ")
    print("\n¿Que quiere hacer?\n1. Encryptar\n2. Descifrar")
    opc = int(input("Opción: "))

    if opc == 1:
        traduccion = cifrar(key, mensaje)
    elif opc == 2:
        traduccion = decifrar(key, mensaje)
    print(traduccion)

if __name__ == '__main__':
    main()