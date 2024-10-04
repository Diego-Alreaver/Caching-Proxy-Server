# Caching Proxy Server

## Overview
The Caching Proxy Server is a lightweight command-line interface (CLI) tool designed to cache responses from origin servers. By forwarding requests to a specified origin and caching the responses, it enhances the efficiency of repeated requests, reducing latency and server load.

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
   for example:
   python app.py --port 3000 --origin http://dummyjson.com
