# Caching Proxy Server

## Overview
This is a lightweight command-line interface (CLI) tool designed to cache responses from origin servers. By forwarding requests to a specified origin and caching the responses, it enhances the efficiency of repeated requests, reducing latency and server load.

## Features
- Start the proxy server using CLI commands with customizable port and origin URL.
- Cache responses from the origin server to serve future requests faster.
- Include headers to indicate whether the response was served from the cache or the origin server.
- Clear the cached data with a simple command.

## Technologies Used
- **Python**: The primary programming language for building the server.
- **Flask**: A lightweight web framework to handle HTTP requests and responses.
- **pipenv**: A dependency manager for Python that creates a virtual environment for the project.

## How to Use
1. **Start the Server**:
   ```bash
   python app.py --port <number> --origin <url>
   #for example:
   python app.py --port 3000 --origin http://dummyjson.com

## Caching Mechanism

The caching mechanism is designed to optimize the response times for repeated requests. It utilizes two key concepts:

- **Cache Miss**: If the requested resource is not found in the cache, the proxy server forwards the request to the origin server. The response from the origin server is then cached for future requests. Responses served from the origin server will include the header:
  
curl -I http://localhost:3000/products
HTTP/1.1 200 OK
Server: Werkzeug/3.0.4 Python/3.10.12
Date: Fri, 04 Oct 2024 14:08:15 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 44275
X-Cache: MISS
Connection: close

- **Cache Hit**: When a request is made to the caching proxy server, if the response is available in the cache, it is served directly from there. This results in faster response times and reduces the load on the origin server. Responses served from the cache will include the header:
  
HTTP/1.1 200 OK
Server: Werkzeug/3.0.4 Python/3.10.12
Date: Fri, 04 Oct 2024 14:08:22 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 44275
X-Cache: HIT
Connection: close


## Idea from: 
https://roadmap.sh/projects/caching-server
