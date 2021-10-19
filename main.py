
from flask import Flask, jsonify, request, Response
from Estudiante import *
from DBHandler import *
app = Flask(__name__)


@app.route('/students', methods=['POST'])
def insert_student():
    print(request.json)
    estudiante = Estudiante(**request.json)
    okinsert = DBHandler().insertar(estudiante)
    #JsonHandler().nuevoEstudiante(estudiante)
    return {'result': okinsert}



if __name__ == '__main__':
    app.run(debug=True, port=8068, host='infsalinas.systes.net')
    # handler = DBHandler()
    # estudiante = Estudiante('23421','Rafa',32,'segundo')
    #
    # handler.insertar(estudiante)
    # user = handler.obtener('23421')
    # if(user==None):
    #     print('Estudiante no encontrado')
    # else:
    #     print('Estudiante encontrado: ',user)
