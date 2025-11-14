#!/usr/bin/env python3
"""
Library Manager - Cross-Platform Package Installation Tool
Main entry point for the application
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow


def main():
    """Initialize and run the application"""
    # Enable high DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName("Library Manager")
    app.setOrganizationName("DevTools")
    app.setQuitOnLastWindowClosed(False)  # Keep app running when window is closed

    # Create and show main window
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
