"""Dependency Viewer Dialog"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
    QTreeWidget, QTreeWidgetItem, QLabel, QTextEdit,
    QSplitter, QWidget, QProgressBar, QMessageBox
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QColor
from core.dependency_manager import DependencyManager


class DependencyWorker(QThread):
    """Worker thread to build dependency tree"""
    finished = pyqtSignal(object, str)

    def __init__(self, package_name):
        super().__init__()
        self.package_name = package_name
        self.dep_manager = DependencyManager()

    def run(self):
        try:
            tree = self.dep_manager.build_dependency_tree(self.package_name)
            self.finished.emit(tree, "")
        except Exception as e:
            self.finished.emit(None, str(e))


class DependencyViewerDialog(QDialog):
    """Dialog for viewing package dependencies"""

    def __init__(self, package_name, parent=None):
        super().__init__(parent)
        self.package_name = package_name
        self.dep_manager = DependencyManager()
        self.dependency_tree = None

        self.setWindowTitle(f"Dependency Viewer - {package_name}")
        self.setMinimumSize(900, 700)
        self.setModal(True)

        self.init_ui()
        self.load_dependencies()

    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel(f"<h1>🌳 Dependency Tree - {self.package_name}</h1>")
        header.setStyleSheet("color: #3498db; margin-bottom: 10px;")
        layout.addWidget(header)

        # Info text
        info = QLabel(
            "This shows all dependencies (packages required by this package) "
            "up to 3 levels deep."
        )
        info.setStyleSheet("color: #7f8c8d; margin-bottom: 10px;")
        info.setWordWrap(True)
        layout.addWidget(info)

        # Loading indicator
        self.loading_label = QLabel("Building dependency tree...")
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        layout.addWidget(self.progress_bar)

        # Splitter for tree and details
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Tree view container
        tree_container = QWidget()
        tree_layout = QVBoxLayout()
        tree_layout.setContentsMargins(0, 0, 0, 0)

        tree_label = QLabel("<b>Dependency Tree:</b>")
        tree_label.setVisible(False)
        tree_layout.addWidget(tree_label)
        self.tree_label = tree_label

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Package", "Status"])
        self.tree_widget.setVisible(False)
        self.tree_widget.setStyleSheet("""
            QTreeWidget {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                background-color: white;
                font-family: monospace;
                font-size: 13px;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QTreeWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        self.tree_widget.itemClicked.connect(self.on_item_clicked)
        tree_layout.addWidget(self.tree_widget)

        tree_container.setLayout(tree_layout)
        splitter.addWidget(tree_container)

        # Details panel
        details_container = QWidget()
        details_layout = QVBoxLayout()
        details_layout.setContentsMargins(0, 0, 0, 0)

        details_label = QLabel("<b>Package Details:</b>")
        details_label.setVisible(False)
        details_layout.addWidget(details_label)
        self.details_label = details_label

        self.details_panel = QTextEdit()
        self.details_panel.setReadOnly(True)
        self.details_panel.setVisible(False)
        self.details_panel.setStyleSheet("""
            QTextEdit {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                padding: 10px;
                background-color: #f8f9fa;
                font-family: monospace;
                font-size: 12px;
            }
        """)
        details_layout.addWidget(self.details_panel)

        details_container.setLayout(details_layout)
        splitter.addWidget(details_container)

        splitter.setSizes([500, 400])
        splitter.setVisible(False)
        layout.addWidget(splitter)
        self.splitter = splitter

        # Reverse dependencies section
        self.reverse_deps_label = QLabel("<b>Reverse Dependencies (packages that need this):</b>")
        self.reverse_deps_label.setVisible(False)
        layout.addWidget(self.reverse_deps_label)

        self.reverse_deps_text = QTextEdit()
        self.reverse_deps_text.setReadOnly(True)
        self.reverse_deps_text.setMaximumHeight(100)
        self.reverse_deps_text.setVisible(False)
        self.reverse_deps_text.setStyleSheet("""
            QTextEdit {
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                padding: 10px;
                background-color: #fff3cd;
                font-size: 12px;
            }
        """)
        layout.addWidget(self.reverse_deps_text)

        # Buttons
        button_layout = QHBoxLayout()

        self.export_btn = QPushButton("📄 Export as Text")
        self.export_btn.setEnabled(False)
        self.export_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:disabled {
                background-color: #95a5a6;
            }
        """)
        self.export_btn.clicked.connect(self.export_tree)
        button_layout.addWidget(self.export_btn)

        button_layout.addStretch()

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
                color: white;
                border: none;
                padding: 10px 20px;
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

    def load_dependencies(self):
        """Load dependencies in background"""
        self.worker = DependencyWorker(self.package_name)
        self.worker.finished.connect(self.on_dependencies_loaded)
        self.worker.start()

    def on_dependencies_loaded(self, tree, error):
        """Handle loaded dependencies"""
        self.loading_label.setVisible(False)
        self.progress_bar.setVisible(False)

        if error:
            QMessageBox.warning(self, "Error", f"Failed to load dependencies:\n{error}")
            return

        if not tree:
            self.loading_label.setText("⚠ Package not installed or no dependencies found.")
            self.loading_label.setVisible(True)
            return

        self.dependency_tree = tree

        # Show UI elements
        self.tree_label.setVisible(True)
        self.tree_widget.setVisible(True)
        self.details_label.setVisible(True)
        self.details_panel.setVisible(True)
        self.splitter.setVisible(True)
        self.export_btn.setEnabled(True)

        # Build tree widget
        self.tree_widget.clear()
        self.add_tree_items(tree, None)
        self.tree_widget.expandAll()

        # Load reverse dependencies
        self.load_reverse_dependencies()

    def add_tree_items(self, tree_node, parent_item):
        """Recursively add items to tree widget"""
        if parent_item is None:
            item = QTreeWidgetItem(self.tree_widget)
        else:
            item = QTreeWidgetItem(parent_item)

        item.setText(0, tree_node["name"])
        item.setData(0, Qt.ItemDataRole.UserRole, tree_node["name"])

        # Check if package is installed
        info = self.dep_manager.get_package_info_summary(tree_node["name"])
        if info:
            item.setText(1, f"✓ v{info.get('Version', '?')}")
            item.setForeground(1, QColor("#27ae60"))
        else:
            item.setText(1, "✗ Not installed")
            item.setForeground(1, QColor("#e74c3c"))

        # Set font based on depth
        font = QFont()
        if tree_node["depth"] == 0:
            font.setBold(True)
            font.setPointSize(11)
        item.setFont(0, font)

        # Add children
        for child in tree_node.get("dependencies", []):
            self.add_tree_items(child, item)

    def load_reverse_dependencies(self):
        """Load reverse dependencies"""
        reverse_deps, error = self.dep_manager.get_reverse_dependencies(self.package_name)

        if error:
            return

        if reverse_deps and reverse_deps[0]:  # Check if not empty
            self.reverse_deps_label.setVisible(True)
            self.reverse_deps_text.setVisible(True)

            text = f"The following packages depend on {self.package_name}:\n\n"
            for dep in reverse_deps:
                text += f"  • {dep}\n"

            text += f"\n💡 If you uninstall {self.package_name}, these packages may not work correctly."

            self.reverse_deps_text.setText(text)

    def on_item_clicked(self, item, column):
        """Handle tree item click"""
        package_name = item.data(0, Qt.ItemDataRole.UserRole)

        if not package_name:
            return

        # Show package details
        info = self.dep_manager.get_package_info_summary(package_name)

        self.details_panel.clear()

        if info:
            self.details_panel.append(f"Package: {package_name}")
            self.details_panel.append("=" * 60)
            self.details_panel.append(f"Version: {info.get('Version', 'N/A')}")
            self.details_panel.append(f"Author: {info.get('Author', 'N/A')}")
            self.details_panel.append(f"License: {info.get('License', 'N/A')}")
            self.details_panel.append(f"Location: {info.get('Location', 'N/A')}")
            self.details_panel.append("")
            self.details_panel.append(f"Summary:")
            self.details_panel.append(f"{info.get('Summary', 'N/A')}")
            self.details_panel.append("")
            self.details_panel.append(f"Requires: {info.get('Requires', 'None')}")
            self.details_panel.append(f"Required-by: {info.get('Required-by', 'None')}")
        else:
            self.details_panel.append(f"Package: {package_name}")
            self.details_panel.append("=" * 60)
            self.details_panel.append("⚠ This package is not installed.")
            self.details_panel.append("")
            self.details_panel.append("It is required by one of your installed packages.")

    def export_tree(self):
        """Export dependency tree as text"""
        if not self.dependency_tree:
            return

        text = self._tree_to_text(self.dependency_tree, 0)

        # Copy to clipboard
        from PyQt6.QtWidgets import QApplication
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

        QMessageBox.information(
            self,
            "Exported",
            "Dependency tree copied to clipboard!\n\nYou can paste it anywhere."
        )

    def _tree_to_text(self, node, depth):
        """Convert tree to text format"""
        indent = "  " * depth
        prefix = "├─ " if depth > 0 else ""

        text = f"{indent}{prefix}{node['name']}\n"

        for i, child in enumerate(node.get("dependencies", [])):
            text += self._tree_to_text(child, depth + 1)

        return text
