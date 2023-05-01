# Block类
class Block:
    colors = {
        0: (255, 255, 255),
        2: (238, 228, 218),  # 灰白色
        4: (237, 224, 200),  # 浅黄色
        8: (242, 177, 121),  # 橙黄色
        16: (245, 149, 99),  # 橙红色
        32: (246, 124, 95),  # 红色
        64: (246, 94, 59),  # 红色
        128: (237, 207, 114),  # 黄色
        256: (237, 204, 97),  # 黄色
        512: (237, 200, 80),  # 黄色
        1024: (237, 197, 63),  # 黄色
        2048: (237, 194, 46),  # 黄色
        'other': (205, 193, 180)  # 灰色
    }

    def __init__(self, value):
        self.value = value
        self.color = self.get_block_color(value)

    def get_block_color(self, value):
        # 根据数值获取颜色
        if value > 2048:
            return self.colors['other']
        else:
            return self.colors[value]

    def get_value(self):
        # 获取数值
        return self.value

    def get_color(self):
        # 获取颜色
        return self.color
