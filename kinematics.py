import numpy as np
import config
import matplotlib.pyplot as plt

def grados_a_cuentas(grados):
    """
    Convierte grados a cuentas para controlar los servos.
    """
    cuentas = (grados * config.CONVERSION_GRADOS_A_CUENTAS) + config.DESFASE_GRADOS  # Asume un desfase de 180 grados como en el script de MATLAB
    return np.round(cuentas).astype(int)  # Redondea al entero más cercano

def cuentas_a_grados(cuentas):
    """
    Convierte cuentas a grados.
    """
    grados = (cuentas - config.DESFASE_GRADOS) / config.CONVERSION_GRADOS_A_CUENTAS
    return grados

def cinematica_inversa(q1, q4):
    """
    Ejemplo de función de cinemática inversa.
    Calcula las posiciones de los servos basándose en los ángulos dados.
    """
    # Parámetros del mecanismo
    l1, l2, l3, l4, l5 = config.l1, config.l2, config.l3, config.l4, config.l5
    xe = config.l5  # Asume que xe es una constante, ajusta según sea necesario
    
    # Cálculo de cinemática inversa simplificado
    e = (l1 * np.sin(np.radians(q1)) - l4 * np.sin(np.radians(q4))) / (xe + l4 * np.cos(np.radians(q4)) - l1 * np.cos(np.radians(q1)))
    f = (l1**2 + l3**2 - l2**2 - l4**2 - xe**2 - 2 * l4 * xe * np.cos(np.radians(q4))) / (2 * l1 * np.cos(np.radians(q1)) - 2 * l4 * np.cos(np.radians(q4)) - 2 * xe)
    d = e**2 + 1
    g = 2 * e * f - 2 * e * l1 * np.sin(np.radians(q1))
    h = f**2 - 2 * f * l1 * np.cos(np.radians(q1)) + l1**2 - l2**2
    yc_v = (-g + np.sqrt(g**2 - 4 * d * h)) / (2 * d)
    xc_v = e * yc_v + f
    
    return xc_v, yc_v

def graficar_trayectoria(xc_v, yc_v):
    """
    Grafica la trayectoria del mecanismo.
    """

    
    plt.scatter(xc_v, yc_v, color='blue')
    plt.xlabel('Posición eje X [mm]')
    plt.ylabel('Posición eje Y [mm]')
    plt.title('Trayectoria del Mecanismo')
    plt.grid(True)
    plt.show()
# def move_servos(arduino, q1, q4):
#     """
#     Calcula las cuentas y mueve los servos.
#     """
#     cuentas = kinematics.grados_a_cuentas(q1, q4)
#     # Envía cuentas al Arduino
#     send_command(arduino, f"m{cuentas}")
    
# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    q1 = 45  # Ángulo para el servo 1 en grados
    q4 = 30  # Ángulo para el servo 4 en grados
    xc_v, yc_v = cinematica_inversa(q1, q4)
    print(f"Posiciones calculadas: xc_v={xc_v}, yc_v={yc_v}")
    graficar_trayectoria(xc_v, yc_v)