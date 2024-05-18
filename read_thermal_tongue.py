# 导入需要的库
from flirimageextractor import FlirImageExtractor
import pandas as pd
import numpy as np
from PIL import Image

# 创建FlirImageExtractor实例
fir = FlirImageExtractor(palettes=[0], is_debug=True)

# 处理FLIR图片文件
fir.process_image('./data/sample.jpg')

# 获取温度数据
temperature_array = fir.get_thermal_np()

# 获取图像的分辨率（高度和宽度）
height, width = temperature_array.shape
print(f"Image Resolution: {width} x {height}")

# 将温度数据转换成Pandas DataFrame，便于导出
df = pd.DataFrame(temperature_array)

# 将DataFrame保存到CSV文件
df.to_csv('./data/tongue_temperature.csv', index=False)

image = Image.open('data/sample.jpg')
# 获取图像的分辨率
width, height = image.size

# 打印图像的分辨率
print(f"Image Resolution: {width} x {height}")