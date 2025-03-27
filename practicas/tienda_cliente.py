def hacer_menu():
    print("1.registar cliente")
    print("2.eliminar cliente")
    print("0.salir del sistema")
    print("...selecione una opcion...")
    
    opcion= int(input())
    return opcion
 
#zona codigo 
 
 
def registrar_cliente():
    nombre_cliente = input("digite el nombre: ")
    apellido_cliente = input("digite el apellido: ")
    cedula_cliente = input("digite la cedula: ")
    info_cliente= [nombre_cliente, apellido_cliente, cedula_cliente]    
    
    return info_cliente

def guardar_cliente(info_cliente,bd_cliente):
    bd_cliente.append(info_cliente)
    return bd_cliente

def incluir_nueva_lista():
    aux_lista=[]
    cantidad_nuevas = int(input("digite la cantidad nueva de clientes"))
    for i in range(cantidad_nuevas):
        aux = registrar_cliente()
        aux_lista.append(aux)
    print(aux_lista)




base_datos = []
aux_opcion = hacer_menu()
aux_info_cliente = registrar_cliente()

aux_basedatos = guardar_cliente(aux_info_cliente,base_datos)
base_datos = aux_basedatos
print(base_datos)