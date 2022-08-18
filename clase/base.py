
def algoX():
    nombre = "Edi"
    edad = 50
    esProgramador = True

    return nombre, edad, esProgramador

if __name__ == '__main__':
    x,y,z = algoX()
    xyx = algoX()
    print(f'la variable xyz es de tipo: {type(x)},{type(y)},{type(z)}')
    print(f'{x},{y},{z}')
    