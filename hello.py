from flask import Flask
app = Flask(__name__) #le paso el nombre de nuestro fichero, aplcación

@app.route('/')
def hello_world():
    return 'Hola, mundo'

