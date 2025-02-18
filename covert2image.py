import base64
from PIL import Image
from io import BytesIO
import json
import os

path = 'test_img'
# path = 'raw_image_before1000'
for root, dirs, files in os.walk(path):
    for file in files:
        filepath = root + "/" + file
        name = file[:4]
        print(name)
        # 创建一个1080*1440的纯黑色画布
        canvas = Image.new('RGB', (1080, 1440), (0, 0, 0))

        # 打开并读取JSON文件
        with open(filepath, 'r', encoding='UTF-8') as file:
            data = json.load(file)

        # 获取'imageData'项的内容
        base64_image_string = data['shapes'][0]['mask']

        position = data['shapes'][0]['points'][0]
        # base64_image_string = ''

        image_data = base64.b64decode(base64_image_string)

        image = Image.open(BytesIO(image_data))

        # 将1.jpg放置在指定的(480, 640)坐标位置上
        canvas.paste(image, (int(position[0]), int(position[1])))

        # 保存合成后的图片为predict.jpg
        # canvas.save('pred_mask/ground truth/{filename}.jpg'.format(filename=name))
        canvas.save('test_img_res/{filename}.jpg'.format(filename=name))
