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
            "docCompra": input('Ingrese documento compra'),
            "fechaCompra": input('Ingrese fecha de compra'),
            "compra": {}
        }
    }

    while isAddShopping:
        producto = productos.get(input('Ingrese el codigo de producto:'),-1)
        if producto == -1:
            print('Codigo de producto no encontrado')
        else:
            cantCompra = int(input('Ingrese cantidad: '))
            if cantCompra <= producto['stock']:
                newStock = producto['stock']-cantCompra
                valCompra = newStock * producto['valorCompra']
                productos.update({producto['stock']: newStock})
                compra.update({codCompra['compra']: producto})
                #compra['codCompra']['compra'].update(producto[valCompra])
                
        compras.update(compra)
        isAddShopping = bool("Desea agregar otro Producto S(Si) Enter(No)")