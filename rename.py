import os

# 文件夹的路径
folder_path = './test'

# 遍历文件夹中的每个文件
for filename in os.listdir(folder_path):
    # 检查文件名是否足够长且包含数字
    if len(filename) >= 4 and filename[:4].isdigit():
        # 构造新文件名：保留前4位数字并添加原文件名的扩展名
        new_filename = filename[:4] + os.path.splitext(filename)[1]
        # 构造完整的原始文件路径和新文件路径
        original_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(original_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")
    else:
        # 如果文件名不符合条件，打印一条消息
        print(f"Skipped '{filename}'")

# 提示完成
print("Renaming process completed.")
