#!/usr/bin/env python3
"""
SimpleSensorSync GUI 启动脚本

启动多传感器同步监控的图形界面应用程序
"""

import sys
import os
import argparse
import logging
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from infinite_sense_core.gui import MainWindow
from infinite_sense_core.gui.utils.theme_manager import get_theme_manager, Theme


def setup_logging(log_level: str = "INFO", log_file: str = None):
    """设置日志配置"""
    level = getattr(logging, log_level.upper(), logging.INFO)

    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding='utf-8'))

    logging.basicConfig(
        level=level,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        handlers=handlers
    )


def create_application() -> QApplication:
    """创建QApplication实例"""
    app = QApplication(sys.argv)

    # 设置应用程序属性
    app.setApplicationName("SimpleSensorSync")
    app.setApplicationVersion("0.2.0")
    app.setApplicationDisplayName("SimpleSensorSync - 多传感器同步监控")
    app.setOrganizationName("SimpleSensorSync Team")
    app.setOrganizationDomain("simplesensorsync.org")

    # 设置应用程序图标（如果存在）
    icon_path = project_root / "infinite_sense_core" / "gui" / "resources" / "icons" / "app_icon.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))

    # 启用高DPI支持 (PyQt6中自动启用，这些属性已弃用)

    return app


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="SimpleSensorSync GUI - 多传感器同步监控界面",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python gui_main.py                    # 启动GUI界面
  python gui_main.py --theme dark       # 使用深色主题
  python gui_main.py --log-level DEBUG  # 启用调试日志
  python gui_main.py --log-file app.log # 保存日志到文件
        """
    )

    parser.add_argument(
        "--theme",
        choices=["light", "dark", "auto"],
        default="light",
        help="界面主题 (默认: light)"
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="日志级别 (默认: INFO)"
    )

    parser.add_argument(
        "--log-file",
        type=str,
        help="日志文件路径"
    )

    parser.add_argument(
        "--config",
        type=str,
        help="配置文件路径"
    )

    args = parser.parse_args()

    # 设置日志
    setup_logging(args.log_level, args.log_file)
    logging.info("SimpleSensorSync GUI 启动中...")

    try:
        # 创建应用程序
        app = create_application()

        # 设置主题
        theme_manager = get_theme_manager()
        if args.theme == "dark":
            theme_manager.set_theme(Theme.DARK)
        elif args.theme == "auto":
            theme_manager.set_theme(Theme.AUTO)
        else:
            theme_manager.set_theme(Theme.LIGHT)

        logging.info(f"已设置主题: {args.theme}")

        # 创建主窗口
        main_window = MainWindow()

        # 加载配置文件（如果指定）
        if args.config and os.path.exists(args.config):
            logging.info(f"加载配置文件: {args.config}")
            # 这里可以添加配置文件加载逻辑

        # 显示主窗口
        main_window.show()
        logging.info("主窗口已显示")

        # 运行应用程序
        logging.info("应用程序开始运行")
        exit_code = app.exec()

        logging.info(f"应用程序退出，退出码: {exit_code}")
        return exit_code

    except Exception as e:
        logging.error(f"应用程序启动失败: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())