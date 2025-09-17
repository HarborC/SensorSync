# SimpleSensorSync GUI 使用说明

## 概述

SimpleSensorSync GUI 是基于 PyQt6 开发的多传感器同步监控图形界面。提供实时触发信号可视化、设备状态监控、配置管理等功能。

## 环境要求

- Python 3.10+
- uv 包管理器
- PyQt6, pyqtgraph, numpy (已在 pyproject.toml 中配置)

## 安装和启动

### 1. 环境准备

```bash
# 进入 Python 项目目录
cd python/

# 激活 uv 虚拟环境
source .venv/bin/activate

# 确认依赖已安装 (已配置完成)
uv pip list
```

### 2. 启动GUI应用

```bash
# 基本启动
python gui_main.py

# 使用深色主题
python gui_main.py --theme dark

# 启用调试日志
python gui_main.py --log-level DEBUG

# 保存日志到文件
python gui_main.py --log-file sensor_sync.log

# 查看帮助
python gui_main.py --help
```

## 功能特性

### 主界面功能

1. **设备状态面板** (左侧)
   - 实时显示8个传感器设备的触发状态
   - LED指示器显示设备活跃状态
   - 设备统计信息 (触发次数、最后触发时间)
   - 点击设备可在图表中高亮显示

2. **触发信号图表** (右侧)
   - 实时显示触发信号时序图
   - 支持多设备信号重叠显示
   - 可调节时间窗口 (5-300秒)
   - 支持设备显示开关控制

3. **菜单功能**
   - 文件 → 连接配置: 设置网络/串口连接参数
   - 监控 → 开始/停止监控: 控制数据采集
   - 帮助 → 关于: 查看应用信息

### 支持的传感器设备

- **IMU_1, IMU_2**: 惯性测量单元
- **CAM_1, CAM_2, CAM_3, CAM_4**: 相机设备
- **LASER**: 激光雷达
- **GPS**: GPS/RTK 系统

### 连接配置

#### 网络连接模式
- IP 地址: 同步板网络地址
- 端口: UDP 通信端口 (默认 8888)
- PTP 接口: 网络接口名称 (如 eth0)

#### 串口连接模式
- 串口设备: 自动检测可用串口
- 波特率: 支持常用波特率 (默认 115200)
- 数据位、停止位、校验位配置

## 架构设计

### 目录结构

```
infinite_sense_core/
├── gui/                    # GUI 模块
│   ├── main_window.py      # 主窗口
│   ├── widgets/            # 自定义组件
│   │   ├── device_panel.py      # 设备面板
│   │   ├── signal_chart.py      # 信号图表
│   │   └── trigger_indicator.py # 触发指示器
│   ├── dialogs/            # 对话框
│   │   ├── config_dialog.py     # 配置对话框
│   │   └── about_dialog.py      # 关于对话框
│   └── utils/              # 工具模块
│       ├── theme_manager.py     # 主题管理
│       ├── chart_utils.py       # 图表工具
│       └── ui_utils.py          # UI 工具
├── data.py                 # 增强的数据处理
├── infinit_sense.py        # 同步器核心
└── message.py              # ZeroMQ 通信
```

### 核心组件

1. **TriggerProcessor**: 触发信号处理器
   - 实时处理8位触发状态掩码
   - 支持回调函数注册
   - 提供设备统计信息

2. **SignalChart**: 信号图表组件
   - 基于 pyqtgraph 的高性能实时绘图
   - 支持散点图显示触发事件
   - 时间窗口可调，设备显示可控

3. **DevicePanel**: 设备面板组件
   - LED 风格的触发状态指示器
   - 实时统计信息更新
   - 设备选择和高亮功能

## 数据流程

```
硬件同步板 → USB/网络 → Synchronizer → TriggerProcessor → GUI组件
                                              ↓
                                        实时数据显示
```

1. 硬件同步板通过 USB 串口或网络发送触发数据
2. Synchronizer 协调 USB/网络管理器接收数据
3. TriggerProcessor 解析触发事件并调用回调函数
4. GUI 组件接收触发事件并更新显示

## 性能特性

- **实时响应**: 触发检测延迟 ≤1ms
- **界面流畅**: 30fps+ 的界面刷新率
- **内存优化**: 环形缓冲区管理历史数据
- **高频支持**: 支持 1kHz+ 的触发频率监控

## 主题支持

支持浅色和深色两种界面主题：

```bash
# 浅色主题 (默认)
python gui_main.py --theme light

# 深色主题
python gui_main.py --theme dark

# 自动主题 (根据系统设置)
python gui_main.py --theme auto
```

## 故障排除

### 常见问题

1. **PyQt6 导入错误**
   ```bash
   # 确保激活 uv 环境
   source .venv/bin/activate
   ```

2. **串口设备不可用**
   - 检查设备连接和权限
   - 在配置对话框中刷新串口列表

3. **网络连接失败**
   - 验证 IP 地址和端口配置
   - 检查网络连通性和防火墙设置

4. **显示问题**
   - 确保系统支持图形界面
   - 检查显示驱动和 OpenGL 支持

### 调试模式

启用详细日志进行问题诊断：

```bash
python gui_main.py --log-level DEBUG --log-file debug.log
```

## 开发扩展

### 添加新传感器设备

1. 在 `data.py` 中更新 `device_names` 列表
2. 在 `signal_chart.py` 中添加对应颜色
3. 更新设备面板显示逻辑

### 自定义主题

在 `theme_manager.py` 中添加新的主题样式表。

### 导出功能扩展

利用 `chart_utils.py` 中的工具函数添加更多数据导出格式。

## 技术栈

- **GUI框架**: PyQt6
- **图表库**: pyqtgraph
- **数值计算**: NumPy
- **通信**: ZeroMQ
- **串口**: pyserial
- **构建**: uv + pyproject.toml

## 版本信息

- 当前版本: 0.2.0
- 基于: SimpleSensorSync C++ 核心库
- 兼容: Python 3.10+, PyQt6 6.9+

---

**注意**: 该 GUI 应用需要与 SimpleSensorSync 硬件同步板配合使用，用于实际的多传感器同步监控场景。