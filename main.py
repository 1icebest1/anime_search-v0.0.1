
import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtGui import QPainter, QColor


from account import AccountPage
from explore import ExplorePage
from library import LibraryPage
from recommendation import RecommendationPage
from setting import SettingsPage
from help import HelpPage
from detail import DetailPage
from side_panel import RoundedPanel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime Viewer")

        self.setGeometry(200, 0, 1366, 768)

        # Ініціалізація змінних для теми
        self.current_theme = "dark"
        self.stars = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_stars)

        # Головний макет
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Бічна панель
        self.panel = RoundedPanel(self)
        self.main_layout.addWidget(self.panel)

        # Область контенту
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout(self.content_area)
        self.stacked_widget = QStackedWidget()

        # Сторінки
        self.pages = {
            "home": RecommendationPage(self),
            "explore": ExplorePage(self),
            "library": LibraryPage(self),
            "account": AccountPage(),
            "settings": SettingsPage(self),
            "help": HelpPage(),
            "detail": DetailPage()
        }

        for name, widget in self.pages.items():
            self.stacked_widget.addWidget(widget)

        self.content_layout.addWidget(self.stacked_widget)
        self.main_layout.addWidget(self.content_area)

        # Підключення сигналів
        self.pages["detail"].back_callback = lambda: self.switch_page("home")
        self.switch_page("home")
        self.apply_theme("dark")

    def apply_theme(self, theme_name):
        self.current_theme = theme_name
        theme_styles = {
            "dark": """
                * { color: white; }
                QWidget { background: #1a1a1a; }
                QFrame, QPushButton, QComboBox, QLineEdit { 
                    background: #404040;
                    border-radius: 15px;
                }
                QPushButton:hover { background: #505050; }
            """,
            "light": """
                * { color: #333; }
                QWidget { background: #f0f0f0; }
                QFrame, QPushButton, QComboBox, QLineEdit {
                    background: white;
                    border: 1px solid #ddd;
                    border-radius: 15px;
                }
                QPushButton:hover { background: #f0f0f0; }
            """,
            "space": """
                * { color: white; }
                QWidget {
                    background: qlineargradient(x1:0 y1:0, x2:1 y2:1,
                        stop:0 #0c1445, stop:0.5 #301959, stop:1 #5a1464);
                }
                QFrame, QPushButton, QComboBox, QLineEdit {
                    background: rgba(43, 43, 43, 200);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                }
                QPushButton:hover { background: rgba(65, 65, 65, 200); }
            """
        }

        self.setStyleSheet(theme_styles[theme_name])
        self.update_space_effect()
        self.update()

    def update_space_effect(self):
        if self.current_theme == "space":
            self.stars = [QPoint(random.randint(0, self.width()),
                                 random.randint(0, self.height()))
                          for _ in range(100)]
            self.timer.start(50)
        else:
            self.timer.stop()

    def move_stars(self):
        for i in range(len(self.stars)):
            self.stars[i].setX((self.stars[i].x() + 2) % self.width())
        self.update()

    def paintEvent(self, event):
        if self.current_theme == "space":
            painter = QPainter(self)
            painter.setPen(QColor(255, 255, 255, 200))
            for star in self.stars:
                painter.drawPoint(star)

    def switch_page(self, page_name):
        self.stacked_widget.setCurrentWidget(self.pages[page_name])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
