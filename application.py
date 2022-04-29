import os
import requests
from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
import d
from blockchain import Block, Blockchain
bc = Blockchain()

# creo clientes base


clientesTodos=[{"name": 'GENESIS', "email": 'med@usa.com', "phone": '911', "cedula": '9999999999', "enfermedades": ['todos'], "option": 'Agencia', "detalles": 'cualquier informacion 911'},
{"name": 'Jean Sotelo', "email": 'js@outlook.com', "phone": '67866786789', "cedula": '4444444444', "enfermedades": ['Alergia a la penicilina'], "option": 'Masculino', "detalles": 'Historial de paros cardiacos'},
{"name": 'Paco Gerlo', "email": 'teienoToyo@gmail.com', "phone": '1112224444', "cedula": '1111111111', "enfermedades": ['Alergia a la penicilina, Alergia con anticonvulsivos, Sufre de diabetes'], "option": 'Masculino', "detalles": 'Sufre de narcolepsia'},
{"name": 'Jack Hallate', "email": 'Dolores@gmail.com', "phone": '4556778899', "cedula": '8888888888', "enfermedades": [ 'Alergia con anticonvulsivos, Sufre de diabetes'], "option": 'Femenino', "detalles": 'En quimioterapia'}]
#agrego al blockchain un cliente
# print(clientesTodos[0])
# print(d.dicTostring(clientesTodos[0]))

bc.add_block(d.dicTostring(clientesTodos[0]))
bc.add_block(d.dicTostring(clientesTodos[1]))
bc.add_block(d.dicTostring(clientesTodos[2]))
bc.add_block(d.dicTostring(clientesTodos[3]))
bc.unconfirmed_transactions.append({"name": 'Frank Mill', "email": 'arres@gmail.com', "phone": '3454556677', "cedula": '5555555555', "enfermedades": 'Alergia con anticonvulsivos, Sufre de diabetes', "option": 'Femenino', "detalles": 'tercera edad'})
print(d.dicTostring(clientesTodos[3]))
# print("-----------")
# bc.chain[-1].print_bloque()
indexTodos=[{"indice":0,"cedula":"9999999999"},
{"indice":1, "cedula": '4444444444'},
{"indice":2, "cedula": '1111111111'},
{"indice":3, "cedula": '8888888888'},
]
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("bienvenido.html")
@app.route("/buscar",methods=["GET","POST"])
def buscar():
    print("BUSCAR")
    indices=[]
    bloques=[]
    info=[]
    indiceTemp=0
    if request.form.get("name") is not None:
        name=request.form
        print(name)
        if name["name"]=="todos":
            bloques=bc.chain[1:]
            info=clientesTodos

        else:
            """primero obtengo indice  con el nombre"""
            indiceNombre=d.getCedula(name["name"],clientesTodos)
            """segundo obtengo indice  con el nombre"""
            indiceCedula=d.getIndex(name["cedula"],indexTodos)
            """tercero obtengo indice por indice"""

            if (""==name["indice"]):
                print("kkkkkkkkkkkkk")
                indiceTemp=-1
            else:
                indiceTemp=int(name["indice"])-1
                if indiceTemp>len(clientesTodos):
                    indiceTemp=-1
            print("------------",indiceNombre,indiceCedula,indiceTemp)

            indices=d.listaBusqueda([indiceNombre,indiceCedula,indiceTemp])
            print(len(bc.chain),len(clientesTodos))
            if len(indices)>0:
                for i in indices:
                    print(i)
                    bTemp=bc.searchIndex(i+1)
                    bloques.append(bTemp)
                    bloques[-1].print_bloque()
                    info.append(clientesTodos[i])
                    print("-------",clientesTodos[-1],"-------")
                    print("-------",bTemp,"-------")
                # print(bloques)
                # print(info)
    return render_template("buscar.html",bloques=bloques,info=info)
@app.route("/guardar",methods=["GET","POST"])
def guardar():
    exito=0
    print(request.form.get("name"))
    if request.form.get("name") is not None:
        name=request.form
        print(name)
        # # creo lista de las enfermedades recibidas en la forma
        newCliente=d.nuevoTodict(name)
        print(newCliente)
        # # reviso si existe el cliente o no para "agregarlo"
        if d.existe(name,clientesTodos) and d.existe(name,bc.unconfirmed_transactions):
            print("no hay, no existe")
            newCliente["enfermedades"]=",".join(newCliente["enfermedades"])
            bc.unconfirmed_transactions.append(newCliente)
            print(bc.unconfirmed_transactions)
            exito=1

        else:
            print("existe")
            exito=0

    else:
        exito=2    
    return render_template("guardar.html",success=exito)
@app.route("/minar",methods=["GET","POST"])
def minar():
    if len(bc.unconfirmed_transactions)==0 and (request.form.get("name") is None):
        return render_template("minar.html",success=1)
    if request.form.get("name") is not None:
        name=request.form
        newCliente=d.nuevoTodict(name)
        # # reviso si existe el cliente o no para "agregarlo"

        if d.existe(name,clientesTodos) :
            print("no hay, no existe")
            clientData=d.dicTostring(newCliente)
            bc.add_block(clientData)
            clientesTodos.append(newCliente)
            indexTodos.append({"indice":bc.chain[-1].index,"cedula":newCliente["cedula"]})
            bc.printChainConfirmed()
            for i in range(len(bc.unconfirmed_transactions)):
                if bc.unconfirmed_transactions[i]["cedula"]==name["cedula"]:
                    bc.unconfirmed_transactions.pop(i)
                    # temp=bc.unconfirmed_transactions[i+1:]
                    # bc.unconfirmed_transactions=bc.unconfirmed_transactions[0:i]
                    # if len(temp)!=0:
                    #     bc.unconfirmed_transactions.join(temp)

            print(clientData)

    return render_template("minar.html",success=0,info=bc.unconfirmed_transactions)
@app.route("/verificar",methods=["GET","POST"])
def verificar():
    if request.form.get("name") is not None:
        name=request.form
        list=[]
        h=bc.chain[int(name["name"])].verificarHash()
        for i in indexTodos:
            if int(name["name"])== i["indice"]:
                # list=i
                for j in clientesTodos:
                    if j["cedula"]==i["cedula"]:
                        # list=j
                        return render_template("verificar.html",var=0,bloques=bc.chain[int(name["name"])],info=j,h=h)
        # d.getInfo(i,indexTodos,clientesTodos)


    return render_template("verificar.html",var=1,bloques=bc.chain[1:],info=clientesTodos)



#
# # if __name__ == "__main__":
# #     socketio.run(app)
