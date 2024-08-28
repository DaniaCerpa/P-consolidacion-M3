def clasificar_en_categ(celebridades):
    
    categorias= {
    "magos" : [],
    "cientificos" : [],
    "otros" : []
    }
    
    for nombre in celebridades:
        if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
            categorias["magos"].append(nombre) 
        elif nombre in ["Newton", "Hawking", "Einstein"]:
            categorias["cientificos"].append(nombre)
        else:
            categorias["otros"].append(nombre) 
    return categorias
