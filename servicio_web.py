
import json

import cnx_base_datos
from flask import Flask, Response, request
from cnx_base_datos import MongoDriver
from datetime import datetime

from bson import json_util
from bson.objectid import ObjectId



app = Flask(__name__)


@app.route("/")
def hello_world():
    '''
    mongodb = MongoDriver()
    response_raw = {
            "INSTITUCION": "cnt",
            "ULTIMO-PRECIO": "10",
            "FECHA_REGISTRO": datetime.now()
            }

    mongodb.insert_record(record=response_raw, username="REGISTROS")
    '''

    mongodb = MongoDriver()

    datos = mongodb.consulta_record(username="REGISTROS")
    # response = json_util.dumps(datos)
    # return Response(response, mimetype="application/json")

    #return Response(json.dumps(datos), mimetype='application/json')

    return "<h2>Hola.. Mi pais Ecuador 2023!</h2>"
    #return datos

@app.route('/ws_datos', methods=['GET'])
def get_ws_datos():
    mongodb = MongoDriver()
    datos = mongodb.consulta_record(username="REGISTROS")
    response = json_util.dumps(datos)
    return Response(response, mimetype="application/json")

@app.route('/ws_datos_id/<id>', methods=['GET'])
def get_ws_datos_id(id):
    mongodb = MongoDriver()
    response_raw = {
            "INSTITUCION": id
            }
    datos = mongodb.consulta_record_one(record=response_raw,username="REGISTROS")
    response = json_util.dumps(datos)
    return Response(response, mimetype="application/json")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)