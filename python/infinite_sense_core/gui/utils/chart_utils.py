"""
图表工具模块

提供pyqtgraph图表的通用工具函数
支持数据导出、样式设置、性能优化等功能
"""

import numpy as np
import pyqtgraph as pg
from typing import List, Dict, Tuple, Optional
from datetime import datetime
import csv
import json


class ChartUtils:
    """图表工具类"""

    @staticmethod
    def setup_plot_widget(
        plot_widget: pg.PlotWidget,
        title: str = "",
        x_label: str = "",
        y_label: str = "",
        background: str = 'w'
    ):
        """设置图表组件的基本属性"""
        plot_widget.setBackground(background)
        plot_widget.setLabel('left', y_label)
        plot_widget.setLabel('bottom', x_label)
        plot_widget.setTitle(title)
        plot_widget.showGrid(x=True, y=True, alpha=0.3)

    @staticmethod
    def create_color_map(device_count: int) -> List[str]:
        """创建设备颜色映射"""
        # 预定义的颜色列表
        colors = [
            '#FF6B6B',  # 红色
            '#4ECDC4',  # 青色
            '#45B7D1',  # 蓝色
            '#96CEB4',  # 绿色
            '#FECA57',  # 黄色
            '#FF9FF3',  # 粉色
            '#54A0FF',  # 深蓝
            '#5F27CD',  # 紫色
            '#00D2D3',  # 青绿
            '#FF9F43',  # 橙色
            '#EE5A24',  # 深红
            '#0984E3',  # 深蓝
            '#6C5CE7',  # 深紫
            '#A29BFE',  # 浅紫
            '#FD79A8',  # 粉红
            '#FDCB6E'   # 浅黄
        ]

        # 如果设备数量超过预定义颜色，生成额外颜色
        if device_count > len(colors):
            for i in range(len(colors), device_count):
                # 使用HSV色彩空间生成颜色
                hue = (i * 137.5) % 360  # 黄金角度分布
                color = pg.hsvColor(hue / 360, 0.8, 0.9)
                colors.append(color.name())

        return colors[:device_count]

    @staticmethod
    def export_plot_to_image(
        plot_widget: pg.PlotWidget,
        filename: str,
        width: int = 1920,
        height: int = 1080
    ):
        """导出图表为图像文件"""
        exporter = pg.exporters.ImageExporter(plot_widget.plotItem)
        exporter.parameters()['width'] = width
        exporter.parameters()['height'] = height
        exporter.export(filename)

    @staticmethod
    def export_data_to_csv(
        data: Dict[str, List[Tuple[float, float]]],
        filename: str
    ):
        """导出数据到CSV文件"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # 写入标题行
            header = ['Timestamp']
            for device_name in data.keys():
                header.extend([f'{device_name}_Time', f'{device_name}_Value'])
            writer.writerow(header)

            # 获取所有时间戳
            all_timestamps = set()
            for device_data in data.values():
                for timestamp, _ in device_data:
                    all_timestamps.add(timestamp)

            # 按时间排序
            sorted_timestamps = sorted(all_timestamps)

            # 写入数据行
            for timestamp in sorted_timestamps:
                row = [timestamp]
                for device_name, device_data in data.items():
                    # 查找该时间戳的数据
                    found_data = None
                    for ts, value in device_data:
                        if abs(ts - timestamp) < 1e-6:  # 浮点数比较
                            found_data = (ts, value)
                            break

                    if found_data:
                        row.extend([found_data[0], found_data[1]])
                    else:
                        row.extend(['', ''])

                writer.writerow(row)

    @staticmethod
    def export_data_to_json(
        data: Dict[str, List[Tuple[float, float]]],
        filename: str,
        metadata: Optional[Dict] = None
    ):
        """导出数据到JSON文件"""
        export_data = {
            'metadata': metadata or {},
            'export_time': datetime.now().isoformat(),
            'devices': {}
        }

        for device_name, device_data in data.items():
            export_data['devices'][device_name] = [
                {'timestamp': ts, 'value': val} for ts, val in device_data
            ]

        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(export_data, jsonfile, indent=2, ensure_ascii=False)

    @staticmethod
    def calculate_trigger_statistics(
        data: Dict[str, List[Tuple[float, float]]],
        time_window: float = None
    ) -> Dict[str, Dict]:
        """计算触发统计信息"""
        stats = {}
        current_time = datetime.now().timestamp()

        for device_name, device_data in data.items():
            if not device_data:
                stats[device_name] = {
                    'total_triggers': 0,
                    'trigger_rate': 0.0,
                    'last_trigger_time': None,
                    'avg_interval': 0.0
                }
                continue

            # 过滤时间窗口内的数据
            if time_window:
                filtered_data = [
                    (ts, val) for ts, val in device_data
                    if current_time - ts <= time_window
                ]
            else:
                filtered_data = device_data

            total_triggers = len(filtered_data)
            last_trigger_time = max(ts for ts, _ in filtered_data) if filtered_data else None

            # 计算触发率和平均间隔
            if total_triggers > 1 and time_window:
                trigger_rate = total_triggers / time_window
                # 计算相邻触发的时间间隔
                intervals = []
                sorted_data = sorted(filtered_data, key=lambda x: x[0])
                for i in range(1, len(sorted_data)):
                    interval = sorted_data[i][0] - sorted_data[i-1][0]
                    intervals.append(interval)
                avg_interval = np.mean(intervals) if intervals else 0.0
            else:
                trigger_rate = 0.0
                avg_interval = 0.0

            stats[device_name] = {
                'total_triggers': total_triggers,
                'trigger_rate': trigger_rate,
                'last_trigger_time': last_trigger_time,
                'avg_interval': avg_interval
            }

        return stats

    @staticmethod
    def create_scatter_plot_item(
        color: str,
        size: int = 8,
        symbol: str = 'o'
    ) -> pg.ScatterPlotItem:
        """创建散点图项目"""
        return pg.ScatterPlotItem(
            size=size,
            pen=pg.mkPen(color, width=2),
            brush=pg.mkBrush(color),
            symbol=symbol
        )

    @staticmethod
    def create_line_plot_item(
        color: str,
        width: int = 2,
        style: str = '-'
    ) -> pg.PlotDataItem:
        """创建线图项目"""
        pen_styles = {
            '-': pg.QtCore.Qt.PenStyle.SolidLine,
            '--': pg.QtCore.Qt.PenStyle.DashLine,
            ':': pg.QtCore.Qt.PenStyle.DotLine,
            '-.': pg.QtCore.Qt.PenStyle.DashDotLine
        }

        pen = pg.mkPen(
            color=color,
            width=width,
            style=pen_styles.get(style, pg.QtCore.Qt.PenStyle.SolidLine)
        )

        return pg.PlotDataItem(pen=pen)

    @staticmethod
    def optimize_plot_performance(plot_widget: pg.PlotWidget):
        """优化图表性能"""
        # 启用OpenGL加速（如果可用）
        try:
            plot_widget.useOpenGL(True)
        except:
            pass

        # 设置抗锯齿
        plot_widget.setRenderHint(plot_widget.RenderHint.Antialiasing, True)

        # 禁用自动范围调整（手动控制）
        plot_widget.enableAutoRange(axis='x', enable=False)
        plot_widget.enableAutoRange(axis='y', enable=False)

    @staticmethod
    def add_crosshair_cursor(plot_widget: pg.PlotWidget) -> Tuple[pg.InfiniteLine, pg.InfiniteLine]:
        """添加十字光标"""
        v_line = pg.InfiniteLine(angle=90, movable=False, pen='k')
        h_line = pg.InfiniteLine(angle=0, movable=False, pen='k')

        plot_widget.addItem(v_line, ignoreBounds=True)
        plot_widget.addItem(h_line, ignoreBounds=True)

        def mouse_moved(evt):
            pos = evt
            if plot_widget.sceneBoundingRect().contains(pos):
                mouse_point = plot_widget.plotItem.vb.mapSceneToView(pos)
                v_line.setPos(mouse_point.x())
                h_line.setPos(mouse_point.y())

        plot_widget.scene().sigMouseMoved.connect(mouse_moved)

        return v_line, h_line

    @staticmethod
    def format_timestamp(timestamp: float, format_type: str = 'time') -> str:
        """格式化时间戳"""
        dt = datetime.fromtimestamp(timestamp)

        if format_type == 'time':
            return dt.strftime("%H:%M:%S.%f")[:-3]  # 毫秒精度
        elif format_type == 'datetime':
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        elif format_type == 'iso':
            return dt.isoformat()
        else:
            return str(timestamp)