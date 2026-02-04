import json
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QTextBrowser, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt

from config.settings import READING_PLAN_FILE
from services.biblia_api import fetch_passage
from utils.progress_tracker import load_progress, save_progress


class BibleReadingApp(QWidget):
    def __init__(self):
        super().__init__()

        with open(READING_PLAN_FILE, "r") as f:
            self.reading_plan = json.load(f)

        self.total_days = len(self.reading_plan)

        last_completed = load_progress()
        self.current_day = min(last_completed + 1, self.total_days)

        self.init_ui()
        self.load_day(self.current_day)

    def init_ui(self):
        self.setWindowTitle("Bible Reading Plan")
        self.setGeometry(200, 100, 900, 700)

        layout = QVBoxLayout(self)

        self.progress_label = QLabel(alignment=Qt.AlignCenter)
        self.progress_label.setStyleSheet(
            "font-size: 16pt; font-weight: bold;"
        )
        layout.addWidget(self.progress_label)

        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setStyleSheet("""
            background-color: #023d6b;
            border-radius: 10px;
            padding: 20px;
            font-family: Georgia;
            font-size: 20pt;
            color: white;
        """)
        layout.addWidget(self.text_browser)

        # buttons = QHBoxLayout()

        # self.prev_btn = QPushButton("<< Previous Day")
        # self.next_btn = QPushButton("Next Day >>")

        # self.prev_btn.clicked.connect(self.prev_day)
        # self.next_btn.clicked.connect(self.next_day)

        # buttons.addWidget(self.prev_btn)
        # buttons.addWidget(self.next_btn)
        # layout.addLayout(buttons)

        # self.setStyleSheet("background-color: #f0f8ff;")
        
        
        button_layout = QHBoxLayout()

        self.prev_button = QPushButton("⟵ Previous")
        self.next_button = QPushButton("Next ⟶")

        self.prev_button.clicked.connect(self.prev_day)
        self.next_button.clicked.connect(self.next_day)

        for btn in (self.prev_button, self.next_button):
            btn.setStyleSheet("""
                background-color: #aabde7;
                color: #023d6b;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px 24px;
                font-size: 14pt;
                border: 1px solid #023d6b;
            """)
            btn.setCursor(Qt.PointingHandCursor)

        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        layout.addLayout(button_layout)

        #self.setStyleSheet("background-color: #f0f8ff;")
        self.setStyleSheet("background-color: #aabde7;")

    def load_day(self, day):
        chapters = self.reading_plan.get(f"Day {day}", [])
        self.progress_label.setText(f"Day {day} / {self.total_days}")
        self.text_browser.setHtml(fetch_passage(chapters))

    def next_day(self):
        if self.current_day < self.total_days:
            save_progress(self.current_day)
            self.current_day += 1
            self.load_day(self.current_day)

    def prev_day(self):
        if self.current_day > 1:
            self.current_day -= 1
            self.load_day(self.current_day)
