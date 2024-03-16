import base64
from PIL import Image
from io import BytesIO
import json

# 创建一个1080*1440的纯黑色画布
canvas = Image.new('RGB', (2448, 3264), (0, 0, 0))

# 打开并读取JSON文件
with open('1038.json', 'r') as file:
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
canvas.save('predict.jpg')
