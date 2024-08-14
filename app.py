from flask import Flask, jsonify, request, render_template
from servicios import*  # noqa: F403
from metadatos import*

app = Flask(__name__)

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
def cargar_metadata():
        url = request.args.get('url')              
        metadato = Metadatos.obtener_metadatos_shoutcast(url)
        print(metadato)
        # Renderizar alguna respuesta o redirigir
        return jsonify(metadato)

if __name__ == '__main__':
    app.run(debug=True)
