from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout, QScrollArea
from PySide6.QtGui import QPixmap, QColor, QFont
from PySide6.QtCore import Qt


class MediaCard(QFrame):
    def __init__(self, parent, data):
        super().__init__()
        self.parent = parent
        self.data = data
        self.setup_ui()
        self.setCursor(Qt.PointingHandCursor)

    def setup_ui(self):
        # Основные настройки карточки
        self.setFixedSize(280, 360)
        self.setStyleSheet("""
            background: #202020;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Блок изображения (Box n2)
        img_label = QLabel()
        img_label.setFixedSize(280, 280)
        img_label.setPixmap(QPixmap(self.data["image"]).scaled(
            280, 280,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        ))
        img_label.setStyleSheet("border-radius: 15px 15px 0 0;")
        layout.addWidget(img_label)

        # Текстовый контейнер (Box n1)
        text_frame = QFrame()
        text_frame.setStyleSheet("""
            background: rgba(40, 40, 40, 0.8);
            border-radius: 0 0 15px 15px;
        """)
        text_layout = QVBoxLayout(text_frame)
        text_layout.setContentsMargins(15, 10, 15, 10)

        title = QLabel(self.data["title"])
        title.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: 500;
            padding: 8px 0;
        """)
        title.setAlignment(Qt.AlignCenter)
        title.setWordWrap(True)

        text_layout.addWidget(title)
        layout.addWidget(text_frame)

    def enterEvent(self, event):
        self.setStyleSheet("background: #282828; border-color: rgba(255, 255, 255, 0.3);")

    def leaveEvent(self, event):
        self.setStyleSheet("background: #202020; border-color: rgba(255, 255, 255, 0.1);")


class ExplorePage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        # Пример данных
        sample_data = [
            {"image": "covers/1.jpg", "title": "Космічні Мандрівники"},
            {"image": "covers/2.jpg", "title": "Таємничий Ліс"},
            # + 4-6 аналогичных элементов
        ]

        # Сетка карточек
        grid = QGridLayout()
        grid.setHorizontalSpacing(25)
        grid.setVerticalSpacing(25)

        for i, item in enumerate(sample_data):
            row = i // 3
            col = i % 3
            grid.addWidget(MediaCard(self, item), row, col)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        content.setLayout(grid)
        scroll.setWidget(content)

        layout.addWidget(scroll)