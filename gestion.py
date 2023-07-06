import os
import inventario

if __name__ == '__main__':
    products = {}
    shopping = {}
    sales = {}
    isAddProducts = True
    while isAddProducts:
        os.system('cls')
        print(f'1. Registrar Producto\n2. Mostrar Productos\n3. Eliminar Producto\n4. Registrar compra\n5. Mostrar Compras\n6. Registrar venta\n6. Mostrar ventas')
        opcion = int(input('Selecione una opcion: '))
        try:
            if opcion == 1:
                inventario.addProduct(products)

            elif opcion == 2:
                os.system('cls')
                clave=(products.keys())
                print('+','-'*76,'+')
                print("| {:^5} | {:^12} | {:^5} | {:^10} | {:^12} | {:^7} | {:^7} |".format('COD','NOMBRE','STOCK','ESTADO','PROVEEDOR','VAL.COM','VAL.VEN'))
                
                for i in clave:
                    print('+','-'*76,'+')
                    print("| {:^5} | {:^12} | {:^5} | {:^10} | {:^12} | {:^7} | {:^7} |".format(products[i]['codigo'], products[i]['nombre'],products[i]['stock'],products[i]['estado'],products[i]['proveedor'],products[i]['valorCompra'],products[i]['valorVenta']))
                print('+','-'*76,'+')    
                os.system('pause')
            
            elif opcion == 3:
                os.system('cls')
                inventario.remProduct(products)

            elif opcion == 4:
                os.system('cls')
                inventario.regShopping(shopping, products)

            elif opcion == 5:
                os.system('cls')
                print(shopping)
                os.system('pause')

            elif opcion == 6:
                os.system('cls')
                inventario.regSales(sales, products)

            else:
                os.system('cls')
                print(sales)
                os.system('pause')
        except Exception:
            isAddTeam= bool(input("Desea continuar en el programa S(Si) o Enter(No) :"))