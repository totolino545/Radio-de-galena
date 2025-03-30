#CONTROLADOR
from flask import jsonify, request
import requests

class Servicios:
    
    def todos_los_tags():
            url = 'https://radio.beffy.de/json/tags/?hidebroken=true&reverse=true&order=stationcount'
            response = requests.get(url)
            data = response.json()
            return data
    
    def buscar_estaciones(name):
            url = 'https://radio.beffy.de/json/stations/search?name={name}&hidebroken=true&limit={limit}&&name=clickcount&reverse=true'
            response = requests.get(url)
            data = response.json()
            return data
    
    def cargar_estaciones(name, limit=10):
                url = f'https://radio.beffy.de/json/stations/search?name={name}&hidebroken=true&&limit={limit}&reverse=true&order=clickcount'
                response = requests.get(url)
                data = response.json()
                total = len(data)  # Ajusta esto según tu API
                return data, total
