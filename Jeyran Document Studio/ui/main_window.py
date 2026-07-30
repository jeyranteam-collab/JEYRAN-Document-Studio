from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QPixmap, QIcon, QAction
from PySide6.QtWidgets import QMenu
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QFileDialog
from ui.image_viewer import ImageViewer
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QLabel,
    QFrame,
    QStatusBar,
    QToolBar
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        print(">>>> MAIN WINDOW LOADED <<<<")

        self.setWindowTitle("JEYRAN Document Studio Professional")
        self.setAcceptDrops(True)
        self.resize(1600, 900)

        self.create_toolbar()
        self.create_statusbar()
        self.create_layout()
        self.images = []

    def create_toolbar(self):
        toolbar = QToolBar("Main")
        toolbar.setMovable(False)

        addAction = toolbar.addAction("افزودن تصاویر")
        addAction.triggered.connect(self.open_images)
        toolbar.addAction("افزودن پوشه")
        deleteAction = toolbar.addAction("حذف")
        deleteAction.triggered.connect(self.delete_image)
        toolbar.addSeparator()
        toolbar.addAction("کراپ")
        toolbar.addAction("چرخش")
        toolbar.addSeparator()
        toolbar.addAction("PDF")
        toolbar.addAction("چاپ")

        self.addToolBar(toolbar)

    def create_statusbar(self):
        status = QStatusBar()
        status.showMessage("آماده")
        self.setStatusBar(status)

    def create_layout(self):
        central = QWidget()
        layout = QHBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setIconSize(QSize(100,100))
        self.listWidget.setMinimumWidth(250)

        self.preview = ImageViewer()

        self.settings = QListWidget()
        self.settings.addItems([
            "Brightness",
            "Contrast",
            "Gamma",
            "Sharpen",
            "Rotate",
            "Crop"
        ])
        self.settings.setMinimumWidth(250)


        layout.addWidget(self.listWidget)
        layout.addWidget(self.preview, 1)
        layout.addWidget(self.settings)

        central.setLayout(layout)
        self.setCentralWidget(central)
 
    def open_images(self):

        files, _ = QFileDialog.getOpenFileNames(
            self,
            "انتخاب تصاویر",
            "",
            "Images (*.jpg *.jpeg *.png *.bmp *.tif *.tiff)"
        )

        if not files:
            return

        self.images = files

        self.listWidget.clear()

        for f in files:
            item = QListWidgetItem(QIcon(f), f.split("/")[-1])
            self.listWidget.addItem(item)

        self.listWidget.currentRowChanged.connect(self.show_image)
        self.listWidget.setCurrentRow(0)


    def show_image(self, row):

        if row < 0:
            return

        self.preview.load_image(self.images[row])
    def delete_image(self):

        row = self.listWidget.currentRow()

        if row < 0:
            return

        self.listWidget.takeItem(row)
        self.images.pop(row)

        if self.images:
            self.listWidget.setCurrentRow(0)
        else:
            self.preview.clear()
        def dragEnterEvent(self, event):

    if event.mimeData().hasUrls():
        event.acceptProposedAction()


def dropEvent(self, event):

    files = []

    for url in event.mimeData().urls():
        files.append(url.toLocalFile())

    if not files:
        return

    self.images = files

    self.listWidget.clear()

    for f in files:
        item = QListWidgetItem(QIcon(f), f.split("/")[-1])
        self.listWidget.addItem(item)

    self.listWidget.setCurrentRow(0)    


