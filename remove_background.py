import numpy as np
import pandas as pd
from PIL import Image
import csv

# 步骤 1: 读取二值图像并识别白色区域
image = Image.open('4.JPG').convert('L')  # 确保图片是灰度格式
mask = np.array(image) == 255  # 假设白色为255

# 步骤 2: 读取CSV文件并根据二值图像提取数值
data = []
max_length = 0
with open('5377.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row, m_row in zip(reader, mask):
        # 仅保存对应白色区域的数值
        filtered_row = [float(val) for val, m in zip(row, m_row) if m]
        max_length = max(max_length, len(filtered_row))  # 更新最大长度
        data.append(filtered_row)

# 填充所有行至最大长度
for i in range(len(data)):
    data[i] += [0] * (max_length - len(data[i]))  # 用0填充不足的部分

# 步骤 3: 将过滤后的数据保存为新的CSV文件
with open('3.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 步骤 4: 转换数据并创建红色图像
data = np.array(data)
max_val = np.max(data)
min_val = np.min(data)
normalized_data = (data - min_val) / (max_val - min_val) * 255
normalized_data = normalized_data.astype(np.uint8)

# 创建红色图像
height, width = normalized_data.shape
red_image = np.zeros((height, width, 3), dtype=np.uint8)
red_image[:, :, 0] = normalized_data  # 设置红色通道

# 将数组转换为图像并保存
red_img = Image.fromarray(red_image, 'RGB')
red_img.save('result.jpg')

print("完成任务，生成的图像已保存为 'result.jpg'")
