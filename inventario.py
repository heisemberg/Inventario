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

def remProduct(productos):
    producto = productos.get(input('Ingrese el codigo de producto: '),-1)
        
    if producto == -1:
        print('Codigo de producto no encontrado')
    else:
        producto.pop(producto['cod'])


def regShopping(compras : dict, productos : dict):
    isAddShopping = True
    item = 1
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
        
        if producto == -1:
            print('Codigo de producto no encontrado')
        else:
            cantCompra = int(input('Ingrese cantidad: '))
            newStock = producto['stock']+cantCompra
            valCompra = cantCompra * producto['valorCompra']
            producto['stock']= newStock            
            carritoCompras.update({item : {producto['codigo']: producto, 'cantCompra':cantCompra, 'valCompra':valCompra } } )
            compra[codCompra].update({'compras':carritoCompras})
            item+=1
            isAddShopping = bool(input("Desea agregar otro Producto S(Si) Enter(No)"))
    compras.update(compra)
   

def regSales(ventas : dict, productos : dict):
    isAddSale = True
    item=1
    codVenta = input('Ingrese codigo de venta: ') 
    venta = {
        codVenta:{
            'cod': codVenta,
            "docCompra": input('Ingrese documento venta: '),
            "fechaCompra": input('Ingrese fecha de venta: '),
        }
    }
    carritoVentas = {}

    while isAddSale:
        producto = productos.get(input('Ingrese el codigo de producto: '),-1)
        
        if producto == -1:
            print('Codigo de producto no encontrado')
        else:
            cantVenta = int(input('Ingrese cantidad: '))
            if cantVenta <= producto['stock']:
                newStock = producto['stock']-cantVenta
                valVenta = cantVenta * producto['valorVenta']
                producto['stock']= newStock
                carritoVentas.update({item:{producto['codigo']: producto, 'cantVenta':cantVenta,'valVenta':valVenta}})
                venta[codVenta].update({'ventas':carritoVentas})
                item+=1
                isAddSale = bool(input("Desea agregar otro Producto S(Si) Enter(No)"))
            else:
                print('No hay stock suficiente')
                isAddSale = bool(input("Desea agregar otro Producto S(Si) Enter(No)"))
    ventas.update(venta)
    