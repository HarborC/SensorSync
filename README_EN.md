<p align="center">
<img  style="width:50%;"  alt="Logo" src="assets/picture/main_logo.png">
<br>
<em>Stable · Easy to Use · Precise</em>
<br>
</p>
<p align="center">
<a href="README_EN.md">English</a>
</p>

---

# 🚀 [A Simple and Easy-to-Use Multi-Sensor Synchronization Solution](https://github.com/InfiniteSenseLab/SimpleSensorSync/wiki)！
   Multi-sensor time synchronization is a critical issue, especially for sensor fusion systems. Incorrect time alignment can cause data fusion errors and negatively affect system performance. For most researchers, this is a low-level and complex issue that is not their research focus. More attention should be paid to designing sensor fusion algorithms rather than struggling with time synchronization. That's why we designed this system — to make time synchronization no longer a hassle.

---

✨ Minimal dependencies – Reduce compilation overhead for faster builds.
🤖 ROS2 & Python support – Easily integrate into modern robotics and scripting workflows.
⏱ More accurate synchronization mechanism – Provides higher precision time coordination.
📡 Transparent data protocol (JSON) – Clearer and more flexible communication.
⚙️ Simpler configuration – Easy to get started, more convenient customization. See [Quick Start & System Guide](https://github.com/InfiniteSenseLab/SimpleSensorSync/wiki).
📜 Enhanced logging – More comprehensive records, more efficient debugging.
🌐 Flexible multi-platform deployment – (ZeroMQ) supports embedded/desktop/cloud deployments.
🔗 Support for multiple cameras 📷, LiDARs ⦿, IMUs 🧭 and GPS 🛰 for mixed signal coordination.
🔄 [Supports multiple sync boards](assets/doc/board_introduction.md) - V3/V4/MINI.
🛡️ Safe and reliable – Safer power and wiring design 🚫.

# News

>1. Onboard IMU chip prices have increased significantly, and the sync board price has been adjusted accordingly.
>2. Increased trigger pin current to 12mA for stronger pin drive capability.
>3. Support for pulse duty cycle adjustment.
>4. Onboard IMU frequency (attitude solution) increased to 200HZ.
>5. Complete [User Manual & System Guide](https://github.com/InfiniteSenseLab/SimpleSensorSync/wiki) released.
>6. Python-SDK released, sync visualization tool released.

<p align="center">
  <img alt="tool" src="https://github.com/user-attachments/assets/6787bf44-0433-4cee-9843-9e48ebab3e41" width="60%">
</p>

# Supported Devices

| Device Type      | Brand(s)                          | Sync Method |
|------------------|-----------------------------------|-------------|
| Depth Camera     | RealSense Series                  | PWM         |
| Industrial Camera (Ethernet) | Hikvision/HikRoboSense/Daheng/Jinghang/PointGrey/Basler/... | PWM         |
| Industrial Camera (USB)      | Hikvision/HikRoboSense/Daheng/Jinghang/PointGrey/Basler/... | PWM         |
| Special Camera   | OAK/...                           | PWM         |
| Third-party IMU   | Xsens Series/HiPNUC...            | PWM         |
| 3D LiDAR          | Mid360/Mid70/RoboSense/Tele-15/Horizon Series/Ouster/... | PPS        |
| RTK/GPS/GNSS      | All devices supporting NMEA0183   | NMEA        |
| Host (ARM/X86)    | Intel/AMD/Jetson/RockChip/...     | PTP         |

# Contact

[【Taobao】Multi-camera sync IMU LiDAR Mid360 hardware sync board GPS Ethernet Serial industrial camera ROS
Click the link to open directly or search on Taobao](https://item.taobao.com/item.htm?abbucket=20&id=832624497202&mi_id=0000hMPUBSVCRAYonU3gjxDgfdY-8yA6by6IijyfYwEQCjc&ns=1&priceTId=214787c217683999683236296e0ff7&skuId=5934998856763&spm=a21n57.1.hoverItem.1&utparam=%7B%22aplus_abtest%22%3A%229758fee20f89c46fbabfb29784cc8409%22%7D&xxc=taobaoSearch)

# Thanks

The sync board has been used by more and more users 🎉
Welcome to give suggestions and create Issues 🛠️📝
Let's make it better together! If you find it helpful, don't forget to leave us a ⭐ to support us ❤️