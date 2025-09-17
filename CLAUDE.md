# CLAUDE.md

这个文件为 Claude Code (claude.ai/code) 在此代码仓库中工作时提供指导。

## 项目概述

SimpleSensorSync 是一个为机器人和传感器融合系统设计的多传感器同步解决方案。它使用专用同步板为相机、激光雷达、IMU 和 GPS 等各种传感器提供精确的时间协调。

## 架构

### 核心组件
- **infinite_sense_core/**: 提供同步功能的主库
  - `Synchronizer` 类: 网络、USB 和传感器管理的主协调器
  - `Messenger`: 基于 ZeroMQ 的数据交换通信系统
  - `TriggerManager`: 处理传感器同步的 PWM/PPS 触发信号
  - `NetManager`: 网络通信 (支持 PTP 协议)
  - `UsbManager`: 同步板控制的串口通信
  - `Sensor`: 传感器抽象基类

### 关键技术
- **ZeroMQ**: 主要消息/通信协议
- **PTP (精确时间协议)**: 网络时间同步
- **PWM/PPS**: 传感器硬件触发信号
- **JSON**: 数据序列化格式
- **CMake**: 构建系统，使用 C++17 标准

### 目录结构
- `infinite_sense_core/`: 核心同步库
  - `include/`: 头文件，包括主 API (`infinite_sense.h`)
  - `src/`: 实现文件
  - `third_party/`: 串口和 UDP 通信库
- `example/`: 演示用法的示例应用
  - `NetCam/`: 工业网络相机集成 (支持 ROS1/ROS2)
  - `CustomCam/`: 自定义相机 SDK 集成模板
  - `VideoCam/`: 视频相机示例
- `tools/monitor/`: 系统状态监控工具

## 构建命令

### 基本构建
```bash
# 创建构建目录并编译
mkdir -p build && cd build
cmake ..
make -j$(nproc)
```

### 平台特定说明
- 支持 ARM (aarch64) 和 x86_64 架构
- NetCam 示例自动检测平台并链接相应库
- 构建系统根据可用包条件编译 ROS1/ROS2 支持

### 依赖项
- **必需**: ZeroMQ, CMake 3.16+, C++17 编译器
- **可选**: ROS1 (catkin), ROS2 (ament), OpenCV (用于相机示例)

## 开发工作流

### 添加新传感器支持
1. 扩展 `infinite_sense_core/include/sensor.h` 中的 `Sensor` 基类
2. 实现传感器特定的初始化和触发处理
3. 在 `example/` 目录中按照 `CustomCam` 模板创建示例
4. 更新 CMakeLists.txt 以链接传感器 SDK 库

### 集成模式
- **ROS 集成**: 示例展示了双 ROS1/ROS2 支持模式
- **硬件抽象**: 使用 `TriggerManager` 进行同步板通信
- **数据流**: 传感器数据 → JSON 序列化 → ZeroMQ 消息传递
- **时间同步**: 结合 PTP (网络) + PWM/PPS (硬件) 实现精确同步

### 配置
- 通过 `Synchronizer::UseSensor()` 配置传感器
- 通过 `SetNetLink()` 设置网络用于 PTP 同步
- 通过 `SetUsbLink()` 设置串口用于同步板通信
- 通过 `SetLogPath()` 配置日志

## 测试和验证

使用内置监控工具监视系统状态：
```bash
# 构建并运行监控器
cd build/tools/monitor
./monitor
```

## 重要实现说明

- 系统需要硬件同步板 (V3/V4/MINI 版本)
- 网络相机需要正确的 PTP 配置以实现亚微秒精度
- 串口通信使用特定协议进行同步板控制
- ZeroMQ 处理所有组件间的消息传递和 JSON 序列化
- 构建系统自动处理 ROS1/ROS2 条件编译

## 支持的硬件

完整的设备兼容性列表请参考 README.md，包括：
- RealSense 深度相机 (PWM 同步)
- 主要厂商的工业相机 (PWM 同步)
- 3D 激光雷达传感器 (PPS 同步)
- IMU 设备 (PWM 同步)
- GPS/RTK 系统 (NMEA 同步)