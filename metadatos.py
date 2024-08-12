import requests

class Metadatos:

    def obtener_metadatos_shoutcast(url):
        headers = {
            'Icy-MetaData': '1',  # Solicita metadatos ICY
            'User-Agent': 'Mozilla/5.0'  # Simula una solicitud de navegador
        }
        
        try:
            response = requests.get(url, headers=headers, stream=True)
            
            # Verifica si el servidor responde con metadatos ICY
            if 'icy-metaint' in response.headers:
                metaint = int(response.headers['icy-metaint'])
                for chunk in response.iter_content(chunk_size=metaint + 255):
                    if len(chunk) < metaint:
                        continue
                    metadata = chunk[metaint:].split(b'\0', 1)[0]
                    metadata_str = metadata.decode('utf-8', errors='replace')
                    
                    # Extraer y limpiar los metadatos
                    title = metadata_str.split('StreamTitle=')[1].split(';')[0]
                    title = title.strip("'")

                    return title
            else:
                print("No se encontraron metadatos ICY en la transmisión.")
        except Exception as e:
            print("Error al intentar leer metadatos:", e)


