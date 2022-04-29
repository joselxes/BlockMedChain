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
            print(i+1,"xxxx")
            return False
    return True
            # print("ya existe wey")
    #realizo operacion de acurdo a la varibale de si existe o no
def getCedula(nombre,todo):
    for i in range(0,len(todo)):
        print(i,todo[i])
        if todo[i]["name"]==nombre:
            return i
    return -1
def getIndex(cedula,listaIndices):
    for i in range(0,len(listaIndices)):
        if cedula== listaIndices[i]["cedula"]:
            return i

    return -1
# def getInfo(indice,listaIndices,listadiccionarios):
#     for i in listaIndices:

#         return j
#     return "False"
def listaBusqueda(indicesSearch):
    rLista=[]
    for i in indicesSearch:
        if i>=0:
            rLista.append(i)
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


# {'name': 'GENESIS', 'email': 'med@usa.com', 'phone': '911', 'cedula': '9999999999', 'enfermedades': ['todos'], 'option': 'Agencia', 'detalles': 'cualquier informacion 911'},
#  {'name': 'Jean Sotelo', 'email': 'js@outlook.com', 'phone': '67866786789', 'cedula': '4444444444', 'enfermedades': ['Alergia a la penicilina'], 'option': 'Masculino', 'detalles': 'Historial de paros cardiacos'},
#   {'name': 'Paco Gerlo', 'email': 'teienoToyo@gmail.com', 'phone': '1112224444', 'cedula': '1111111111', 'enfermedades': ['Alergia a la penicilina, Alergia con anticonvulsivos, Sufre de diabetes'], 'option': 'Masculino', 'detalles': 'Sufre de narcolepsia'}, 
#   {'name': 'Jack Hallate', 'email': 'Dolores@gmail.com', 'phone': '4556778899', 'cedula': '8888888888', 'enfermedades': ['Alergia con anticonvulsivos, Sufre de diabetes'], 'option': 'Femenino', 'detalles': 'En quimioterapia'}]
