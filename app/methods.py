
def buscar_elemento_id_nombre(lista_objetos_almacen,parametro_id, parametro_nombre):
    if parametro_id != None:
        for objeto in lista_objetos_almacen:
            if objeto.get('id') == int(parametro_id):
                return { 'objeto': objeto, 'status': 200}
                
        return {'Mensaje': 'Objeto no encontrado', 'status': 404}
        
    elif parametro_nombre != None:
        for objeto in lista_objetos_almacen:
            if objeto.get('nombre') == parametro_nombre.capitalize():
                return { 'objeto': objeto, 'status': 200}
                
        return {'Mensaje': 'Objeto no encontrado', 'status': 404}
        
    return {'Objetos': lista_objetos_almacen, 'status': 200}