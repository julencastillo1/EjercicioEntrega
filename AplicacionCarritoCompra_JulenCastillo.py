import pandas as pd
import re


# Clases
class Producto:
    def __init__(self, codigo, nombre, precio, categoria, stock, atributo_adicional):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.atributo_adicional = atributo_adicional

class Hogar_y_cocina(Producto):
    def __init__(self, codigo, nombre, precio, categoria, stock,atributo_adicional,descuento=25):
        super().__init__(codigo, nombre, precio, categoria, stock, atributo_adicional)
        self.descuento = descuento
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio:{self.precio}, Categoría: {self.categoria}, Stock:{self.stock}, Descuento:{self.descuento} "

class Bebe(Producto):
    def __init__(self, codigo, nombre, precio, categoria, stock,atributo_adicional, descuento=25):
        super().__init__(codigo, nombre, precio, categoria, stock, atributo_adicional)
        self.descuento = descuento
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio:{self.precio}, Categoría: {self.categoria}, Stock:{self.stock}, Descuento:{self.descuento} "

class Electronica(Producto):
    def __init__(self, codigo, nombre, precio, categoria, stock,atributo_adicional, descuento=25):
        super().__init__(codigo, nombre, precio, categoria, stock, atributo_adicional)
        self.descuento = descuento
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio:{self.precio}, Categoría: {self.categoria}, Stock:{self.stock}, Descuento:{self.descuento} "

class Jardin(Producto):
    def __init__(self, codigo, nombre, precio, categoria, stock,atributo_adicional, descuento=25):
        super().__init__(codigo, nombre, precio, categoria, stock, atributo_adicional)
        self.descuento = descuento

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio:{self.precio}, Categoría: {self.categoria}, Stock:{self.stock}, Descuento:{self.descuento} "

class Alimentos(Producto):
    def __init__(self, codigo, nombre, precio, categoria, stock,atributo_adicional, descuento=25):
        super().__init__(codigo, nombre, precio, categoria, stock, atributo_adicional)
        self.descuento = descuento
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio:{self.precio}, Categoría: {self.categoria}, Stock:{self.stock}, Descuento:{self.descuento} "



# Funciones
def cargar_catalogo(x):
    Catalogo = []
    producto = []
    df = pd.read_csv(x)
    print(df)
    for index, row in df.iterrows():
        categoria = row['categoria']
        if categoria == 'Bebé':
            producto = Bebe(row['codigo'],row['nombre'],row['precio'],row['categoria'],row['stock'],row['atributo_adicional'])
        elif categoria == 'Hogar y cocina':
            producto = Hogar_y_cocina(**row.to_dict())
        elif categoria == 'Electrónica':
            producto = Electronica(**row.to_dict())
        elif categoria == 'Jardín':
            producto = Jardin(**row.to_dict())
        elif categoria == 'Alimentos':
            producto = Alimentos(**row.to_dict())
        else:
            raise ValueError('Categoria no encontrado')

        Catalogo.append(producto)

    return Catalogo, df

def buscar_producto(Catalogo):
    while True:
        print('')
        codigo = input('Inserte el código del producto que desea encontrar. Marque S si quiere salir de esta pestaña: ').upper()
        if codigo == 'S':
            print('')
            print('Regresando al menú principal')
            break
        try:
            codigo = int(codigo)
        except ValueError:
            print('')
            print('Error. Ingrese un código de producto válido: ')
        if type(codigo) == int:
            Esta = 0
            for producto in Catalogo:
                if producto.codigo == codigo:
                    Esta = 1
                    print('')
                    print('El producto es:', producto.nombre)
                    print('El stock del producto es:', producto.stock)

            if Esta == 0:
                print('El producto no está en el catálogo')

def Añadir_Producto(df,Catalogo, Carrito):
    while True:
        print('')
        print(df)
        print('')
        codigo = input('¿Qué producto desea añadir al carrito? Ingrese el código del producto. Marque S si quiere salir de esta pestaña: ').upper()
        if codigo == 'S':
            print('')
            print('Regresando al menú principal')
            break
        try:
            codigo = int(codigo)
        except ValueError:
            print('')
            print('Error. Ingrese un código de producto válido: ')
        Esta = 0

        for producto in Catalogo:

            if producto.codigo == codigo:
                Esta = 1
                print('')
                print('El stock del producto es: ', producto.stock)
                print('')
                Unidades = int(input('Ingrese el número de unidades que quiera añadir al carrito. Marque S si quiere salir de esta pestaña: '))
                if Unidades < producto.stock:
                        producto.unidades = Unidades
                        producto.stock = producto.stock - Unidades
                        if producto not in Carrito:
                            Carrito.append(producto)
                        print('')
                        print('El stock actualizado es:', producto.stock)
                else:
                        print('')
                        print('Lo siento, no hay stock suficiente')
                break
        if Esta == 0:
            print('')
            print('El producto no está en el catálogo')

        return Carrito

def Eliminar_Producto(Carrito):
    while True:
        if not Carrito:
            print('')
            print('El carrito está vacío')
            break
        for producto in Carrito:
            print('')
            print(producto)
            print('')
        codigo = input('Inserte el código del producto que desea eliminar. Marque S si quiere salir de esta pestaña: ').upper()
        if codigo == 'S':
            print('')
            print('Regresando al menú principal')
            break
        try:
            codigo = int(codigo)
        except ValueError:
            print('')
            print('Error. Ingrese un código de producto válido: ')
            Esta = 0
        for producto in Carrito:
            if producto.codigo == codigo:
                Esta = 1
                Carrito.remove(producto)
        if Esta == 0:
            print('')
            print('El producto no está en el catálogo')

    return Carrito

def Ver(Carrito):
    if not Carrito:
        print('')
        print('El carrito está vacío')
        return
    for producto in Carrito:
        print('')
        print(producto)
    def CalcularCosteCarrito(Carrito):
        CosteTotal = 0
        for producto in Carrito:
            CosteTotal = round((producto.precio * producto.unidades)/(1+ producto.descuento/100) + CosteTotal)
        return CosteTotal
    CosteTotal = CalcularCosteCarrito(Carrito)
    print('')
    print('El coste total del carrito es: ',CosteTotal,'€')
    return CosteTotal

def Pagar(CosteTotal):
    if CosteTotal <= 0:
        print('')
        print('No se ha añadido nada al carrito')
        return

    def ValidarTarjeta(NumeroTarjeta):
        patron = r"ES\d{5}"
        if re.match(patron, NumeroTarjeta):
            return True
        else:
            return False

    while True:
        print('')
        print('El coste total del carrito es: ',CosteTotal,'€')
        while True:
            NumeroTarjeta = input('Ingrese su código de tarjeta bancaria. El código debe empezar por "ES" y estar seguido por 5 números (Ej: "ES12345"). Marque S si quiere salir de esta pestaña:  ' ).upper()
            if NumeroTarjeta == 'S':
                print('')
                print('Regresando al menú principal')
                break
            try:
                NumeroTarjeta = str(NumeroTarjeta)
            except ValueError:
                print('')
                print('Ingrese un número de tarjeta válido')
            if ValidarTarjeta(NumeroTarjeta) == True:
                Confirmacion = input('Tarjeta correcta. ¿Quiere proceder con el pago? Responda "Si" o "No"' ).lower()
                if Confirmacion == 'si':
                    print('')
                    print('Pago realizado con existo. ¡Muchas gracias!')
                if Confirmacion == 'no':
                    print('')
                    print('Pago cancelado')
                    break
            if ValidarTarjeta(NumeroTarjeta) == False:
                print('')
                print('Error. Código de tarjeta incorrecto')
                break

def Aplicacion(archivo_csv):
    Catalogo, df = cargar_catalogo(archivo_csv)
    Carrito = []
    CosteTotal = 0
    while True:
        print('')
        Menu = input('¿Que quiere hacer? ¿(B)uscar producto, (A)gregar producto, (E)liminar producto, (V)er carrito, (P)agar o (S)alir?: ').upper()
        if Menu == 'B':
            buscar_producto(Catalogo)
        if Menu == 'A':
            Carrito= Añadir_Producto(df,Catalogo, Carrito)
        if Menu == 'V':
            CosteTotal = Ver(Carrito)
        if Menu == 'E':
            Carrito = Eliminar_Producto(Carrito)
        if Menu == 'P':
            Pagar(CosteTotal)

        if Menu == 'S':
            print('')
            print('Gracias por visitar nuestra página web')
            break



# Programa

Aplicacion('Catálogo.csv')
