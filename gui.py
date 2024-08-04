from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
from utils import leer_datos_csv, escribir_datos_csv

class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRectItem(0, 0, 400, 400, 400)  # Define el área de la escena
        self.setSceneRectItem(0, 0, 400, 400)  # Define el área visible de la escena

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz Gráfica de Usuario")
        self.setGeometry(100, 100, 800, 600)  # Tamaño de la ventana

        # Crear el canvas para la gráfica
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.setGeometry(0, 0, 400, 400)  # Ajusta el tamaño del canvas al área de la escena

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)

        # Botones
        self.btn_cargar_datos = QPushButton("Cargar Datos")
        self.btn_cargar_datos.clicked.connect(self.cargar_datos_clicked)
        self.layout.addWidget(self.btn_cargar_datos)

        self.btn_iniciar_simulacion = QPushButton("Iniciar Simulación")
        self.btn_iniciar_simulacion.clicked.connect(self.iniciar_simulacion_clicked)
        self.layout.addWidget(self.btn_iniciar_simulacion)

        # Etiquetas para mostrar información
        self.label_status = QLabel("Estado: Detenido")
        self.layout.addWidget(self.label_status)

    def cargar_datos_clicked(self):
        # Implementa la lógica para cargar datos
        pass

    def iniciar_simulacion_clicked(self):
        # Implementa la lógica para iniciar la simulación
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()