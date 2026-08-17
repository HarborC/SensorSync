# 传感器同步兼容矩阵与官方依据

## 1. 使用规则

本表的“可适配”表示厂家公开资料足以确定同步方法和主要电气接口，不等于本项目已经完成实机认证。量产支持状态只能在指定型号、硬件修订版、固件、适配板、线束和配置通过测试后由 `可适配` 改为 `已验证`。

任何系列名称都不能替代具体 SKU。相同外壳可能使用不同图像传感器、连接器或固件能力。

## 2. 深度与特殊相机

| 厂家/型号 | 可硬同步范围 | 所需适配 | 状态与限制 |
|---|---|---|---|
| RealSense D415 | depth + RGB | RS-1V8，pin 5/9 | 可适配；depth/RGB 必须相同 FPS |
| RealSense D455/D455f/D456 | depth + RGB | RS-1V8，pin 5/9 | 可适配；IMU 不受外部 SYNC 触发；D456 打开同步口影响 IP65 |
| RealSense D435/D435i/D435f/D435if | depth only | RS-1V8，pin 5/9 | 可适配；RGB/IMU 只能按设备时间戳关联 |
| RealSense D405 | 无外部多机硬同步 | 无 | 不适合作为六机同时曝光方案 |
| OAK-D S2 PoE | 2×OV9282 + IMX378 continuous FSYNC | OAK-ISO-12，M8 | 可适配；snapshot 仅 OV9282；IMU 时间戳关联 |
| OAK-D Pro/W/Pro W PoE | 取决于 IMX378/OV9782 变体 | OAK-ISO-12，M8 | 可适配；必须把传感器变体作为独立 SKU |
| OAK-D ToF | OV9782 FSYNC | OAK-5V，M8 | 可适配；5 V FSYNC |
| OAK4 D/Pro/S/CS | continuous FSYNC | OAK-5V，M8 | 条件可适配；RVC4 当前不承诺 snapshot，CS 需区分 OG05B10/IMX586 |
| OAK-D Lite | stereo 与 color 未共接 FSIN | 无通用整机方案 | 不列为三路同时硬同步型号 |

RealSense 外部源统一配置为相机 Slave，使用 1.8 V CMOS、100 µs 高脉冲，频率匹配真实帧率。OAK 老款 PoE 为 10~24 V 隔离 FSYNC 且内部逻辑反相，新款/OAK4 为 5 V FSYNC，两者不得共用直接输出。Luxonis 的 FSYNC Y-Adapter 页面与具体产品页存在 M8 针脚文字冲突；量产 OAK 线束必须以具体产品原理图、实物导通测试和厂家书面确认闭环。

## 3. 工业相机

| 厂家/型号 | 接口与同步 | PTP | 适配板 |
|---|---|---|---|
| HIKROBOT MV-CS023-10GM/GC、MV-CS050-10GM/GC | Line0 光耦输入 3.3~24 V，或非隔离 Line2 | 按具体型号功能表确认 | IND-SRC 或 OD-24 |
| HIKROBOT MV-CS023-10UM/UC、MV-CS050-10UM/UC | USB 数据，外部 Line Trigger | 无 | IND-SRC 或 OD-24 |
| Daheng MER2-503-23GM/GC(-P) | Line0 光耦 5~24 V；Line2/3 非隔离 1.9~24 V | 型号表明确 IEEE 1588v2 | IND-SRC |
| Daheng ME2P-1230-9GM/GC-P | Line0 光耦 5~24 V | 型号表明确 IEEE 1588v2 | IND-SRC |
| FLIR BFS-PGE-16S2M-CS | Line0 光耦 2.6~30 V；非隔离 GPI 2.6~3.6 V | 产品页明确 PTP | IND-SRC 或 3V3 |
| FLIR BFS-U3-16S2M-CS | USB 数据，硬件 Trigger | 无 | IND-SRC 或 3V3 |
| Basler a2A1920-51gmBAS | Line1 光耦；GPIO 0~24 V | ace 2 支持 IEEE 1588-2008 | IND-SRC 或 OD-24 |
| Basler a2A2448-23gmBAS | Line1 光耦；GPIO 0~24 V | ace 2 支持 IEEE 1588-2008 | IND-SRC 或 OD-24 |

工业相机使用品牌短线适配：HIK P7/P10、Daheng HR25-8、FLIR HR10-6、Basler M8-6。默认 100 µs 仅作为这些已核验型号的安全起始配置，最终频率、脉宽、有效边沿和曝光模式仍由相机配置模板限定。

## 4. 3D LiDAR

| 厂家/型号 | 官方同步方式 | 板端需求 | 状态 |
|---|---|---|---|
| Livox Mid-360 | IEEE 1588-2008，或 3.3 V LVTTL PPS + 9600-8N1 GPRMC | 3V3 PPS + UART 或 PTP 网络 | 可适配 |
| Ouster OS0/OS1/OS2 | PTP，或光耦 SYNC_PULSE_IN + NMEA GPRMC | 隔离脉冲 + 可配极性 UART，或 PTP | 可适配；具体代际/线束再确认 |
| Livox Mid-70 | README 目标型号 | 待取得对应版本官方 ICD | 预留，不列已验证 |
| RoboSense 系列 | README 目标系列 | 逐 SKU 获取用户手册/接口盒定义 | 预留，不列已验证 |
| Livox Tele-15/Horizon | README 目标系列 | 逐 SKU 获取用户手册/接口盒定义 | 预留，不列已验证 |

## 5. GNSS/RTK/组合导航

| 型号 | 时间能力 | 板端需求 | 状态 |
|---|---|---|---|
| u-blox ZED-F9P-04B | NMEA/UBX + TIMEPULSE；数据手册给出 30 ns RMS、60 ns (99%) | 模块级 3.3 V 电源/UART/TIMEPULSE 输入捕获 | 可作为板载或外接 GNSS 时间源 |
| 任意 NMEA0183 接收机 | 仅有 NMEA 不足以给出精确秒边沿 | 必须同时确认 PPS 电平、极性、脉宽和 NMEA 语句/波特率 | 按型号适配 |

ZED-F9P TIMEPULSE 驱动能力为 4 mA。它是模块逻辑信号，不是 12/24 V 工业 PPS；长线或隔离输入需要专用缓冲。

## 6. IMU

README 提到 Xsens 和 HiPNUC，但当前交付不把某个具体 IMU 标为“可直接接线”，因为型号尚未冻结且不同系列的 SyncIn/SyncOut、串口/RS-232/RS-422 和电压不同。主板保留两路：受保护低压 Trigger I/O、隔离式工业 Trigger、UART/RS-422。完成型号认证前，Xsens/HiPNUC 只能写“架构目标”，不能写“已验证”。

相机内置 IMU（RealSense、OAK）通常不由相机 Frame Sync 同时触发，应使用设备硬件时间戳和连续时钟映射关联。

## 7. Radar 与 4D Radar

Radar 没有统一的外部同步标准。主板预留两路 CAN-FD、Trigger/PPS 输入输出、UART，以及可选 100BASE-T1/PTP 子板。任何具体 Radar 只有取得厂家 ICD/DBC/ARXML，明确时间基准、报文端序、时间戳字段、PTP/gPTP profile、连接器和电气参数并实测后，才能列为已支持。

因此当前没有把某个普通 Radar 或 4D Radar 型号列入“可直接接线”表。Continental ARS、smartmicro、Arbe、Zendar 等可以作为采购候选，但公开营销资料不足以生成安全且可验证的同步线束，需向厂家申请集成资料。

## 8. 官方资料索引

- RealSense D400 Series Datasheet，Revision 022，December 2025，§3.7.4、§7.13：https://www.realsenseai.com/wp-content/uploads/2025/12/RealSense-D400-Series-Datasheet-Dec-2025.pdf
- RealSense Multi-Camera configurations，External Trigger/HW sync：https://dev.realsenseai.com/docs/multiple-depth-cameras-configuration/
- Luxonis Hardware synchronization：https://docs.luxonis.com/hardware/platform/deploy/data-sync/hardware-sync/
- Luxonis FSYNC Y-Adapter：https://docs.luxonis.com/hardware/products/FSYNC%20Y-Adapter/
- HIKROBOT 2026 标准产品目录：https://www.hikrobotics.com/cn2/source/vision/video/2026/3/26/机器视觉标准产品手册-V.121.CN.26Q1.1（阅读版）.pdf
- Daheng MERCURY2 GigE 应用说明书：https://www.daheng-imaging.com/index.php?m=content&c=index&a=file_down&id=2190&f=/uploadfile/2026/0724/20260724103225384.pdf
- FLIR Blackfly S GigE 产品页：https://www.teledynevisionsolutions.com/products/blackfly-s-gige/?model=BFS-PGE-16S2M-CS
- FLIR Blackfly S Installation Guide：https://flir.netx.net/file/asset/13147/original/attachment/
- Basler ace 2 a2A1920-51gmBAS：https://docs.baslerweb.com/a2a1920-51gmbas
- Basler opto-coupled I/O：https://docs.baslerweb.com/opto-coupled-io-lines
- Livox Mid-360 User Manual：https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/Livox/Livox_Mid-360_User_Manual_EN.pdf
- Ouster Time Synchronization：https://static.ouster.dev/sensor-docs/image_route1/image_route2/time_sync/time-sync.html
- u-blox ZED-F9P-04B Data Sheet R05：https://content.u-blox.com/sites/default/files/ZED-F9P-04B_DataSheet_UBX-21044850.pdf

资料 URL 和网页内容可能更新。产品数据库需保存文档版本、获取日期、SHA-256 和对应页码，不应只保存 URL。
