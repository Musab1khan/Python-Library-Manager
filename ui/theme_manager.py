"""Theme management for the application"""


class ThemeManager:
    """Manages application themes (light/dark mode)"""

    def __init__(self):
        self.is_dark = False

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.is_dark = not self.is_dark

    def get_stylesheet(self):
        """Get the current theme stylesheet"""
        if self.is_dark:
            return self._dark_theme()
        return self._light_theme()

    def _light_theme(self):
        """Light theme stylesheet"""
        return """
            QMainWindow {
                background-color: #f5f5f5;
            }
            QWidget {
                background-color: white;
                color: #2c3e50;
            }
            QLabel {
                color: #2c3e50;
            }
            QScrollArea {
                background-color: white;
            }
            QTextEdit {
                color: #2c3e50;
            }
            QPushButton {
                font-size: 13px;
                color: #2c3e50;
            }
            LibraryItem {
                border-bottom: 1px solid #e0e0e0;
            }
        """

    def _dark_theme(self):
        """Dark theme stylesheet"""
        return """
            QMainWindow {
                background-color: #1e1e1e;
            }
            QWidget {
                background-color: #2d2d30;
                color: #e0e0e0;
            }
            QFrame {
                background-color: #2d2d30;
            }
            QLabel {
                color: #e0e0e0;
            }
            QScrollArea {
                background-color: #2d2d30;
            }
            QPushButton {
                font-size: 13px;
            }
            LibraryItem {
                border-bottom: 1px solid #3e3e42;
            }
        """
