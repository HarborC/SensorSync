#!/usr/bin/env python3
"""
演示数据生成器

为SimpleSensorSync GUI生成模拟的触发信号数据
用于测试和演示GUI功能
"""

import time
import random
import threading
import json
from datetime import datetime

from infinite_sense_core.data import get_trigger_processor, TriggerEvent


class DemoDataGenerator:
    """演示数据生成器"""

    def __init__(self):
        self.running = False
        self.thread = None
        self.trigger_processor = get_trigger_processor()

        # 设备触发概率配置
        self.device_probabilities = {
            0: 0.8,   # IMU_1 - 高频
            1: 0.6,   # IMU_2 - 中频
            2: 0.3,   # CAM_1 - 低频
            3: 0.3,   # CAM_2 - 低频
            4: 0.2,   # CAM_3 - 很低频
            5: 0.2,   # CAM_4 - 很低频
            6: 0.1,   # LASER - 极低频
            7: 0.05,  # GPS - 极低频
        }

    def start(self):
        """开始生成数据"""
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._generate_data, daemon=True)
        self.thread.start()
        print("[Demo] 演示数据生成器已启动")

    def stop(self):
        """停止生成数据"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("[Demo] 演示数据生成器已停止")

    def _generate_data(self):
        """生成数据的主循环"""
        while self.running:
            # 随机生成触发状态
            status = 0
            triggered_devices = []

            for device_id, probability in self.device_probabilities.items():
                if random.random() < probability:
                    status |= (1 << device_id)
                    triggered_devices.append(device_id)

            # 只在有设备触发时发送事件
            if status > 0:
                current_time = int(time.time() * 1_000_000)  # 微秒时间戳

                trigger_event = TriggerEvent(
                    timestamp_us=current_time,
                    status=status
                )

                # 发送到触发处理器
                self.trigger_processor.process_trigger_data({
                    "f": "t",
                    "t": current_time,
                    "s": status
                })

                device_names = [
                    "IMU_1", "IMU_2", "CAM_1", "CAM_2",
                    "CAM_3", "CAM_4", "LASER", "GPS"
                ]
                triggered_names = [device_names[i] for i in triggered_devices]
                print(f"[Demo] 触发事件: {triggered_names} @ {trigger_event.timestamp_str}")

            # 随机间隔 (0.1-1.0秒)
            time.sleep(random.uniform(0.1, 1.0))


def main():
    """主函数 - 运行数据生成器"""
    import argparse

    parser = argparse.ArgumentParser(description="SimpleSensorSync 演示数据生成器")
    parser.add_argument("--duration", type=int, default=60, help="运行时长(秒, 默认60)")
    parser.add_argument("--freq", type=float, default=1.0, help="平均触发频率(Hz, 默认1.0)")

    args = parser.parse_args()

    generator = DemoDataGenerator()

    # 根据频率调整触发概率
    freq_factor = args.freq / 1.0  # 基准频率1Hz
    for device_id in generator.device_probabilities:
        generator.device_probabilities[device_id] *= freq_factor

    try:
        print(f"启动演示数据生成器，运行{args.duration}秒...")
        generator.start()

        # 运行指定时长
        time.sleep(args.duration)

    except KeyboardInterrupt:
        print("\n用户中断，正在停止...")
    finally:
        generator.stop()


if __name__ == "__main__":
    main()