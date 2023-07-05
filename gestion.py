import os
import inventario

if __name__ == '__main__':
    products = {}
    shopping = {}
    sales = {}
    isAddProducts = True
    while isAddProducts:
        os.system('cls')
        print(f'1. Registrar Producto\n2. Borrar Producto\n3. Salir')
        opcion = int(input('Selecione una opcion: '))
        if opcion == 1:
            inventario.addProduct(products)
        
        elif opcion == 2:
            os.system('cls')
            print(products)
            os.system('pause')