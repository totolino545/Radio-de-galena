from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS
from servicios import*  # noqa: F403
from metadatos import*  # noqa: F403

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para toda la app

@app.route('/')
def index():
    page = int(request.form.get('page', 1))
    tags=Servicios.todos_los_tags()    
    return render_template('estaciones/index.html', tags=tags, page=page)


@app.route('/', methods=['POST'])
def cargar_estaciones():
        name = request.form.get('myinput', 'blues')               
        limit = request.form.get('limit', 10)
        estaciones, total  = Servicios.cargar_estaciones(name, limit)
        print(total)
        tags = Servicios.todos_los_tags()
        return render_template('estaciones/index.html', estaciones=estaciones, tags=tags, limit=limit)

@app.route('/reproduciendo', methods=['GET'])
@cross_origin()  # Habilita CORS para esta ruta
def cargar_metadata():
        url = request.args.get('url')              
        metadato = Metadatos.obtener_metadatos_shoutcast(url)
        print(metadato)
        # Renderizar alguna respuesta o redirigir
        return jsonify(metadato)

@app.route('/radios', methods=['GET'])
def radios():
    genero = request.args.get('genero', 'blues')
    resultado, status = Servicios.obtener_radios(genero)
    return jsonify(resultado), status

@app.route('/radio/<radio_id>', methods=['GET'])
def radio_por_id(radio_id):
    resultado, status = Servicios.obtener_radio_por_id(radio_id)
    return jsonify(resultado), status

@app.route('/metadato/<id>', methods=['GET'])
def metadata_por_id(id):
    resultado, status = Servicios.obtener_metadata_por_id(id)
    return jsonify(resultado), status

if __name__ == '__main__':
    app.run(debug=True)
