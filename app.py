from flask import Flask
from Conexión.conexion import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Aplicación Flask funcionando!"

@app.route('/test_db')
def test_db():
    conn = get_connection()
    if conn:
        conn.close()
        return "Conexión a MySQL exitosa"
    else:
        return "Error al conectar con MySQL"

if __name__ == '__main__':
    app.run(debug=True)