from flask import Flask, request, Response
import requests
import argparse

# Crear instancia de Flask
app = Flask(__name__)

# Cache básico
cache_store = {}

# Configurar argumentos de la CLI
parser = argparse.ArgumentParser(description="Caching Proxy Server")
parser.add_argument('--port', type=int, default=3000, help="Port to run the proxy on")
parser.add_argument('--origin', type=str, required=True, help="Origin server URL")
parser.add_argument('--clear-cache', action='store_true', help="Clear the cache")

args = parser.parse_args()

# Establecer el servidor de origen
origin_server = args.origin

# Limpiar caché si se solicita
if args.clear_cache:
    cache_store.clear()
    print("Cache cleared.")

@app.route('/<path:url>', methods=['GET'])
def proxy(url):
    full_url = f"{origin_server}/{url}"
    
    if full_url in cache_store:
        response = cache_store[full_url]
        response.headers['X-Cache'] = 'HIT'
        return response
    
    origin_response = requests.get(full_url)
    flask_response = Response(origin_response.content, status=origin_response.status_code)
    flask_response.headers['X-Cache'] = 'MISS'
    cache_store[full_url] = flask_response
    
    return flask_response

if __name__ == '__main__':
    app.run(port=args.port)
