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
