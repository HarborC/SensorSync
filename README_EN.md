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

>1. Online auto-configuration tool is now available — open it in Chrome at [imaginative-fenglisu-9fcdf0.netlify.app](https://imaginative-fenglisu-9fcdf0.netlify.app/).
>2. New Python version user documentation.
>3. Increased trigger pin current to 12mA for stronger pin drive capability.
>4. Support for pulse duty cycle adjustment.
>5. Onboard IMU frequency (attitude solution) increased to 200HZ.
>6. Complete [User Manual & System Guide](https://github.com/InfiniteSenseLab/SimpleSensorSync/wiki) released.
>7. Python-SDK released, sync visualization tool released.

<table>
<tr>
<td align="center">
<img src="https://github.com/user-attachments/assets/6787bf44-0433-4cee-9843-9e48ebab3e41" width="400">
</td>

<td align="center">
<img src="https://private-user-images.githubusercontent.com/22969665/600415113-ec9255e4-0978-4188-a41e-485636df4fad.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAxMDM1ODQsIm5iZiI6MTc4MDEwMzI4NCwicGF0aCI6Ii8yMjk2OTY2NS82MDA0MTUxMTMtZWM5MjU1ZTQtMDk3OC00MTg4LWE0MWUtNDg1NjM2ZGY0ZmFkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMwVDAxMDgwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ1NTY2MDI3YTU5MGY3YjRhOTUyZWFkOWRjMmRlMmRiNjU5MGY0ODMxM2NiNjk4YTNmNTY4Njk0ZmU0Yzg3ZGUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.N47cam81n1R1qCqYbdpgxs10THxirbHQVK_N7DCa54I" width="400">
</td>
</tr>
</table>

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