def copias_genero(genero,dict_libros,dict_prestamos):
    total_copias_genero = 0
    for codigo_libro,valor_libro in dict_libros.items():
        if genero == valor_libro[2].lower():
            for codigo_prestamo,valor_prestamo in dict_prestamos.items():
                if codigo_libro == codigo_prestamo:
                    total_copias_genero += int(valor_prestamo[1])
                    break
    print(f"La cantidad de copias de libros de el genero [{genero}] es de: {total_copias_genero} copias")
def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Ingrese una opcion que sea un numero y valido (No puede ser un decimal)")
    if opcion > 6 or opcion < 1:
        print("La opcion ingresada tiene que estar dentro del rango de opciones ofreciadas")
    else:
        return opcion
def validar_codigo(codigo,dict_libros,dict_prestamos):
    if codigo.strip() == "":
        return False
    elif codigo in dict_libros.keys() or codigo in dict_prestamos.keys():
        return False
    else:
        return True
def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    else:
        return True
def validar_autor(autor):
    if autor.strip() == "":
        return False
    else:
        return True
def validar_genero(genero):
    if genero.strip() == "":
        return False
    else:
        return True
def validar_anio(anio):
    try:
        anio = int(anio)
    except ValueError:
        return False
    if anio < 0:
        return False
    else:
        return True
def validar_editorial(editorial):
    if editorial.strip() == "":
        return False
    else:
        return True
def validar_es_novedad(es_novedad):
    if es_novedad == "s" or es_novedad == "n":
        return True
    else:
        return False
def validar_precio_multa(precio_multa):
    try:
        precio_multa = int(precio_multa)
    except ValueError:
        return False
    if precio_multa > 0:
        return True
    else:
        return False
def validar_copias_disponibles(copias_disponibles):
    try:
        copias_disponibles = int(copias_disponibles)
    except ValueError:
        return False
    if copias_disponibles < 0:
        return False
    else:
        return True
def agregar_libro(codigo, titulo, autor, genero, anio, editorial, es_novedad, precio_multa, copias_disponibles,dict_libros,dict_prestamos):
    if codigo in dict_libros.keys() or codigo in dict_prestamos.keys():
        return False
    libros[codigo] = [titulo,autor,genero,anio,editorial,es_novedad]
    prestamos[codigo] = [precio_multa,copias_disponibles]
    return True
def busqueda_multa(multa_min, multa_max,dict_libros, dict_prestamos):
    if multa_min < 0 or multa_max < 0:
        print("Las multas ingresadas no pueden ser menores a 0")
    elif multa_min > multa_max:
        print("La multa minima no puede superar el valor de la multa maxima")
    else:
        lista_multa = []
        for codigo_prestamo,prestamo in dict_prestamos.items():
            if prestamo[0] >= multa_min and prestamo[0] <= multa_max:
                if prestamo[1] > 0:
                    for codigo_libro, libro in dict_libros.items():
                        if codigo_prestamo == codigo_libro:
                            string_libro = ""
                            string_libro += libro[0]
                            string_libro += "--"
                            string_libro += codigo_libro
                            lista_multa.append(string_libro)
                            break
        if not lista_multa:
            print("No hay libros en ese rango de multa")
        else:
            print(sorted(lista_multa))
        
def buscar_codigo(codigo,dict_libros):
    for codigo_libro in dict_libros.keys():
        if codigo.upper() == codigo_libro.upper():
            return True
    return False

def actualizar_multa(codigo,nueva_multa,dict_prestamos):
    if buscar_codigo(codigo.upper(),libros):
        dict_prestamos[codigo.upper()][0] = nueva_multa
        return True
    else:
        return False

def eliminar_libro(codigo,dict_libros,dict_prestamos):
    if buscar_codigo(codigo.upper(),libros):
        dict_libros.pop(codigo.upper())
        dict_prestamos.pop(codigo.upper())
        return True
    else:
        return False
libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019,
'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023,
'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral',
False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015,
'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021,
'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores',
False]
}
prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6]
}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género\n2. Búsqueda de libros por rango de multa\n3. Actualizar multa de libro\n4. Agregar libro\n5. Eliminar libro\n6. Salir")
    print("====================================")
    match leer_opcion():
        case 1:
            copias_genero(input("Ingrese el genero del cual desea encontrar copias de libros").lower(),libros,prestamos)
        case 2:
            try:
               busqueda_multa(int(input("Ingrese la multa minima para la busqueda: ")),int(input("Ingrese la multa maxima para la busqueda: ")),libros,prestamos)
            except ValueError:
                print("Los valores de las multas deben ser numeros enteros")
            
        case 3:
            try:
                nueva_multa_ingresada = int(input("Ingrese la nueva multa de el libro siendo modificado: "))
            except ValueError:
                print("La nueva multa ingresada debe ser un numero entero")
            if nueva_multa_ingresada <= 0:
                print("La nueva multa debe ser mayor a 0")
            else:
                actualizar_multa(input("Ingrese el codigo del libro el cual desea actualizar su multa: "),nueva_multa_ingresada ,prestamos)
        case 4:
            codigo = input("Ingrese el CODIGO del libro a agregar: ")
            if not validar_codigo(codigo,libros,prestamos):
                print("[Error] Codigo ingresado esta vacio o ya se encuentra en la base de datos")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            titulo = input("Ingrese el TITULO del libro que desea agregar: ")
            if not validar_titulo(titulo):
                print("[Error] El titulo se encuentra en blanco")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            autor = input("Ingrese el AUTOR del libro a agregar: ")
            if not validar_autor(autor):
                print("[Error] El autor se encuentra en blanco")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            genero = input("Ingrese el GENERO del libro a agregar: ")
            if not validar_genero(genero):
                print("[Error] El genero se encuentra en blanco")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            anio = input("Ingrese el AÑO del libro que desea agregar: ")
            if not validar_anio(anio):
                print("[Error] El año debe ser un numero entero, positivo y mayor que 0")          
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            else:
                anio = int(anio)
            editorial = input("Ingrese EDITORIAL del libro a agregar: ")
            if not validar_editorial(editorial):
                print("[Error] La editorial se encuentra en blanco")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            es_novedad = input("El libro es novedad? (s = Sí / n = No): ")
            if not validar_es_novedad(es_novedad):
                print("[Error] La opcion escogida tiene que ser s o n")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            if es_novedad.lower() == "s":
                es_novedad = True
            else:
                es_novedad = False
            precio_multa = input("Ingrese el precio de multa del libro a agregar: ")
            if not validar_precio_multa(precio_multa):
                print("[Error] El precio de multa del libro no puede ser menor o igual a 0")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            else:
                precio_multa = int(precio_multa)
            copias_disponibles = input("Ingrese las copias disponibles del libro a agregar: ")
            if not validar_copias_disponibles(copias_disponibles):
                print("[Error] Las copias disponibles no pueden ser menor a 0")
                print("[Error] No se ha podido agregar el libro a la base de datos...")
                continue
            else:
                precio_multa = int(precio_multa)
            if agregar_libro(codigo,titulo,autor,genero,anio,editorial,es_novedad,precio_multa,copias_disponibles,libros,prestamos):
                print("Libro Agregado Correctamente")
            else:
                print("El libro no se ha podido agregar")
        case 5:
            eliminar_libro(input("Ingrese el codigo del libro que desea eliminar de la base de datos: "),libros,prestamos)
        case 6:
            break

print("Programa Finalizado")