from flask import Flask
from fastapi import FastAPI
import uvicorn
import threading

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Hello from Jenkins + Flask!"

@flask_app.route('/health')
def health():
    return {"status": "ok"}

# FastAPI app
fastapi_app = FastAPI()

@fastapi_app.get('/')
def fastapi_home():
    return {"message": "Hello from Jenkins + FastAPI!"}

@fastapi_app.get('/health')
def fastapi_health():
    return {"status": "ok"}

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

def run_fastapi():
    uvicorn.run(fastapi_app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    t1 = threading.Thread(target=run_flask)
    t2 = threading.Thread(target=run_fastapi)
    t1.start()
    t2.start()
