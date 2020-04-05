# config.py
import os.path

# gets home dir cross platform
HOME = os.path.expanduser("~")

# for making bounding boxes pretty
COLORS = ((255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128),
          (0, 255, 255, 128), (255, 0, 255, 128), (255, 255, 0, 128))

MEANS = (104, 117, 123)

# SSD300 CONFIGS
voc = {
    'num_classes': 21,
    'lr_steps': (80000, 100000, 120000),
    'max_iter': 120000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [30, 60, 111, 162, 213, 264],
    'max_sizes': [60, 111, 162, 213, 264, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}
"""
wider_face = {
    'num_classes': 2,
    'lr_steps': (80000, 100000, 120000),
    'max_iter': 120000,
    'feature_maps': [16, 8],
    'min_dim': 128,
    'steps': [8, 16],
    'min_sizes': [32, 51],
    'max_sizes': [51, 80],
    'aspect_ratios': [],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'WIDER_face',
}
"""
"""
wider_face = {
    'num_classes': 2,
    'lr_steps': (80000, 100000, 120000),
    'max_iter': 120000,
    'feature_maps': [16, 16, 16, 8],
    'min_dim': 128,
    'steps': [8, 8, 8, 16],
    'min_sizes': [19, 38, 57, 76],
    'max_sizes': [38, 57, 76, 96],
    'aspect_ratios': [],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}
"""
wider_face = {
    'num_classes': 2,
    'lr_steps': (80000, 100000, 120000),
    'max_iter': 120000,
    'feature_maps': [128, 64, 32, 16, 8],
    'min_dim': 128,
    'steps': [1, 2, 4, 8, 16],
    'min_sizes': [16, 38, 56, 78, 96],
    'max_sizes': [38, 56, 78, 96, 128],
    'aspect_ratios': [],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'VOC',
}
coco = {
    'num_classes': 201,
    'lr_steps': (280000, 360000, 400000),
    'max_iter': 400000,
    'feature_maps': [38, 19, 10, 5, 3, 1],
    'min_dim': 300,
    'steps': [8, 16, 32, 64, 100, 300],
    'min_sizes': [21, 45, 99, 153, 207, 261],
    'max_sizes': [45, 99, 153, 207, 261, 315],
    'aspect_ratios': [[2], [2, 3], [2, 3], [2, 3], [2], [2]],
    'variance': [0.1, 0.2],
    'clip': True,
    'name': 'COCO',
}


#
# wider_face = {
#     'num_classes': 2,
#     'lr_steps': (280000, 360000, 400000),
#     'max_iter': 400000,
#     'feature_maps': [[32, 32], [16, 16], [8, 8]],
#     'min_dim': 1024,
#     'steps': [8, 16, 32, 64, 100, 300],
#     'min_sizes': [[32, 64, 128], [256], [512]],
#     'max_sizes': [45, 99, 153, 207, 261, 315],
#     'aspect_ratios': [[1], [1], [1]],
#     'variance': [0.1, 0.2],
#     'clip': True,
#     'name': 'WIDER_face',
# }




