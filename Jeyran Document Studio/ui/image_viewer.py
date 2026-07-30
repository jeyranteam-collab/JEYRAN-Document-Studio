from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImageViewer(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText("Preview")
        self.setStyleSheet("""
            QLabel{
                border:1px solid #808080;
                background:white;
            }
        """)

        self.scale_factor = 1.0
        self.pix = None

    def load_image(self, filename):

        self.pix = QPixmap(filename)
        self.scale_factor = 1.0
        self.update_view()

    def update_view(self):

        if self.pix is None:
            return

        pix = self.pix.scaled(
            self.pix.size()*self.scale_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(pix)

    def wheelEvent(self, event):

        if self.pix is None:
            return

        if event.angleDelta().y() > 0:
            self.scale_factor *= 1.10
        else:
            self.scale_factor *= 0.90

        self.update_view()