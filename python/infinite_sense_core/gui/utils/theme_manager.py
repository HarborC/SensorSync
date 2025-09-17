"""
主题管理器模块

提供GUI主题切换和样式管理功能
支持浅色和深色主题
"""

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QPalette, QColor
from enum import Enum


class Theme(Enum):
    """主题枚举"""
    LIGHT = "light"
    DARK = "dark"
    AUTO = "auto"


class ThemeManager(QObject):
    """主题管理器"""

    theme_changed = pyqtSignal(str)  # 主题变化信号

    def __init__(self):
        super().__init__()
        self.current_theme = Theme.LIGHT

    def set_theme(self, theme: Theme):
        """设置主题"""
        self.current_theme = theme
        self.apply_theme()
        self.theme_changed.emit(theme.value)

    def apply_theme(self):
        """应用主题"""
        app = QApplication.instance()
        if not app:
            return

        if self.current_theme == Theme.LIGHT:
            self.apply_light_theme(app)
        elif self.current_theme == Theme.DARK:
            self.apply_dark_theme(app)
        else:  # AUTO
            # 这里可以根据系统设置自动选择主题
            self.apply_light_theme(app)

    def apply_light_theme(self, app: QApplication):
        """应用浅色主题"""
        light_stylesheet = """
        QMainWindow {
            background-color: #f0f0f0;
            color: #333333;
        }

        QWidget {
            background-color: #ffffff;
            color: #333333;
        }

        QMenuBar {
            background-color: #f8f8f8;
            border-bottom: 1px solid #d0d0d0;
        }

        QMenuBar::item {
            background-color: transparent;
            padding: 4px 8px;
        }

        QMenuBar::item:selected {
            background-color: #e0e0e0;
        }

        QMenu {
            background-color: #ffffff;
            border: 1px solid #d0d0d0;
        }

        QMenu::item:selected {
            background-color: #0078d4;
            color: white;
        }

        QStatusBar {
            background-color: #f8f8f8;
            border-top: 1px solid #d0d0d0;
        }

        QPushButton {
            background-color: #0078d4;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 3px;
        }

        QPushButton:hover {
            background-color: #106ebe;
        }

        QPushButton:pressed {
            background-color: #005a9e;
        }

        QPushButton:disabled {
            background-color: #cccccc;
            color: #888888;
        }

        QLineEdit, QSpinBox, QComboBox {
            border: 1px solid #d0d0d0;
            padding: 4px;
            border-radius: 3px;
            background-color: white;
        }

        QLineEdit:focus, QSpinBox:focus, QComboBox:focus {
            border: 2px solid #0078d4;
        }

        QGroupBox {
            font-weight: bold;
            border: 2px solid #d0d0d0;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 5px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            background-color: #ffffff;
        }

        QTabWidget::pane {
            border: 1px solid #d0d0d0;
            background-color: white;
        }

        QTabBar::tab {
            background-color: #f0f0f0;
            border: 1px solid #d0d0d0;
            padding: 8px 16px;
            margin-right: 2px;
        }

        QTabBar::tab:selected {
            background-color: white;
            border-bottom: none;
        }

        QCheckBox::indicator {
            width: 16px;
            height: 16px;
        }

        QCheckBox::indicator:unchecked {
            border: 1px solid #d0d0d0;
            background-color: white;
        }

        QCheckBox::indicator:checked {
            border: 1px solid #0078d4;
            background-color: #0078d4;
        }
        """

        app.setStyleSheet(light_stylesheet)

    def apply_dark_theme(self, app: QApplication):
        """应用深色主题"""
        dark_stylesheet = """
        QMainWindow {
            background-color: #2b2b2b;
            color: #ffffff;
        }

        QWidget {
            background-color: #3c3c3c;
            color: #ffffff;
        }

        QMenuBar {
            background-color: #2b2b2b;
            border-bottom: 1px solid #555555;
            color: #ffffff;
        }

        QMenuBar::item {
            background-color: transparent;
            padding: 4px 8px;
        }

        QMenuBar::item:selected {
            background-color: #555555;
        }

        QMenu {
            background-color: #3c3c3c;
            border: 1px solid #555555;
            color: #ffffff;
        }

        QMenu::item:selected {
            background-color: #0078d4;
            color: white;
        }

        QStatusBar {
            background-color: #2b2b2b;
            border-top: 1px solid #555555;
            color: #ffffff;
        }

        QPushButton {
            background-color: #0078d4;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 3px;
        }

        QPushButton:hover {
            background-color: #106ebe;
        }

        QPushButton:pressed {
            background-color: #005a9e;
        }

        QPushButton:disabled {
            background-color: #666666;
            color: #aaaaaa;
        }

        QLineEdit, QSpinBox, QComboBox {
            border: 1px solid #555555;
            padding: 4px;
            border-radius: 3px;
            background-color: #2b2b2b;
            color: #ffffff;
        }

        QLineEdit:focus, QSpinBox:focus, QComboBox:focus {
            border: 2px solid #0078d4;
        }

        QGroupBox {
            font-weight: bold;
            border: 2px solid #555555;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 5px;
            color: #ffffff;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
            background-color: #3c3c3c;
        }

        QTabWidget::pane {
            border: 1px solid #555555;
            background-color: #3c3c3c;
        }

        QTabBar::tab {
            background-color: #2b2b2b;
            border: 1px solid #555555;
            padding: 8px 16px;
            margin-right: 2px;
            color: #ffffff;
        }

        QTabBar::tab:selected {
            background-color: #3c3c3c;
            border-bottom: none;
        }

        QCheckBox {
            color: #ffffff;
        }

        QCheckBox::indicator {
            width: 16px;
            height: 16px;
        }

        QCheckBox::indicator:unchecked {
            border: 1px solid #555555;
            background-color: #2b2b2b;
        }

        QCheckBox::indicator:checked {
            border: 1px solid #0078d4;
            background-color: #0078d4;
        }

        QLabel {
            color: #ffffff;
        }
        """

        app.setStyleSheet(dark_stylesheet)

    def get_current_theme(self) -> Theme:
        """获取当前主题"""
        return self.current_theme

    def get_color_scheme(self) -> dict:
        """获取当前主题的颜色方案"""
        if self.current_theme == Theme.DARK:
            return {
                'background': '#3c3c3c',
                'foreground': '#ffffff',
                'primary': '#0078d4',
                'secondary': '#555555',
                'accent': '#106ebe',
                'success': '#00d084',
                'warning': '#ffcc00',
                'error': '#ff4d4f'
            }
        else:  # Light theme
            return {
                'background': '#ffffff',
                'foreground': '#333333',
                'primary': '#0078d4',
                'secondary': '#d0d0d0',
                'accent': '#106ebe',
                'success': '#00a86b',
                'warning': '#ff9500',
                'error': '#e74c3c'
            }


# 全局主题管理器实例
_theme_manager = ThemeManager()


def get_theme_manager() -> ThemeManager:
    """获取全局主题管理器实例"""
    return _theme_manager