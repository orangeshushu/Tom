import numpy as np
from PIL import Image
import csv

# 读取CSV文件并将其转换为numpy数组
data = []
with open('3.csv', newline='', encoding='utf-8-sig') as csvfile:  # 使用 'utf-8-sig' 来自动处理BOM
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            # 尝试将每一项转换为浮点数，如果失败则跳过该项
            float_row = [float(i) for i in row if i.strip()]
            if float_row:  # 确保不添加空行
                data.append(float_row)
        except ValueError as e:
            print(f"Skipping row due to conversion error: {e}")

data = np.array(data)

# 获取数据的最大值和最小值
max_val = np.max(data)
min_val = np.min(data)

# 将数据归一化到0到255的范围内
normalized_data = (data - min_val) / (max_val - min_val) * 255
normalized_data = normalized_data.astype(np.uint8)

# 创建一个全红色的图像
red_image = np.zeros((640, 480, 3), dtype=np.uint8)
red_image[:, :, 0] = normalized_data  # 红色通道

# 将numpy数组转换为图像
img = Image.fromarray(red_image, 'RGB')

# 保存图像
img.save('10.jpg')

print("图像已保存为10.jpg")
