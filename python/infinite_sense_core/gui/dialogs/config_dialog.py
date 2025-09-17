"""
配置对话框模块

提供网络和串口连接参数配置界面
支持配置验证和参数保存功能
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QSpinBox, QComboBox, QGroupBox,
    QPushButton, QRadioButton, QButtonGroup, QMessageBox,
    QTabWidget, QWidget
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
import serial.tools.list_ports


class NetworkConfigWidget(QWidget):
    """网络配置组件"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        layout = QFormLayout(self)

        # IP地址
        self.ip_edit = QLineEdit("192.168.1.188")
        self.ip_edit.setPlaceholderText("例如: 192.168.1.100")
        layout.addRow("IP地址:", self.ip_edit)

        # 端口
        self.port_spin = QSpinBox()
        self.port_spin.setRange(1, 65535)
        self.port_spin.setValue(8888)
        layout.addRow("端口:", self.port_spin)

        # PTP配置
        self.ptp_interface_edit = QLineEdit("eth0")
        self.ptp_interface_edit.setPlaceholderText("网络接口名称")
        layout.addRow("PTP接口:", self.ptp_interface_edit)

    def get_config(self) -> dict:
        """获取网络配置"""
        return {
            'net_ip': self.ip_edit.text(),
            'net_port': self.port_spin.value(),
            'ptp_interface': self.ptp_interface_edit.text()
        }

    def set_config(self, config: dict):
        """设置网络配置"""
        self.ip_edit.setText(config.get('net_ip', '192.168.1.188'))
        self.port_spin.setValue(config.get('net_port', 8888))
        self.ptp_interface_edit.setText(config.get('ptp_interface', 'eth0'))

    def validate(self) -> tuple[bool, str]:
        """验证配置"""
        ip = self.ip_edit.text().strip()
        if not ip:
            return False, "IP地址不能为空"

        # 简单的IP地址格式验证
        parts = ip.split('.')
        if len(parts) != 4:
            return False, "IP地址格式错误"

        try:
            for part in parts:
                if not (0 <= int(part) <= 255):
                    return False, "IP地址数值超出范围"
        except ValueError:
            return False, "IP地址包含非数字字符"

        return True, ""


class SerialConfigWidget(QWidget):
    """串口配置组件"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        layout = QFormLayout(self)

        # 串口设备
        self.device_combo = QComboBox()
        self.refresh_serial_ports()
        layout.addRow("串口设备:", self.device_combo)

        # 刷新按钮
        refresh_layout = QHBoxLayout()
        refresh_button = QPushButton("刷新")
        refresh_button.clicked.connect(self.refresh_serial_ports)
        refresh_layout.addWidget(self.device_combo, 1)
        refresh_layout.addWidget(refresh_button)
        layout.addRow("", refresh_layout)

        # 波特率
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(['9600', '19200', '38400', '57600', '115200', '230400', '460800', '921600'])
        self.baudrate_combo.setCurrentText('115200')
        layout.addRow("波特率:", self.baudrate_combo)

        # 数据位
        self.databits_combo = QComboBox()
        self.databits_combo.addItems(['5', '6', '7', '8'])
        self.databits_combo.setCurrentText('8')
        layout.addRow("数据位:", self.databits_combo)

        # 停止位
        self.stopbits_combo = QComboBox()
        self.stopbits_combo.addItems(['1', '1.5', '2'])
        self.stopbits_combo.setCurrentText('1')
        layout.addRow("停止位:", self.stopbits_combo)

        # 校验位
        self.parity_combo = QComboBox()
        self.parity_combo.addItems(['None', 'Even', 'Odd', 'Mark', 'Space'])
        self.parity_combo.setCurrentText('None')
        layout.addRow("校验位:", self.parity_combo)

    def refresh_serial_ports(self):
        """刷新串口列表"""
        self.device_combo.clear()
        ports = serial.tools.list_ports.comports()

        for port in ports:
            self.device_combo.addItem(f"{port.device} - {port.description}", port.device)

        if self.device_combo.count() == 0:
            self.device_combo.addItem("未找到串口设备", "")

    def get_config(self) -> dict:
        """获取串口配置"""
        return {
            'serial_device': self.device_combo.currentData(),
            'serial_baudrate': int(self.baudrate_combo.currentText()),
            'serial_databits': int(self.databits_combo.currentText()),
            'serial_stopbits': float(self.stopbits_combo.currentText()),
            'serial_parity': self.parity_combo.currentText()
        }

    def set_config(self, config: dict):
        """设置串口配置"""
        device = config.get('serial_device', '')
        # 尝试找到对应的设备
        index = self.device_combo.findData(device)
        if index >= 0:
            self.device_combo.setCurrentIndex(index)

        self.baudrate_combo.setCurrentText(str(config.get('serial_baudrate', 115200)))
        self.databits_combo.setCurrentText(str(config.get('serial_databits', 8)))
        self.stopbits_combo.setCurrentText(str(config.get('serial_stopbits', 1)))
        self.parity_combo.setCurrentText(config.get('serial_parity', 'None'))

    def validate(self) -> tuple[bool, str]:
        """验证配置"""
        device = self.device_combo.currentData()
        if not device:
            return False, "请选择有效的串口设备"

        return True, ""


class ConfigDialog(QDialog):
    """配置对话框主类"""

    config_applied = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("连接配置")
        self.setModal(True)
        self.resize(400, 350)

        self.connection_type = 'network'  # 默认网络连接

        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        layout = QVBoxLayout(self)

        # 标题
        title_label = QLabel("SimpleSensorSync 连接配置")
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # 连接类型选择
        self.create_connection_type_group(layout)

        # 配置选项卡
        self.create_config_tabs(layout)

        # 按钮区域
        self.create_button_area(layout)

    def create_connection_type_group(self, parent_layout):
        """创建连接类型选择组"""
        group = QGroupBox("连接类型")
        layout = QHBoxLayout(group)

        self.button_group = QButtonGroup()

        self.network_radio = QRadioButton("网络连接")
        self.network_radio.setChecked(True)
        self.network_radio.toggled.connect(self.on_connection_type_changed)

        self.serial_radio = QRadioButton("串口连接")
        self.serial_radio.toggled.connect(self.on_connection_type_changed)

        self.button_group.addButton(self.network_radio, 0)
        self.button_group.addButton(self.serial_radio, 1)

        layout.addWidget(self.network_radio)
        layout.addWidget(self.serial_radio)

        parent_layout.addWidget(group)

    def create_config_tabs(self, parent_layout):
        """创建配置选项卡"""
        self.tab_widget = QTabWidget()

        # 网络配置标签页
        self.network_config = NetworkConfigWidget()
        self.tab_widget.addTab(self.network_config, "网络设置")

        # 串口配置标签页
        self.serial_config = SerialConfigWidget()
        self.tab_widget.addTab(self.serial_config, "串口设置")

        parent_layout.addWidget(self.tab_widget)

    def create_button_area(self, parent_layout):
        """创建按钮区域"""
        button_layout = QHBoxLayout()

        # 测试连接按钮
        self.test_button = QPushButton("测试连接")
        self.test_button.clicked.connect(self.test_connection)

        # 确定按钮
        self.ok_button = QPushButton("确定")
        self.ok_button.clicked.connect(self.accept_config)
        self.ok_button.setDefault(True)

        # 取消按钮
        self.cancel_button = QPushButton("取消")
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.test_button)
        button_layout.addStretch()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        parent_layout.addLayout(button_layout)

    def on_connection_type_changed(self):
        """连接类型变化处理"""
        if self.network_radio.isChecked():
            self.connection_type = 'network'
            self.tab_widget.setCurrentIndex(0)
        else:
            self.connection_type = 'serial'
            self.tab_widget.setCurrentIndex(1)

    def test_connection(self):
        """测试连接"""
        # 这里可以添加实际的连接测试逻辑
        if self.connection_type == 'network':
            valid, error_msg = self.network_config.validate()
            if not valid:
                QMessageBox.warning(self, "配置错误", error_msg)
                return

            QMessageBox.information(self, "测试连接", "网络连接配置有效（实际连接测试需要硬件支持）")
        else:
            valid, error_msg = self.serial_config.validate()
            if not valid:
                QMessageBox.warning(self, "配置错误", error_msg)
                return

            QMessageBox.information(self, "测试连接", "串口连接配置有效（实际连接测试需要硬件支持）")

    def accept_config(self):
        """接受配置"""
        # 验证当前配置
        if self.connection_type == 'network':
            valid, error_msg = self.network_config.validate()
            if not valid:
                QMessageBox.warning(self, "配置错误", error_msg)
                return
        else:
            valid, error_msg = self.serial_config.validate()
            if not valid:
                QMessageBox.warning(self, "配置错误", error_msg)
                return

        self.accept()

    def get_config(self) -> dict:
        """获取完整配置"""
        config = {'connection_type': self.connection_type}

        if self.connection_type == 'network':
            config.update(self.network_config.get_config())
        else:
            config.update(self.serial_config.get_config())

        return config

    def set_config(self, config: dict):
        """设置配置"""
        connection_type = config.get('connection_type', 'network')

        if connection_type == 'network':
            self.network_radio.setChecked(True)
            self.network_config.set_config(config)
        else:
            self.serial_radio.setChecked(True)
            self.serial_config.set_config(config)