from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
import numpy as np

class PlottingWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PlottingWindow, self).__init__(parent)
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self)
        
        # Configura el layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        # Configura el timer para actualizar la gráfica
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # Actualiza cada 100 ms
        
        # Datos de ejemplo
        self.xc_v = np.random.rand(100) * 200 - 100  # Posiciones x aleatorias
        self.yc_v = np.random.rand(100) * 200 - 100  # Posiciones y aleatorias
        self.index = 0
        
        # Configura el gráfico inicial
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim([-200, 200])
        self.ax.set_ylim([-200, 200])
        self.ax.set_aspect('equal', adjustable='box')
        self.line, = self.ax.plot([], [], 'ro-')
        
    def update_plot(self):
        """Actualiza la gráfica con nuevos datos."""
        if self.index < len(self.xc_v):
            self.line.set_data(self.xc_v[:self.index], self.yc_v[:self.index])
            self.canvas.draw()
            self.index += 1
        else:
            self.timer.stop()

def main():
    app = QApplication(sys.argv)
    window = PlottingWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()