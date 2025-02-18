from PIL import Image
import numpy as np
import os


# 指定要遍历的目录
directory = 'test_img'
dic2 = 'test_img_res'

# 创建一个列表来保存找到的文件
a = []
b = []

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".JPEG"):
            # 将符合条件的文件路径加入列表
            a.append(os.path.join(root, file))

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(dic2):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".JPEG"):
            # 将符合条件的文件路径加入列表
            b.append(os.path.join(root, file))
print(a)

for i in b:
    print(i)
    print('data4_1' + i[9:])
    color_image = Image.open(i)
    mask_image = Image.open('data4_1' + i[9:])

    # 确保mask是单通道二值图像
    mask_image = mask_image.convert('L')  # 灰度图
    mask_image = mask_image.point(lambda p: p > 128 and 255)  # 二值化处理

    color_array = np.array(color_image)
    mask_array = np.array(mask_image)

    # 检查图像和遮罩的尺寸
    if color_array.shape[:2] != mask_array.shape:
        print("Color and mask dimensions do not match!")
        print('Color array shape:', color_array.shape)
        print('Mask array shape:', mask_array.shape)
        # 尝试调整color_image的尺寸以匹配mask_image
        color_image = color_image.transpose(Image.ROTATE_90)  # 旋转color_image
        color_array = np.array(color_image)  # 重新转换为数组

    # 应用 np.where
    result_array = np.where(mask_array[:, :, None] == 255, color_array, 255)
    result_image = Image.fromarray(result_array.astype('uint8'))
    result_image.save('res' + i[9:])





