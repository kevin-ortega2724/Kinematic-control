# Parámetros del sistema
TIEMPO_MUESTREO_MINIMO = 40  # milisegundos
TAMANO_MAXIMO_VECTOR = 750  # muestras
RANGO_ANGULAR = (0, 4095)  # 0-4095 equivalentes a 0-360 grados
RANGO_VELOCIDAD = (0, 511)  # 0-511 equivalentes a 0-360 grados/seg
CONVERSION_GRADOS_A_CUENTAS = 11.37  # 11.37 cuentas es 1 grado
CONVERSION_CUENTAS_A_GRADOS = 0.088  # 1 cuenta son 0.088 grados
CONVERSION_GRADOS_SEG_A_CUENTAS = 1.419  # 1.419 cuentas es 1 grado/seg
CONVERSION_CUENTAS_A_GRADOS_SEG = 0.704  # 1 cuenta son 0.704 grados/seg

# Longitudes de las barras del mecanismo
l1 = 95  # mm
l2 = 85  # mm
l3 = 85  # mm
l4 = 95  # mm
l5 = 75  # mm

# Estados iniciales
xc_v = 0
yc_v = 0

# Vectores iniciales
vector_angulos_izq_GR = 0
vector_angulos_encoder_izq_G = 0
vector_velocidades_izq_GR = 0
vector_velocidades_encoder_izq_G = 0
vector_angulos_der_GR = 0
vector_angulos_encoder_der_G = 0
vector_velocidades_der_GR = 0
vector_velocidades_encoder_der_G = 0
vector_angulos_izq_SR = 0
vector_angulos_encoder_izq_SR = 0
vector_velocidades_izq_SR = 0
vector_velocidades_encoder_izq_SR = 0
vector_angulos_der_SR = 0
vector_angulos_encoder_der_SR = 0
vector_velocidades_der_SR = 0
vector_velocidades_encoder_der_SR = 0

# Tamaños de vectores y tiempos de muestreo iniciales
tamano_vector_angulos_izq = 1
tamano_vector_angulos_der = 2
tamano_vector_velocidades_izq = 3
tamano_vector_velocidades_der = 4
t_muestreo_angulos_izq = 5
t_muestreo_angulos_der = 6
t_muestreo_velocidades_izq = 7
t_muestreo_velocidades_der = 8
t_simulacion_angulos_izq = 9
t_simulacion_angulos_der = 10
t_simulacion_velocidades_izq = 11
t_simulacion_velocidades_der = 12
k = 0
t_muestreo = 0
t_simulacion = 0
tamano_vector = 0

# Estados de los botones y banderas
button_state_boton_detener = 0
bandera_t_muestreo = 0
bandera_t_simulacion = 0
bandera_tamano_vector = 0
bandera_servos_cargados = 0
bandera_calculada_cinematica = 0
bandera_boton_angulos_izq = 0
bandera_boton_velocidades_izq = 0
bandera_boton_angulos_der = 0
bandera_boton_velocidades_der = 0
bandera_trayectoria_ejecutada = 0

# Puerto serie para Arduino
COM_PORT = 'COM_PORT'  # Este valor debe ser reemplazado por el puerto real
BAUDRATE = 1000000

# Rutas de archivos de audio
AUDIO_COMUNICADO = 'sistema_comunicado.wav'
AUDIO_CALCULANDO = 'calculando_cinematica.wav'
AUDIO_FINALIZADO = 'proceso_finalizado.wav'
AUDIO_FALLIDO = 'calculo_fallido.wav'
AUDIO_CARGA_EXITOSA = 'carga_exitosa.wav'
AUDIO_CARGA_FALLIDA = 'carga_fallida.wav'

# Ruta para guardar datos
RUTA_DATOS_ESTADISTICOS = 'Datos_Estadisticos.xls'