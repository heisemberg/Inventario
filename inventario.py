import os

def addProduct (productos : dict):
    cod = input('Ingrese Codigo de producto: ')
    producto = {
        cod:{
            "codigo": cod,
            "nombre": input('Ingrese Nombre de Producto: '),
            "stock": int(input('Ingrese Stock: ')),
            "estado": input('Estado: '),
            "proveedor": input('Ingrese proveedor: '),
            "valorCompra": int(input('Ingrese valor de Compra: ')),
            "valorVenta": int(input('Ingrese valor de Venta: '))
        }  
    } 
    productos.update(producto)

def regShopping(compras : dict, productos : dict):
    isAddShopping = True
    codCompra = input('Ingrese codigo de compra: ') 
    compra = {
        codCompra:{
            'cod': codCompra,
            "docCompra": input('Ingrese documento compra: '),
            "fechaCompra": input('Ingrese fecha de compra: '),
        }
    }
    carritoCompras = {}

    while isAddShopping:
        producto = productos.get(input('Ingrese el codigo de producto: '),-1)
        print(producto)
        if producto == -1:
            print('Codigo de producto no encontrado')
        else:
            cantCompra = int(input('Ingrese cantidad: '))
            print(producto['stock'])
            if cantCompra <= producto['stock']:
                newStock = producto['stock']-cantCompra
                valCompra = cantCompra * producto['valorCompra']
                producto['stock']= newStock
                producto.update({'cantCompra':cantCompra})
                producto.update({'valCompra':valCompra})
                producto.pop('valorVenta')
                print(producto)
                carritoCompras.update({producto['codigo']: producto})
                print(carritoCompras)
                compra[codCompra].update({'compras':carritoCompras})
                print(compra)
                isAddShopping = bool(input("Desea agregar otro Producto S(Si) Enter(No)"))
    compras.update(compra)
    print(compras)
        