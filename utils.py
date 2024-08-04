import numpy as np
import pandas as pd
import csv
import os

def leer_datos_csv(archivo):
    """
    Lee datos de un archivo CSV y retorna un DataFrame de pandas.
    """
    if os.path.isfile(archivo):
        return pd.read_csv(archivo)
    else:
        raise FileNotFoundError(f"El archivo {archivo} no existe.")

def escribir_datos_csv(datos, archivo):
    """
    Escribe datos en un archivo CSV.
    """
    if isinstance(datos, pd.DataFrame):
        datos.to_csv(archivo, index=False)
    elif isinstance(datos, np.ndarray):
        np.savetxt(archivo, datos, delimiter=',')
    else:
        raise TypeError("Datos deben ser un DataFrame de pandas o un ndarray de numpy.")

def grados_a_cuentas(grados, conversion=11.37, desfase=180):
    """
    Convierte grados a cuentas para controlar los servos.
    """
    cuentas = (grados + desfase) * conversion
    return np.round(cuentas).astype(int)

def cuentas_a_grados(cuentas, conversion=11.37, desfase=180):
    """
    Convierte cuentas a grados.
    """
    grados = (cuentas / conversion) - desfase
    return grados

def convertir_tiempo_milisegundos_a_segundos(tiempo_milisegundos):
    """
    Convierte tiempo de milisegundos a segundos.
    """
    return tiempo_milisegundos / 1000.0

def convertir_segundos_a_milisegundos(tiempo_segundos):
    """
    Convierte tiempo de segundos a milisegundos.
    """
    return tiempo_segundos * 1000.0

def encontrar_puerto_serie(dispositivo):
    """
    Intenta encontrar el puerto serie al que está conectado el dispositivo.
    Retorna el puerto como string o None si no se encuentra.
    """
    # Este es un ejemplo, necesitarás implementar la lógica específica para tu sistema operativo y dispositivo
    puertos_posibles = ['/dev/ttyUSB0', '/dev/ttyUSB1', 'COM3', 'COM4']  # Ejemplo de puertos
    for puerto in puertos_posibles:
        if dispositivo_conectado(puerto):  # Implementa esta función según tu lógica de detección
            return puerto
    return None

def dispositivo_conectado(puerto):
    """
    Verifica si un dispositivo está conectado en el puerto dado.
    Retorna True si está conectado, False de lo contrario.
    """
    # Implementa la lógica para verificar la conexión del dispositivo
    return False

def guardar_datos_excel(datos, archivo, hoja='Datos'):
    """
    Guarda datos en un archivo de Excel.
    """
    if isinstance(datos, pd.DataFrame):
        with pd.ExcelWriter(archivo, engine='xlsxwriter') as writer:
            datos.to_excel(writer, sheet_name=hoja)
    else:
        raise TypeError("Datos deben ser un DataFrame de pandas.")

def leer_datos_excel(archivo, hoja=0):
    """
    Lee datos de un archivo de Excel y retorna un DataFrame de pandas.
    """
    return pd.read_excel(archivo, sheet_name=hoja)

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    datos = pd.DataFrame({'Tiempo': [1, 2, 3], 'Valor': [4, 5, 6]})
    escribir_datos_csv(datos, 'ver.csv')
    datos_leidos = leer_datos_csv('01_RotaryMotor1 - Mango_Cuchillo_1x6s.csv')
    print(datos_leidos)