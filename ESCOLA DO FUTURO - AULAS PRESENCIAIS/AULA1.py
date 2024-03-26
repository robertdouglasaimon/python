def calcular_area_cubo (lado):

    return 6 * lado ** 2

lado = float (input("Digite o comprimento do lado:"))
area = calcular_area_cubo (lado)
print(f"A área do cubo com lado {lado} é {area}.")

