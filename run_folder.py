import os
data_folder_path = 'test'
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.pgm']

image_files = [os.path.join(data_folder_path, f) for f in os.listdir(data_folder_path) if os.path.splitext(f)[1].lower() in image_extensions]
counter = 0

with open('performance.csv', 'w') as f:
    f.write('file,mpa,miou,accuracy,f1_score,dice,jaccard,hausdorff_distance,yolo_box\n')

for image_file in image_files:
    command = 'python detect_dual.py --weights runs/train/tongue3/weights/best.pt --source ' + image_file.replace('\\', '/')
    print(command)
    os.system(command)
    print("Processing    " + str(counter))
    counter += 1
