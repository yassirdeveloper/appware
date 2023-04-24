from PySide6.QtWidgets import QErrorMessage, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class ErrorWidget(QErrorMessage):
    def __init__(self, exception):
        super().__init__()

        self.text = QLabel(exception.message, alignment=Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.exec()
