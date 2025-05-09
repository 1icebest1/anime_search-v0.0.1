from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QScrollArea, QFrame, QLabel
from PySide6.QtCore import Qt


class LibraryPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignCenter)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setStyleSheet("""
            QTabBar::tab { 
                background: #404040;
                color: white;
                padding: 12px 25px;
                border-radius: 5px;
                margin: 2px;
            }
            QTabBar::tab:selected { background: #505050; }
        """)

        categories = ["Watching", "Planned", "Dropped", "Completed"]
        for status in categories:
            scroll = QScrollArea()
            content = QWidget()
            content_layout = QVBoxLayout(content)
            content_layout.setSpacing(15)
            content_layout.setAlignment(Qt.AlignCenter)

            for _ in range(10):
                card = QFrame()
                card.setStyleSheet("""
                    background: #404040;
                    border-radius: 10px;
                    padding: 10px;
                """)
                content_layout.addWidget(card)

            scroll.setWidget(content)
            scroll.setWidgetResizable(True)
            tabs.addTab(scroll, status)

        layout.addWidget(tabs)