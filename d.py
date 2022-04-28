#my librery dictionario para
def dicTostring(diccionario):
    clientDissease=[]
    st=""
    clientData=""
    for i in diccionario:
        if "enfermedad" in i:
            for j in diccionario["enfermedades"]:
                st+=j+""
            clientData+=st
        else:
            clientData+=diccionario[i]
    # reviso si existe el cliente o no para "agregarlo"
    # print(st)
    return clientData
def existe(nuevo,todo):
    for i in todo:
        if i["cedula"]==nuevo["cedula"]:
            return False
    return True
            # print("ya existe wey")
    #realizo operacion de acurdo a la varibale de si existe o no
def getCedula(nuevo,todo):
    for i in todo:
        if i["name"]==nuevo["name"]:
            return i["cedula"]
    return "False"
def getIndex(cedula,listaIndices):
    if cedula=="False":
        return "False"
    for i in listaIndices:
        if i["cedula"]==cedula:
            return i["indice"]
    return "False"
def getInfo(indice,listaIndices,listadiccionarios):
    for i in listaIndices:
        if i["indice"]==indice:
            for j in listadiccionarios:
                if j["cedula"]==i["cedula"]:
                    return j
    return "False"
def listaBusqueda(a,b,c):
    rLista=[]
    if not(a=="False"):
        rLista.append(a)
    if not(b=="False"):
        if not(b in rLista):
            rLista.append(b)
    if not(c in rLista):
        rLista.append(c)

    return rLista

def nuevoTodict(diccionario):
    clientDissease=[]
    # clientData=""
    for i in diccionario:
        if "enfermedad" in i:
            clientDissease.append(diccionario[i])
    nuevoCliente={"name":diccionario["name"],"email":diccionario["email"],"phone":diccionario["phone"],"cedula":diccionario["cedula"],"enfermedades":clientDissease,"option":diccionario["option"],"detalles":diccionario["about"]}
    return nuevoCliente
def getListFromDict(diccionario):
    dis=[]
    for i in diccionario:
        if type(diccionario[i])==type([]):
            dis.append(diccionario[i])
    return dis
