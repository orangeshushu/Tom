import base64
from PIL import Image
from io import BytesIO
import json
import os

path = 'test_img'
output_folder = "test_img_res"
# path = 'raw_image_before1000'
for root_folder, each_folder, root_files in os.walk(path):
    print(root_folder, each_folder)
    break
for i in each_folder:
    whole_path = os.path.join(root_folder, i)
    output_path = os.path.join(output_folder, i)
    for root, dirs, files in os.walk(whole_path):
        for file in files:
            filepath = os.path.join(root, file)

            # 解析文件名（去掉扩展名）
            name = os.path.splitext(file)[0]

            # 创建一个1080*1440的纯黑色画布
            canvas = Image.new('RGB', (1080, 1440), (0, 0, 0))

            # 打开并读取 JSON 文件
            with open(filepath, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)

            # 解析 JSON 获取 imageData 和 位置
            base64_image_string = data['shapes'][0]['mask']
            position = data['shapes'][0]['points'][0]

            # 解码 base64 图片
            image_data = base64.b64decode(base64_image_string)
            image = Image.open(BytesIO(image_data))

            # 将解码的图片粘贴到指定位置
            canvas.paste(image, (int(position[0]), int(position[1])))

            # **确保目标目录存在**
            save_folder = output_path
            os.makedirs(save_folder, exist_ok=True)  # 创建目录（如果不存在）

            # **保存图片**
            save_path = os.path.join(save_folder, f"{name}.jpg")
            canvas.save(save_path)
            print(f"图片已保存：{save_path}")
