# SimpleSensorSync Python可视化工具开发计划

## 项目概述
基于现有SimpleSensorSync C++代码库，开发Python包装层和PyQt可视化界面，专注于触发信号解析和实时监控，提供简洁高效的多传感器同步管理工具。

## 现有代码库分析总结

### C++核心架构组件
- **TriggerManager**: 单例模式管理8个设备触发状态(IMU_1/2, CAM_1-4, LASER, GPS)
- **Messenger**: ZeroMQ发布/订阅通信，端口4565，支持结构体和字符串消息
- **Synchronizer**: 主协调器，支持串口/网络链接配置
- **TopicMonitor**: 实时监控ZeroMQ话题频率和活跃状态
- **传感器抽象**: 支持IMU、相机、激光雷达、GPS数据结构

### 现有Python基础代码 (python/)
- **项目结构**: 已配置uv环境 + pyproject.toml
- **基础模块**: infinite_sense_core/ 包含8个核心Python文件
  - `infinit_sense.py`: Synchronizer Python实现
  - `message.py`: Messenger ZeroMQ包装
  - `usb.py`: 串口通信模块
  - `net.py`: 网络通信模块
  - `ptp.py`: PTP时间同步
  - `data.py`: 数据结构定义
  - `times.py`: 时间处理工具
  - `app.py`: 应用层封装
- **依赖配置**: pyserial>=3.5, pyzmq>=27.0.1
- **示例代码**: main.py 包含基础使用示例

### 开发环境配置
```bash
# 进入项目Python目录
cd python/

# 激活uv虚拟环境
source .venv/bin/activate

# uv环境已配置，包含必要依赖
```

### 已有功能特性
- ✅ 8位触发状态位掩码管理
- ✅ 微秒级时间戳精度
- ✅ ZeroMQ实时通信机制
- ✅ 多平台架构检测(ARM/x86)
- ✅ ROS1/ROS2条件编译支持
- ✅ 串口/网络双模式同步板连接
- ✅ 实时话题监控和频率统计
- ✅ Python基础框架已搭建
- ✅ uv包管理环境配置完成

---

## 阶段一：Python核心增强和GUI框架 🐍

### [ ] 1.1 现有Python代码增强
- [ ] **基于现有infinite_sense_core模块优化**
  - [ ] 分析和完善 `infinit_sense.py` Synchronizer实现
  - [ ] 优化 `message.py` ZeroMQ消息处理性能
  - [ ] 增强 `data.py` 数据结构和触发状态解析
  - [ ] 完善 `times.py` 高精度时间戳处理
- [ ] **新增GUI相关模块**
  - [ ] 创建 `gui/

## GUI脚本命名规范方案 🎯

### [ ] GUI模块命名约定
- [ ] **核心组件命名**
  - [ ] 主窗口: `main_window.py` - 应用程序主界面
  - [ ] 设备面板: `device_panel.py` - 设备状态和控制面板
  - [ ] 信号图表: `signal_chart.py` - 实时触发信号可视化
  - [ ] 监控仪表: `monitor_dashboard.py` - 统计和监控数据展示
  - [ ] 配置对话框: `config_dialog.py` - 连接和设置配置界面

- [ ] **工具模块命名**
  - [ ] 数据导出: `data_exporter.py` - CSV/图表导出功能
  - [ ] 主题样式: `theme_manager.py` - PyQt样式和主题管理
  - [ ] 图表工具: `chart_utils.py` - pyqtgraph图表工具函数
  - [ ] 界面工具: `ui_utils.py` - 通用UI组件和工具

- [ ] **子包结构规划**
  ```
  gui/
  ├── __init__.py              # GUI包初始化
  ├── main_window.py           # 主应用窗口
  ├── widgets/                 # 自定义组件子包
  │   ├── __init__.py
  │   ├── device_panel.py      # 设备状态面板组件
  │   ├── signal_chart.py      # 信号图表组件
  │   └── trigger_indicator.py # 触发状态指示器
  ├── dialogs/                 # 对话框子包
  │   ├── __init__.py
  │   ├── config_dialog.py     # 配置对话框
  │   └── about_dialog.py      # 关于对话框
  ├── utils/                   # GUI工具子包
  │   ├── __init__.py
  │   ├── theme_manager.py     # 主题管理
  │   ├── chart_utils.py       # 图表工具
  │   └── ui_utils.py          # UI工具函数
  └── resources/               # 资源文件
      ├── icons/               # 图标文件
      ├── styles/              # 样式表文件
      └── themes/              # 主题配置
  ```

### [ ] 文件命名规范
- [ ] **命名约定**
  - [ ] 使用小写字母和下划线 (snake_case)
  - [ ] 文件名应清晰表达功能用途
  - [ ] 避免缩写，使用完整描述性名称
  - [ ] 类名使用帕斯卡命名法 (PascalCase)

- [ ] **模块前缀规范**
  - [ ] `main_*`: 主要应用窗口和入口点
  - [ ] `*_panel`: 功能面板组件
  - [ ] `*_dialog`: 对话框和弹窗
  - [ ] `*_chart`: 图表和可视化组件
  - [ ] `*_utils`: 工具函数和助手模块
  - [ ] `*_manager`: 管理器和控制器类

### [ ] 类和函数命名规范
- [ ] **PyQt组件类命名**
  - [ ] 主窗口类: `MainWindow` (继承自 QMainWindow)
  - [ ] 自定义组件: `*Widget`, `*Panel`, `*Chart`
  - [ ] 对话框类: `*Dialog` (继承自 QDialog)
  - [ ] 工具类: `*Manager`, `*Utils`, `*Helper`

- [ ] **方法命名约定**
  - [ ] Qt槽函数: `on_*_clicked`, `on_*_changed`
  - [ ] 初始化方法: `init_*`, `setup_*`
  - [ ] 更新方法: `update_*`, `refresh_*`
  - [ ] 数据处理: `process_*`, `handle_*`

### [ ] 导入和依赖规范
- [ ] **导入顺序标准**
  ```python
  # 标准库导入
  import sys
  from typing import Optional, Dict

  # 第三方库导入
  from PyQt6.QtWidgets import QMainWindow, QWidget
  from PyQt6.QtCore import QTimer, pyqtSignal
  import pyqtgraph as pg

  # 项目内部导入
  from ..infinite_sense_core import Synchronizer
  from .widgets.device_panel import DevicePanel
  ```

- [ ] **相对导入规范**
  - [ ] gui包内模块间使用相对导入
  - [ ] 避免循环导入依赖
  - [ ] 明确定义包内接口和边界` 子包用于PyQt界面
  - [ ] 实现触发信号可视化组件
  - [ ] 添加实时数据监控窗口
  - [ ] 配置PyQt6和pyqtgraph依赖
- [ ] **uv环境依赖管理**
  - [ ] 更新 `pyproject.toml` 添加GUI依赖
  - [ ] 配置开发和生产环境依赖分离
  - [ ] 添加开发工具依赖(black, pytest, mypy)

### [ ] 1.2 触发信号解析增强
- [ ] **信号解析引擎**
  - [ ] PWM信号波形分析
  - [ ] PPS信号精度测量
  - [ ] 触发延迟统计和补偿
  - [ ] 信号质量评估指标
- [ ] **数据缓冲和处理**
  - [ ] 高频数据环形缓冲区
  - [ ] 触发事件时序分析
  - [ ] 同步精度实时计算
  - [ ] 异常检测和报警机制

---

## 阶段二：PyQt简洁界面设计 🖥️

### [ ] 2.1 主界面布局(简洁风格)
- [ ] **单窗口设计**
  - [ ] 顶部: 连接状态和控制按钮
  - [ ] 左侧: 设备列表(8个触发设备)
  - [ ] 右侧: 触发信号可视化区域
  - [ ] 底部: 状态栏和简要统计信息

### [ ] 2.2 核心可视化组件
- [ ] **触发信号实时显示**
  - [ ] 8通道触发状态LED指示器
  - [ ] 触发时序图(时间轴+设备标识)
  - [ ] 触发频率实时柱状图
  - [ ] 同步精度散点图
- [ ] **设备状态面板**
  - [ ] 设备连接状态图标
  - [ ] 最后触发时间显示
  - [ ] 触发计数和频率统计
  - [ ] 设备健康状态指示

### [ ] 2.3 交互控制界面
- [ ] **连接配置对话框**
  - [ ] 串口选择和参数设置
  - [ ] 网络IP/端口配置
  - [ ] 连接测试和状态反馈
- [ ] **监控控制面板**
  - [ ] 开始/停止监控按钮
  - [ ] 数据记录开关
  - [ ] 显示刷新率调节
  - [ ] 导出数据功能

---

## 阶段三：数据处理和可视化优化 📊

### [ ] 3.1 实时数据流处理
- [ ] **高效数据管道**
  - [ ] 异步ZeroMQ消息接收
  - [ ] 多线程数据处理队列
  - [ ] 实时数据压缩和缓存
  - [ ] 内存使用优化管理
- [ ] **触发信号分析算法**
  - [ ] 触发间隔时间分析
  - [ ] 同步精度统计计算
  - [ ] 信号抖动检测
  - [ ] 设备协调性评估

### [ ] 3.2 高性能图表组件
- [ ] **PyQtGraph集成**
  - [ ] 实时波形绘制(1kHz+更新)
  - [ ] 多通道触发信号重叠显示
  - [ ] 可缩放时间轴和自动范围
  - [ ] 触发事件标记和注释
- [ ] **数据导出功能**
  - [ ] CSV格式触发数据导出
  - [ ] PNG/SVG图表截图保存
  - [ ] 时间段数据选择导出
  - [ ] 统计报告生成

---

## 阶段四：集成测试和优化 🔧

### [ ] 4.1 系统集成
- [ ] **多线程架构**
  - [ ] 主线程: PyQt界面渲染
  - [ ] 数据线程: ZeroMQ消息处理
  - [ ] 分析线程: 触发信号解析
  - [ ] 监控线程: 系统状态检查
- [ ] **线程同步机制**
  - [ ] 线程安全的数据队列
  - [ ] Qt信号槽跨线程通信
  - [ ] 资源竞争避免和死锁预防

### [ ] 4.2 性能优化和测试
- [ ] **性能基准**
  - [ ] 触发响应延迟 <1ms
  - [ ] 界面刷新率 ≥30fps
  - [ ] 内存占用 <100MB
  - [ ] CPU使用率 <20%
- [ ] **稳定性测试**
  - [ ] 24小时连续运行测试
  - [ ] 高频触发压力测试
  - [ ] 网络断连恢复测试
  - [ ] 异常场景处理验证

---

## 简化功能特性

### 核心功能(必需)
- [x] 8设备触发状态实时监控
- [x] 触发信号波形可视化
- [x] 串口/网络双模式连接
- [x] 基础数据导出功能

### 增强功能(可选)
- [ ] 触发精度统计分析
- [ ] 设备同步质量评估
- [ ] 历史数据回放功能
- [ ] 配置模板保存/加载

### 暂不实现
- ❌ 复杂的传感器SDK集成
- ❌ ROS节点发布功能
- ❌ 高级数据融合算法
- ❌ 多语言界面支持

---

## 技术栈和环境配置

### uv环境使用指南
```bash
# 进入Python开发目录
cd python/

# 激活uv虚拟环境
source .venv/bin/activate

# 安装GUI相关依赖
uv add PyQt6 pyqtgraph numpy

# 安装开发工具
uv add --dev black pytest mypy ruff

# 查看已安装依赖
uv pip list

# 退出虚拟环境
deactivate
```

### pyproject.toml 配置更新
```toml
[project]
name = "infinitesense"
version = "0.2.0"
requires-python = ">=3.10"
dependencies = [
    "pyserial>=3.5",
    "pyzmq>=27.0.1",
    "PyQt6>=6.4.0",
    "pyqtgraph>=0.13.0",
    "numpy>=1.21.0",
]

[tool.uv]
dev-dependencies = [
    "black>=23.0.0",
    "pytest>=7.0.0",
    "mypy>=1.0.0",
    "ruff>=0.1.0",
]
```

### 现有依赖分析
- ✅ **pyserial>=3.5**: 串口通信，已配置
- ✅ **pyzmq>=27.0.1**: ZeroMQ消息传递，已配置
- 🔄 **PyQt6**: GUI框架，需要添加
- 🔄 **pyqtgraph**: 高性能图表，需要添加
- 🔄 **numpy**: 数值计算，需要添加

---

## 开发时间线和环境准备

### 环境准备阶段
**预计时间**: 1周
**主要任务**:
- 配置uv环境GUI依赖
- 分析现有Python代码质量
- 设计GUI模块架构

### 开发阶段规划

| 阶段 | 时间 | 关键交付物 | uv环境操作 |
|------|------|-----------|-----------|
| 准备阶段 | 第1周 | 环境配置完成 | `uv add PyQt6 pyqtgraph numpy` |
| 阶段一 | 第2-3周 | Python核心增强 | 基于现有infinite_sense_core优化 |
| 阶段二 | 第4-5周 | PyQt基础界面 | GUI模块开发和测试 |
| 阶段三 | 第6-7周 | 可视化优化 | 触发信号实时显示 |
| 阶段四 | 第8周 | 集成测试 | 完整功能验证 |

## 成功标准

### 功能完整性
- ✅ 完全兼容现有C++触发管理功能
- ✅ 8设备触发状态100%准确显示
- ✅ 实时数据可视化流畅无卡顿
- ✅ 配置保存/加载功能正常

### 性能指标
- ✅ 触发检测延迟 ≤1毫秒
- ✅ 界面响应时间 ≤100毫秒
- ✅ 内存使用 ≤100MB
- ✅ 支持1kHz+触发频率监控

### 用户体验
- ✅ 一键启动监控功能
- ✅ 直观的设备状态指示
- ✅ 简洁的参数配置界面
- ✅ 可靠的数据导出功能

---

**最后更新**: 2025-09-17
**版本**: v2.0 - 基于现有代码库优化版
**负责人**: Claude Code Assistant