# FastAPI
from fastapi import FastAPI

# App
app = FastAPI()


@app.get('/')
async def hola():
    print('Hola mundo')
    return {
        'Hello': 'Este es un cambioo',
    }
