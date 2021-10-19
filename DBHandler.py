from pymongo import MongoClient
from Estudiante import *


class DBHandler(object):

    def __init__(self):
        self.db = self.conectar()
        self.coleccion = self.db.get_collection('estudiantes')



    def conectar(self):
        client = MongoClient(
            host='infsalinas.sytes.net:10450',  # <-- IP and port go here
            serverSelectionTimeoutMS=3000,  # 3 second timeout
            username="profe2",
            password="mypass1234",
            authSource='profe2'
        )
        db = client.get_database('profe2')

        return db

    def insertar(self, estudiante):
        try:
            self.coleccion.insert(estudiante.__dict__)
            return True
        except Exception as e:
            print('No se puede insertar:',e)
            return False


    def obtener(self, dni):
        try:
            user = self.coleccion.find_one({'_id':dni})
        except Exception as e:
            print(e)

        return user


        #for data in user:
            #estudiante = Estudiante(**data)
            #print(data)
            #print(estudiante.__dict__)