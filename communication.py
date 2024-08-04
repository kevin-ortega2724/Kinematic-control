import serial
import config

def initialize_arduino():
    """
    Inicializa la conexión con el Arduino.
    Retorna el objeto de conexión serie.
    """
    try:
        arduino = serial.Serial(config.COM_PORT, config.BAUDRATE, timeout=1)
        print(f"Conexión establecida con el Arduino en {config.COM_PORT} a {config.BAUDRATE} baudios.")
        return arduino
    except serial.SerialException as e:
        print(f"Error al abrir el puerto {config.COM_PORT}: {e}")
        return None

def send_command(arduino, command):
    """
    Envía un comando al Arduino.
    """
    if arduino is not None and arduino.isOpen():
        arduino.write(command.encode())
        print(f"Enviando comando: {command}")
    else:
        print("Arduino no está conectado.")

def read_data(arduino):
    """
    Lee datos del Arduino.
    Retorna los datos leídos como string.
    """
    if arduino is not None and arduino.isOpen():
        data = arduino.readline().decode().strip()  # Lee hasta el final de la línea y elimina espacios en blanco
        return data
    else:
        print("Arduino no está conectado.")
        return ""

def close_connection(arduino):
    """
    Cierra la conexión con el Arduino.
    """
    if arduino is not None and arduino.isOpen():
        arduino.close()
        print(f"Conexión con {config.COM_PORT} cerrada.")
    else:
        print("Arduino no está conectado.")