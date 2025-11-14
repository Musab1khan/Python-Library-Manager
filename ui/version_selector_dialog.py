"""Package Version Selector Dialog"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QListWidgetItem, QMessageBox,
    QProgressBar, QTextEdit
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from core.package_version_manager import PackageVersionManager


class VersionFetchWorker(QThread):
    """Worker thread to fetch available versions"""
    finished = pyqtSignal(list, str)

    def __init__(self, package_name):
        super().__init__()
        self.package_name = package_name
        self.version_manager = PackageVersionManager()

    def run(self):
        versions, error = self.version_manager.get_available_versions(self.package_name)
        self.finished.emit(versions, error if error else "")


class VersionInstallWorker(QThread):
    """Worker thread to install specific version"""
    finished = pyqtSignal(bool, str)

    def __init__(self, package_name, version_str):
        super().__init__()
        self.package_name = package_name
        self.version_str = version_str
        self.version_manager = PackageVersionManager()

    def run(self):
        success, output = self.version_manager.install_specific_version(
            self.package_name,
            self.version_str
        )
        self.finished.emit(success, output)


class VersionSelectorDialog(QDialog):
    """Dialog for selecting and installing package versions"""

    def __init__(self, package_name, parent=None):
        super().__init__(parent)
        self.package_name = package_name
        self.version_manager = PackageVersionManager()
        self.available_versions = []
        self.installed_version = None

        self.setWindowTitle(f"Version Selector - {package_name}")
        self.setMinimumSize(600, 500)
        self.setModal(True)

        self.init_ui()
        self.load_versions()

    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel(f"<h1>📦 {self.package_name}</h1>")
        header.setStyleSheet("color: #3498db; margin-bottom: 10px;")
        layout.addWidget(header)

        # Current version info
        self.current_version_label = QLabel("Checking installed version...")
        self.current_version_label.setStyleSheet("""
            padding: 10px;
            background-color: #ecf0f1;
            border-radius: 5px;
            font-size: 13px;
        """)
        layout.addWidget(self.current_version_label)

        # Loading indicator
        self.loading_label = QLabel("Loading available versions from PyPI...")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate
        layout.addWidget(self.progress_bar)

        # Versions list
        list_label = QLabel("<b>Available Versions:</b>")
        list_label.setVisible(False)
        layout.addWidget(list_label)
        self.versions_list_label = list_label

        self.versions_list = QListWidget()
        self.versions_list.setStyleSheet("""
            QListWidget {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                padding: 5px;
                background-color: white;
                font-family: monospace;
                font-size: 13px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #e0e0e0;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #ecf0f1;
            }
        """)
        self.versions_list.setVisible(False)
        self.versions_list.itemSelectionChanged.connect(self.on_version_selected)
        layout.addWidget(self.versions_list)

        # Info panel
        self.info_panel = QTextEdit()
        self.info_panel.setReadOnly(True)
        self.info_panel.setMaximumHeight(100)
        self.info_panel.setVisible(False)
        self.info_panel.setStyleSheet("""
            QTextEdit {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                padding: 10px;
                background-color: #f8f9fa;
                font-size: 12px;
            }
        """)
        layout.addWidget(self.info_panel)

        # Buttons
        button_layout = QHBoxLayout()

        self.install_btn = QPushButton("📥 Install Selected Version")
        self.install_btn.setEnabled(False)
        self.install_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 5px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        self.install_btn.clicked.connect(self.install_selected_version)
        button_layout.addWidget(self.install_btn)

        button_layout.addStretch()

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 5px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_versions(self):
        """Load available versions"""
        # Get installed version first
        self.installed_version = self.version_manager.get_installed_version(self.package_name)

        if self.installed_version:
            self.current_version_label.setText(
                f"✓ Currently installed: <b>v{self.installed_version}</b>"
            )
            self.current_version_label.setStyleSheet("""
                padding: 10px;
                background-color: #d5f4e6;
                border-left: 4px solid #27ae60;
                border-radius: 5px;
                font-size: 13px;
                color: #27ae60;
            """)
        else:
            self.current_version_label.setText(
                "⚠ Not installed - Select a version to install"
            )
            self.current_version_label.setStyleSheet("""
                padding: 10px;
                background-color: #fff3cd;
                border-left: 4px solid #ffc107;
                border-radius: 5px;
                font-size: 13px;
                color: #856404;
            """)

        # Fetch versions in background
        self.fetch_worker = VersionFetchWorker(self.package_name)
        self.fetch_worker.finished.connect(self.on_versions_loaded)
        self.fetch_worker.start()

    def on_versions_loaded(self, versions, error):
        """Handle loaded versions"""
        self.loading_label.setVisible(False)
        self.progress_bar.setVisible(False)

        if error:
            QMessageBox.warning(self, "Error", f"Failed to fetch versions:\n{error}")
            return

        if not versions:
            self.loading_label.setText("No versions found for this package.")
            self.loading_label.setVisible(True)
            return

        # Sort versions (latest first)
        sorted_versions = self.version_manager.sort_versions(versions)
        self.available_versions = sorted_versions

        # Show versions list
        self.versions_list_label.setVisible(True)
        self.versions_list.setVisible(True)

        for ver in sorted_versions:
            item = QListWidgetItem()

            # Mark if it's the installed version
            if ver == self.installed_version:
                item.setText(f"{ver}  ✓ INSTALLED")
                item.setBackground(Qt.GlobalColor.lightGray)
            # Mark if it's the latest
            elif ver == sorted_versions[0]:
                item.setText(f"{ver}  ⭐ LATEST")
            else:
                item.setText(ver)

            item.setData(Qt.ItemDataRole.UserRole, ver)
            self.versions_list.addItem(item)

    def on_version_selected(self):
        """Handle version selection"""
        selected = self.versions_list.selectedItems()

        if selected:
            version_str = selected[0].data(Qt.ItemDataRole.UserRole)
            self.install_btn.setEnabled(True)

            # Show info
            self.info_panel.setVisible(True)
            self.info_panel.clear()

            if version_str == self.installed_version:
                self.info_panel.append(
                    f"⚠ Version {version_str} is already installed.\n"
                    f"Reinstalling will download and install it again."
                )
            elif self.installed_version:
                # Compare versions
                if self.available_versions.index(version_str) < self.available_versions.index(self.installed_version):
                    self.info_panel.append(
                        f"⬆ Upgrading from {self.installed_version} to {version_str}\n"
                        f"This is a newer version."
                    )
                else:
                    self.info_panel.append(
                        f"⬇ Downgrading from {self.installed_version} to {version_str}\n"
                        f"This is an older version."
                    )
            else:
                self.info_panel.append(
                    f"📥 Installing version {version_str}\n"
                    f"This package is not currently installed."
                )
        else:
            self.install_btn.setEnabled(False)
            self.info_panel.setVisible(False)

    def install_selected_version(self):
        """Install the selected version"""
        selected = self.versions_list.selectedItems()
        if not selected:
            return

        version_str = selected[0].data(Qt.ItemDataRole.UserRole)

        # Confirm
        msg = f"Install {self.package_name} version {version_str}?"
        if self.installed_version:
            msg += f"\n\nCurrent version: {self.installed_version}"

        reply = QMessageBox.question(
            self,
            "Confirm Installation",
            msg,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.No:
            return

        # Disable UI
        self.install_btn.setEnabled(False)
        self.versions_list.setEnabled(False)

        # Show progress
        self.info_panel.clear()
        self.info_panel.append(f"Installing {self.package_name}=={version_str}...")
        self.info_panel.append("This may take a few moments...")

        # Install in background
        self.install_worker = VersionInstallWorker(self.package_name, version_str)
        self.install_worker.finished.connect(self.on_install_finished)
        self.install_worker.start()

    def on_install_finished(self, success, output):
        """Handle installation result"""
        self.install_btn.setEnabled(True)
        self.versions_list.setEnabled(True)

        if success:
            QMessageBox.information(
                self,
                "Success",
                f"Successfully installed {self.package_name}!"
            )
            # Reload to update installed version
            self.load_versions()
        else:
            QMessageBox.warning(
                self,
                "Installation Failed",
                f"Failed to install package.\n\nError:\n{output[:500]}"
            )
            self.info_panel.clear()
            self.info_panel.append("Installation failed:")
            self.info_panel.append(output)
