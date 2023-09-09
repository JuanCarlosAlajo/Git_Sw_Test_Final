
import json
from flask import Flask, Response, request
from db import MongoDriver
from datetime import datetime

from bson import json_util



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
    return "<h2>Hola.. Mi pais Ecuador 2023!</h2>"


@app.route("/datos", methods=['GET'])
def ws_consultar_todo():
     mongodb = MongoDriver()

     datos=mongodb.consulta_record(username="CONSULTA")
     #users = mongo.db.users.find()



     response = json_util.dumps(datos)
     return Response(response, mimetype="application/json")






if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)