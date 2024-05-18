import os
a_path = 'D:\code\yolov5-master\datasets\\tongueset\labels\\train'
b_path = 'D:\code\yolov5-master\datasets\\tongueset\images\\train'

# Function to get file names without extensions from a given path
def get_filenames_without_extension(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filename, _ = os.path.splitext(file)
            filenames.append(filename)
    return filenames

# Get filenames without extensions from both paths
c_list = get_filenames_without_extension(a_path)
d_list = get_filenames_without_extension(b_path)

# Find differences between c and d lists
difference = set(c_list).symmetric_difference(set(d_list))

print(difference)