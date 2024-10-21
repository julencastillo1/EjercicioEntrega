CLASES
  Producto:
    Es la clase base para todos los productos.
    Atributos: codigo, nombre, precio, categoria, stock, atributo_adicional.
    Método: __init__ para inicializar los atributos.
    
  Hogar_y_cocina, Bebe, Electronica, Jardin, Alimentos:
    Heredan de la clase Producto.
    Atributo adicional: descuento (inicializado a 25% por defecto).
    Método: __str__ para proporcionar una representación en cadena del objeto, mostrando todos sus atributos.
    
FUNCIONES

  cargar_catalogo:
    Lee un archivo CSV y crea un dataframe. A continuación, crea una lista de objetos Producto a partir del dataframe, instanciando la clase correspondiente según la categoría.
    
  buscar_producto:
    Permite al usuario buscar un producto por su código y muestra su información relevante.(Sirve para consultar información relevante de cada producto, como su stock)
    
  Añadir_Producto:
    Permite al usuario agregar un producto al carrito, verificando la disponibilidad de stock. El stock del producto se actualiza constantemente al añadir productos al carrito.
    
  Eliminar_Producto:
    Permite al usuario eliminar un producto del carrito. Muestra los productos que se han añadido y da la opción de eliminar el producto insertando su código. (No se pueden eliminar unidades sueltas, podría ser interesante en un futuro)
    
  Ver:
    Muestra los productos que se han añadido al carrito y calcula el coste total y lo visualiza.
    
  Pagar:
    Simula el proceso de pago, validando el número de tarjeta.
    
Aplicacion:
  Es la función principal que controla el flujo de la aplicación, presentando un menú al usuario y llamando a las funciones correspondientes.
  
FLUJO DEL PROGRAMA

  Carga del catálogo: Se lee un archivo CSV para crear una lista de productos.
  
  Menú principal: Se presenta un menú al usuario con opciones para buscar, agregar, eliminar, ver el carrito y pagar. 
  
  Interacción del usuario: Según la opción seleccionada, se ejecuta la función correspondiente.
  
  Proceso de compra: El usuario puede buscar productos, agregarlos al carrito, eliminarlos y finalmente realizar el pago.
  
La aplicación utiliza un interfaz interactivo y guiado con el usuario, haciendo que su uso sea intuitivo y cómodo.
