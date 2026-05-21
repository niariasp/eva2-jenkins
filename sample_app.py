from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Aplicacion Docker Jenkins funcionando en puerto 9999</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
