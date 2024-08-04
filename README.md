# Kinematic-control

Función CalcularCinemáticaInversa(q1, q4):

    // q1 y q4 son los ángulos de los servos en grados
    // Parámetros del mecanismo se obtienen de la configuración global
    l1, l2, l3, l4, l5 = ObtenerParámetrosMecanismo()
    xe = l5  // Asume que xe es una constante, ajusta según sea necesario

    // Cálculo de cinemática inversa simplificado
    e = (l1 * sin(q1) - l4 * sin(q4)) / (xe + l4 * cos(q4) - l1 * cos(q1))
    f = (l1^2 + l3^2 - l2^2 - l4^2 - xe^2 - 2 * l4 * xe * cos(q4)) / (2 * l1 * cos(q1) - 2 * l4 * cos(q4) - 2 * xe)
    d = e^2 + 1
    g = 2 * e * f - 2 * e * l1 * sin(q1)
    h = f^2 - 2 * f * l1 * cos(q1) + l1^2 - l2^2
    yc_v = (-g + sqrt(g^2 - 4 * d * h)) / (2 * d)
    xc_v = e * yc_v + f

    Retornar xc_v, yc_v

Función EjecutarTrayectoria(arduino, xc_v, yc_v):
    // xc_v y yc_v son las posiciones calculadas por la cinemática inversa
    // Convertir posiciones a cuentas para controlar los servos
    cuentas1 = ConvertirGradosACuentas(xc_v)
    cuentas4 = ConvertirGradosACuentas(yc_v)

    // Enviar cuentas al Arduino para mover los servos
    EnviarComando(arduino, "m" + cuentas1)
    EnviarComando(arduino, "m" + cuentas4)

    // Esperar a que los servos alcancen la posición
    EsperarHastaQueServosAlcanzenPosición(arduino)

    // Leer datos de los encoders para verificar la precisión
    datosEncoder = LeerDatosEncoders(arduino)

    // Guardar datos en archivo Excel para análisis posterior
    GuardarDatosExcel(datosEncoder, "Datos_Estadisticos.xls")

Función ConvertirGradosACuentas(grados):
    // Utiliza la conversión definida en la configuración
    conversion = ObtenerConversiónGradosACuentas()
    desfase = ObtenerDesfaseGrados()
    cuentas = (grados + desfase) * conversion
    Retornar Redondear(cuentas)

Función EnviarComando(arduino, comando):
    // Envia un comando al Arduino a través de la conexión serie
    arduino.write(comando.encode())

Función LeerDatosEncoders(arduino):
    // Lee los datos de los encoders del Arduino
    datos = arduino.readline().decode().strip()
    Retornar datos

Función GuardarDatosExcel(datos, archivo):
    // Guarda los datos en un archivo Excel
    CrearDataFrameConDatos(datos)
    GuardarDataFrameEnExcel(archivo)