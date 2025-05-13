#CONTROLADOR
from flask import jsonify, request
import requests

class Servicios:
    
    def todos_los_tags():
        url = f'http://152.53.85.3/json/tags/?hidebroken=true&reverse=true&order=stationcount'
        response = requests.get(url)
        data = response.json()
        return data
    
    def buscar_estaciones(name):
        url = f'http://152.53.85.3/json/stations/search?name={name}&hidebroken=true&limit={limit}&&name=clickcount&reverse=true'
        response = requests.get(url)
        data = response.json()
        return data
    
    def cargar_estaciones(name, limit=10):
        url = f'http://152.53.85.3/json/stations/search?name={name}&hidebroken=true&&limit={limit}&reverse=true&order=clickcount'
        response = requests.get(url)
        data = response.json()
        total = len(data)  # Ajusta esto según tu API
        return data, total

    def obtener_radios(genero='blues'):
        url = f'https://zeno.fm/api/stations/?query={genero}&limit=200&genre=Music'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json(), 200
        except requests.RequestException as e:
            return {'error': str(e)}, 500

    def obtener_radio_por_id(radio_id):
        url = f'https://zeno.fm/api/stations/{radio_id}/'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json(), 200
        except requests.RequestException as e:
            return {'error': str(e)}, 500

    def obtener_metadata_por_id(id):
    url = f'https://api.zeno.fm/mounts/metadata/subscribe/{id}/'
    try:
        with requests.get(url, stream=True, timeout=10) as response:
            response.raise_for_status()

            for line in response.iter_lines(decode_unicode=True):
                if line.startswith("data:"):
                    # Extraer la parte JSON del mensaje
                    data_str = line.removeprefix("data:").strip()
                    try:
                        data = json.loads(data_str)
                        stream_title = data.get("streamTitle", "")
                        if " - " in stream_title:
                            artist, song = stream_title.split(" - ", 1)
                        else:
                            artist, song = "Desconocido", stream_title

                        return {
                            "artist": artist.strip(),
                            "song": song.strip()
                        }, 200
                    except Exception as e:
                        return {"error": f"Error parseando JSON: {e}"}, 500

        return {"error": "No se recibieron metadatos"}, 404

    except requests.RequestException as e:
        return {"error": str(e)}, 500

