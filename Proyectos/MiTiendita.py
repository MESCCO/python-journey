import MiLibreria

InventarioGeneral = {
    "AZ001": {
        "nombre": "AZUCAR RUBIA",
        "unidad": "kg",
        "precio": 3.00,
        "cantidad": 1000
    },
    "AZ002": {
        "nombre": "AZUCAR BLANCO",
        "unidad": "kg",
        "precio": 4.00,
        "cantidad": 1200
    },
    "AZ003": {
        "nombre": "AZUCAR MORENA",
        "unidad": "kg",
        "precio": 4.50,
        "cantidad": 1100
    },
    "AZ004": {
        "nombre": "AZUCAR DE COCO",
        "unidad": "kg",
        "precio": 5.00,
        "cantidad": 500
    },
    "AR001": {
        "nombre": "ARROZ BLANCO",
        "unidad": "kg",
        "precio": 3.50,
        "cantidad": 300
    },
    "AR002": {
        "nombre": "ARROZ INTEGRAL",
        "unidad": "kg",
        "precio": 3.00,
        "cantidad": 1000
    },
    "AR003": {
        "nombre": "ARROZ PARBOIL",
        "unidad": "kg",
        "precio": 4.00,
        "cantidad": 800
    },
    "FI001": {
        "nombre": "FIDEOS LARGOS",
        "unidad": "Pkg",
        "precio": 2.00,
        "cantidad": 900
    },
    "FI002": {
        "nombre": "FIDEOS FINOS",
        "unidad": "Pkg",
        "precio": 1.50,
        "cantidad": 100
    },
    "FI003": {
        "nombre": "FIDEOS CORTOS",
        "unidad": "Pkg",
        "precio": 1.00,
        "cantidad": 1500
    },
    "SA001": {
        "nombre": "SAL MARINA",
        "unidad": "kg",
        "precio": 2.00,
        "cantidad": 100
    },
    "SA002": {
        "nombre": "SAL YODADA",
        "unidad": "kg",
        "precio": 1.00,
        "cantidad": 130
    },
    "SA003": {
        "nombre": "SAL DE MESA",
        "unidad": "kg",
        "precio": 3.00,
        "cantidad": 150
    },
    "SA004": {
        "nombre": "SAL GRUESA",
        "unidad": "kg",
        "precio": 5.00,
        "cantidad": 200
    },
    "GA001": {
        "nombre": "GALLETAS",
        "unidad": "Ud.",
        "precio": 1.00,
        "cantidad": 1400
    },
    "HU001": {
        "nombre": "HUEVOS",
        "unidad": "Ud.",
        "precio": 0.50,
        "cantidad": 10000
    }
}


InventarioInicial = {
    "AZ001": [3.00, 1000],
    "AZ002": [4.00, 1200],
    "AZ003": [4.50, 1100],
    "AZ004": [5.00, 500],
    "AR001": [3.50, 300],
    "AR002": [3.00, 1000],
    "AR003": [4.00, 800],
    "FI001": [2.00, 900],
    "FI002": [1.50, 100],
    "FI003": [1.00, 1500],
    "SA001": [2.00, 100],
    "SA002": [1.00, 130],
    "SA003": [3.00, 150],
    "SA004": [5.00, 200],
    "GA001": [1.00, 1400],
    "HU001": [0.50, 10000]
}

CatalogoProductos = {
    "AZ001": ["AZUCAR RUBIA", "kg"],
    "AZ002": ["AZUCAR BLANCO", "kg"],
    "AZ003": ["AZUCAR MORENA", "kg"],
    "AZ004": ["AZUCAR DE COCO", "kg"],
    "AR001": ["ARROZ BLANCO", "kg"],
    "AR002": ["ARROZ INTEGRAL", "kg"],
    "AR003": ["ARROZ PARBOIL", "kg"],
    "FI001": ["FIDEOS LARGOS", "Pkg"],
    "FI002": ["FIDEOS FINOS", "Pkg"],
    "FI003": ["FIDEOS CORTOS", "Pkg"],
    "SA001": ["SAL MARINA", "KG"],
    "SA002": ["SAL YODADA", "KG"],
    "SA003": ["SAL DE MESA", "kg"],
    "SA004": ["SAL GRUESA", "kg"],
    "GA001": ["GALLETAS", "Ud."],
    "HU001": ["HUEVOS", "Ud."]
}



def MenuPrincipal():
    print("")
    print("1.   Inventario  ")
    print("2.   Compras     ")
    print("3.   Ventas      ")
    print("4.   Proveedores ")
    print("5.   Catalogo    ")
    opcion=MiLibreria.LeerEntero(1,4,"Escoge una opcion entre 1 y 4: ")
    return opcion

def MostrarInventario(InventarioListar,CatalogoProductos,Mensaje):
    print("")
    print(Mensaje)
    print("="*82)
    print(f"{"|"}{"CODIGO":^10}{"PRODUCTO":^20}{"UNIDAD":^10}{"P.UNITARIO":^20}{"CANTIDAD":^20}{"|"}")
    print("="*82)
    for clave,Detalle in InventarioListar.items():
        print(f"{"|"}{clave:^10}{CatalogoProductos[clave][0]:^20}{CatalogoProductos[clave][1]:^10}{Detalle[0]:^20.2f}{Detalle[1]:^20.2f}{"|"}")
    print("="*82)
    return 

MostrarInventario(InventarioInicial,CatalogoProductos,"mostrar")


def mostarInventario2(inventario,mensaje):
    print("")
    print(mensaje)