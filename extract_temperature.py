from PIL import Image

# 打开原始图像
original_image = Image.open('3.JPG')

# 定义新的尺寸
new_size = (480, 640)

# 调整图像大小
resized_image = original_image.resize(new_size, Image.ANTIALIAS)
# 设置DPI为72
dpi_value = 72
resized_image.save('7.JPG', dpi=(dpi_value, dpi_value))
