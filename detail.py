from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt



class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.back_callback = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignCenter)

        btn_back = QPushButton("← Back")
        btn_back.setStyleSheet("color: white; font-size: 16px; border: none;")
        btn_back.clicked.connect(self.go_back)
        layout.addWidget(btn_back, alignment=Qt.AlignLeft)

        content = QFrame()
        content_layout = QVBoxLayout(content)
        self.title = QLabel()
        self.title.setStyleSheet("font-size: 32px; color: white;")
        self.title.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(self.title)

        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignCenter)
        self.poster = QLabel()
        self.poster.setFixedSize(300, 400)
        self.poster.setStyleSheet("border-radius: 15px;")
        hbox.addWidget(self.poster)

        info_layout = QVBoxLayout()
        info_layout.setAlignment(Qt.AlignCenter)
        self.genre = QLabel()
        self.genre.setStyleSheet("color: #ccc; font-size: 16px;")
        self.rating = QLabel()
        self.rating.setStyleSheet("color: #ffd700; font-size: 16px;")
        self.status = QLabel()
        self.status.setStyleSheet("padding: 5px; border-radius: 5px;")
        self.description = QLabel()
        self.description.setStyleSheet("color: #aaa; font-size: 14px;")
        self.description.setWordWrap(True)

        info_layout.addWidget(self.genre)
        info_layout.addWidget(self.rating)
        info_layout.addWidget(self.status)
        info_layout.addWidget(self.description)
        hbox.addLayout(info_layout)
        content_layout.addLayout(hbox)
        layout.addWidget(content)

    def set_data(self, data):
        self.title.setText(data['title'])
        self.poster.setPixmap(QPixmap(data['image']).scaled(300, 400, Qt.KeepAspectRatio))
        self.genre.setText(f"🎭 {data['genre']}")
        self.rating.setText(f"⭐ {data['rating']}")
        self.status.setText(f"📌 {data['status']}")
        self.status.setStyleSheet(f"background: {data['status_color']}; color: white;")
        self.description.setText(data['description'])

    def go_back(self):
        if self.back_callback:
            self.back_callback()
