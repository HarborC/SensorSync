import tkinter as tk

SENSOR_SPACING = 60  # 每个传感器之间的垂直间隔
TICK_INTERVAL = 100  # 时间刻度线间隔（ms）

# 示例传感器数据：{sensor_name: [timestamp1, timestamp2, ...]}
sensor_data = {
    "IMU": [100, 300, 500, 800],
    "Cam": [150, 350, 700],
    "Lid": [200, 600, 900]
}


class TimelineApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.time_scale = 1.0  # px / ms，初始比例
        self.time_offset = 0  # ms，时间轴左端对应时间（平移偏移）

        self.dragging = False
        self.last_x = 0

        self.canvas.bind("<ButtonPress-1>", self.on_drag_start)
        self.canvas.bind("<B1-Motion>", self.on_drag_motion)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)  # Windows/Mac
        self.canvas.bind("<Button-4>", self.on_mousewheel)  # Linux 鼠标滚轮向上
        self.canvas.bind("<Button-5>", self.on_mousewheel)  # Linux 鼠标滚轮向下

        # 绑定窗口尺寸变化事件
        self.canvas.bind("<Configure>", lambda e: self.draw())

        self.draw()

    def draw(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        sensors = list(sensor_data.keys())

        # 画每个传感器的时间轴
        for idx, sensor in enumerate(sensors):
            y = 50 + idx * SENSOR_SPACING
            self.canvas.create_text(30, y, text=sensor, anchor="e")
            self.canvas.create_line(40, y, width - 20, y, fill="gray", dash=(2, 2))

            for t in sensor_data[sensor]:
                # 时间根据偏移和缩放计算X坐标
                x = 40 + (t - self.time_offset) * self.time_scale
                if 40 <= x <= width - 20:
                    self.canvas.create_line(x, y - 10, x, y + 10, fill="blue")
                    self.canvas.create_text(x, y + 15, text=str(t), anchor="n", font=("Arial", 8))

        # 画时间刻度线
        max_time_display = self.time_offset + (width - 60) / self.time_scale
        t = (self.time_offset // TICK_INTERVAL) * TICK_INTERVAL
        while t <= max_time_display:
            x = 40 + (t - self.time_offset) * self.time_scale
            self.canvas.create_line(x, 20, x, height - 20, fill="lightgray", dash=(1, 2))
            self.canvas.create_text(x, 20, text=str(int(t)), anchor="s", font=("Arial", 8))
            t += TICK_INTERVAL

    def on_drag_start(self, event):
        self.dragging = True
        self.last_x = event.x

    def on_drag_motion(self, event):
        if self.dragging:
            dx = event.x - self.last_x
            self.last_x = event.x
            self.time_offset -= dx / self.time_scale
            if self.time_offset < 0:
                self.time_offset = 0
            self.draw()

    def on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            factor = 1.1
        else:
            factor = 0.9

        width = self.canvas.winfo_width()
        mouse_time = self.time_offset + (event.x - 40) / self.time_scale

        new_scale = self.time_scale * factor
        new_scale = max(0.1, min(new_scale, 10))

        self.time_offset = mouse_time - (event.x - 40) / new_scale
        if self.time_offset < 0:
            self.time_offset = 0

        self.time_scale = new_scale
        self.draw()
