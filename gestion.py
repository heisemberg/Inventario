import os
import inventario

if __name__ == '__main__':
    products = {}
    shopping = {}
    sales = {}
    isAddProducts = True
    while isAddProducts:
        os.system('cls')
        print(f'1. Registrar Producto\n2. Mostrar Productos\n3. Registrar compra\n4. Mostrar Compras')
        opcion = int(input('Selecione una opcion: '))
        if opcion == 1:
            inventario.addProduct(products)
        
        elif opcion == 2:
            os.system('cls')
            print(products)
            os.system('pause')

        elif opcion == 3:
            os.system('cls')
            inventario.regShopping(shopping, products)

        elif opcion == 4:
            os.system('cls')
            print(shopping)
            os.system('pause')