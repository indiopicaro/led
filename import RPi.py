import RPi.GPIO as GPIO
import requests
from datetime import datetime

led_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)


api_url = 'https://cpro.cl/paeva3/registrar_datos.php'


def encender_led():
    GPIO.output(led_pin, GPIO.HIGH)
    registrar_estado_led(1)


def apagar_led():
    GPIO.output(led_pin, GPIO.LOW)
    registrar_estado_led(0)


def enviar_estado_led(estado):
    grupo = "10"
    momento = datetime.now()
    fecha = momento.strftime("%Y-%m-%d")
    hora = momento.strftime("%H:%M:%S")
    datos = {
        "usuario": "pa.eva3",
        "contrasena": "eva3.2023",
        "id_grupo": grupo,
        "fecha": fecha,
        "hora": hora,
        "estado": estado
    }
    try:
        response = requests.post(api_url, json=datos)
        if response.status_code == 200:
            print("Estado del LED registrado en el API.")
        else:
            print("Error al registrar el estado del LED en el API.")
    except requests.exceptions.RequestException as e:
        print("Error de conexión al API:", str(e))


encender_led()

apagar_led()

GPIO.cleanup()
