import Sensores as s
from pymongo import MongoClient
from datetime import datetime as time

def addRegistro():
    valores = s.Sensores()    
    datos = valores.getTemp_Hum()
    for x in datos:
        humedad = x[0]
        temperatura = x[1]
    sPIR = valores.getDistanciapir()
    ultrasonico = valores.getDistancia()
    #client = MongoClient("mongodb+srv://admin:12ab34cd@cluster.m4smi.mongodb.net/Sensores?retryWrites=true&w=majority")
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Bullsito"]
    collist = db.list_collection_names()
    valores = db["Valores"]
    x = time.now()
    format = x.strftime("%c")
    sensores = db["Sensores"]
    tempyhum = sensores.find({"Sensor":"Temperatura y humedad"})
    for x in tempyhum:
        temperaturaid = x["_id"]
        humedadid = temperaturaid
    ultra = sensores.find({"Sensor":"Ultrasonico"})
    for x in ultra:
        ultrasonicoid = x["_id"]
    pir = sensores.find({"Sensor":"PIR"})
    for x in pir:
        pirid = x["_id"]
    if "Valores" in collist:
        nid = valores.find().sort("_id",-1).limit(1)
        for x in nid:
            f = int(x["_id"] +1)
            valores.insert_one({ "_id": f,humedadid: humedad, temperaturaid: temperatura, pirid: sPIR, ultrasonicoid: ultrasonico, "Fecha": format})
            client.close()
    else:
        valores.insert_one({ "_id": 1,humedadid: humedad, temperaturaid: temperatura, pirid: sPIR, ultrasonicoid: ultrasonico, "Fecha": format})
        client.close()

def getValores():
    valores = s.Sensores()    
    datos = valores.getTemp_Hum()
    for x in datos:
        humedad = x[0]
        temperatura = x[1]
    sPIR = valores.getDistanciapir()
    ultrasonico = valores.getDistancia()
    sensores = [humedad, temperatura, sPIR, ultrasonico]
    return sensores
