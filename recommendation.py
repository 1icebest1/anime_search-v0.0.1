from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class AnimeCard(QFrame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.data = data
        self.setup_ui()
        self.setCursor(Qt.PointingHandCursor)

    def setup_ui(self):
        self.setFixedSize(200, 300)
        self.setStyleSheet("""
            background: #404040;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        """)


        container = QWidget(self)
        container.setGeometry(0, 0, 200, 300)


        grid = QGridLayout(container)
        grid.setContentsMargins(0, 0, 0, 0)


        img_label = QLabel()
        img_label.setPixmap(QPixmap(self.data["image"]).scaled(
            200, 300,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        ))
        grid.addWidget(img_label, 0, 0)


        text_label = QLabel(self.data["title"])
        text_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        text_label.setStyleSheet("""
            color: black;
            font-size: 20px;
            font-weight: bold;
            background: rgba(0, 0, 0, 0);
            padding: 10px;
        """)
        text_label.setWordWrap(True)
        grid.addWidget(text_label, 0, 0)

class RecommendationPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        layout = QVBoxLayout(self)

        self.anime_list = [
            {"image": "test.png", "title": "1"},
            {"image": "test.png", "title": "2"},
            {"image": "test.png", "title": "3"},
            {"image": "test.png", "title": "4"},
            {"image": "test.png", "title": "5"},
            {"image": "test.png", "title": "6"}
        ]

        grid = QGridLayout()
        for i, anime in enumerate(self.anime_list[:8]):
            grid.addWidget(AnimeCard(self, anime), i // 4, i % 4)

        layout.addLayout(grid)