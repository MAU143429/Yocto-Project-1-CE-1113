from flask import Flask, jsonify, request
from cffi import FFI
import subprocess
from datetime import datetime

app = Flask(__name__)

# Configuración de CFFI para cargar la biblioteca
ffi = FFI()
ffi.cdef("""
    void control_led(int pin, int estado);
    int leer_boton(int pin);
""")
C = ffi.dlopen("./gpio_control.so")

# Endpoint para controlar LEDs
@app.route('/luces/<int:pin>/<estado>', methods=['POST'])
def control_luz(pin, estado):
    estado_int = 1 if estado == "on" else 0
    C.control_led(pin, estado_int)
    return jsonify({"message": f"LED en pin {pin} {estado}"})

# Endpoint para leer botones
@app.route('/puertas/<int:pin>', methods=['GET'])
def leer_puerta(pin):
    estado = C.leer_boton(pin)
    return jsonify({"pin": pin, "estado": "abierta" if estado == 1 else "cerrada"})

# Endpoint para capturar imagen
@app.route('/camara/capturar', methods=['GET'])
def capturar_imagen():
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    image_path = f"static/images/jardin-{timestamp}.jpg"
    subprocess.run(["fswebcam", "-r", "1280x720", "--no-banner", image_path])
    return jsonify({"image_path": f"/static/images/jardin-{timestamp}.jpg"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)