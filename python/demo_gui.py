#!/usr/bin/env python3
"""
SimpleSensorSync GUI 演示脚本

同时启动GUI界面和模拟数据生成器
用于演示和测试GUI功能
"""

import sys
import time
import threading
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer

from infinite_sense_core.gui import MainWindow
from infinite_sense_core.gui.utils.theme_manager import get_theme_manager, Theme
from demo_data_generator import DemoDataGenerator


def create_demo_application():
    """创建演示应用程序"""
    app = QApplication(sys.argv)

    # 设置应用程序属性
    app.setApplicationName("SimpleSensorSync Demo")
    app.setApplicationVersion("0.2.0")
    app.setApplicationDisplayName("SimpleSensorSync 演示 - 多传感器同步监控")

    return app


def main():
    """主函数"""
    print("SimpleSensorSync GUI 演示启动中...")

    try:
        # 创建应用程序
        app = create_demo_application()

        # 设置浅色主题
        theme_manager = get_theme_manager()
        theme_manager.set_theme(Theme.LIGHT)

        # 创建主窗口
        main_window = MainWindow()

        # 创建演示数据生成器
        demo_generator = DemoDataGenerator()

        # 自动开始演示
        def start_demo():
            print("开始演示数据生成...")
            demo_generator.start()

        # 延迟2秒后开始生成演示数据
        QTimer.singleShot(2000, start_demo)

        # 显示主窗口
        main_window.show()

        print("GUI界面已启动")
        print("演示数据将在2秒后开始生成...")
        print("您可以:")
        print("1. 查看左侧设备面板的实时触发状态")
        print("2. 观察右侧图表的触发信号时序")
        print("3. 点击设备面板中的设备来高亮显示")
        print("4. 使用菜单 '文件 → 连接配置' 查看配置界面")
        print("5. 按 Ctrl+Q 或关闭窗口退出演示")

        # 运行应用程序
        exit_code = app.exec()

        # 清理
        print("正在停止演示数据生成器...")
        demo_generator.stop()

        print(f"演示结束，退出码: {exit_code}")
        return exit_code

    except Exception as e:
        print(f"演示启动失败: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())