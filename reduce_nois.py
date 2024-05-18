import cv2

# 读取红外图像
infrared_image_path = '1008.jpg'
infrared_image = cv2.imread(infrared_image_path, cv2.IMREAD_GRAYSCALE)

# 应用颜色映射 - 例如，COLORMAP_JET
color_image = cv2.applyColorMap(infrared_image, cv2.COLORMAP_JET)

# 保存彩色图像
output_image_path = '10082.jpg'
cv2.imwrite(output_image_path, color_image)

# 显示图像（可选）
cv2.imshow('Infrared Image', infrared_image)
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
