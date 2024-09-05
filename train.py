# import warnings
# warnings.filterwarnings('ignore')
# from ultralytics import YOLO

# if __name__ == '__main__':
#     model = YOLO('ultralytics/cfg/models/v8/yolov8n.yaml')
#     # model.load('yolov8n.pt') # loading pretrain weights
#     model.train(data='/home/hjj/Desktop/dataset/dataset_crowdhuman/data_exp.yaml',
#                 cache=False,
#                 imgsz=640,
#                 epochs=100,
#                 batch=16,
#                 close_mosaic=10,
#                 workers=8,
#                 device='0',
#                 optimizer='SGD', # using SGD
#                 # resume='', # last.pt path
#                 # amp=False, # close amp
#                 # fraction=0.2,
#                 project='runs/train',
#                 name='exp',
#                 )

from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO("//root/ultralytics/runs/obb/train29/weights/last.pt")
    model = YOLO("/root/ultralytics-main/ultralytics/cfg/models/v8/yolov8s-obb.yaml")
    # model.load('//root/ultralytics/runs/obb/train41/weights/best.pt') # loading pretrain weights
    model.train(data="/root/ultralytics-main/datasets/mydata.yaml", device="0", epochs=150, patience=50, imgsz=640,
                batch=64, resume=False, half=False, amp=True, single_cls=False)
    model.train(**{'cfg': "ultralytics-main/ultralytics/cfg/default.yaml"})

import os
import re

# # 定义要操作的文件夹路径
# folder_path = 'datasets/Barcode/val/labels'  # 请替换为你的文件夹路径
#
# # 遍历文件夹内的所有文件
# for filename in os.listdir(folder_path):
#     if filename.endswith('.txt'):
#         # 构造文件的完整路径
#         file_path = os.path.join(folder_path, filename)
#
#         try:
#             # 以读取模式打开文件
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 # 读取文件内容
#                 lines = file.readlines()
#
#             # 创建一个新的列表来保存修改后的行
#             new_lines = []
#
#             # 遍历每一行，将开头数字替换为0
#             for line in lines:
#                 # 使用正则表达式查找行开头的数字
#                 match = re.match(r'^\d+', line)
#                 if match:
#                     # 替换开头的数字为0
#                     new_line = '0' + line[match.end():]
#                 else:
#                     # 如果行开头没有数字，则保持原样
#                     new_line = line
#                 new_lines.append(new_line)
#
#             # 以写入模式打开文件，覆盖原内容
#             with open(file_path, 'w', encoding='utf-8') as file:
#                 file.writelines(new_lines)
#
#         except IOError as e:
#             print(f"I/O error({e.errno}): {e.strerror}")
#         except ValueError:
#             print(f"Could not convert data to an integer.")
#         except:
#             print(f"Unexpected error:", sys.exc_info()[0])
#             raise
#
# print("All text files have been processed.")
