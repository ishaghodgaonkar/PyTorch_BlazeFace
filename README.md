# PyTorch_BlazeFace

Unofficial PyTorch implementation of [BlazeFace] - Sub-millisecond Neural Face detection on Mobile GPUs(https://sites.google.com/view/perception-cv4arvr/blazeface)

BlazeFace is a new-and-improved version of SSD-Mobilenet specially developed for face detection. SSD-Mobilenet is an object detection method built to be trained on any object detection dataset (PASCAL VOC, MS COCO). It performs well on different sizes and shapes of objects due to different anchor aspect ratios at each layer that produce detection predictions. BlazeFace has minimized the aspect ratio to a single aspect ratio (1:1) and reduced the number of layers that produce detection (2 layers as opposed to 6 layers in SSD-Mobilenet according to the paper). Besides this, BlazeFace utilizes an improved, more lightweight Mobilenet feature extractor. 

Training and testing functionality was added through modification of this implementation of SSD-VGG in Pytorch: https://github.com/amdegroot/ssd.pytorch

Modifications to the anchor box sizes can be found in config.py, under the WIDER_FACE configuration.

## To Train
```
python3 train.py
```

## To test on testing dataset
```
python3 test.py --real-time=False
```

## To test in real time
```
python3 test.py --real-time=True
```

## Paper
### BlazeFace: Sub-millisecond Neural Face Detection on Mobile GPUs
[[Project Page]](https://sites.google.com/view/perception-cv4arvr/blazeface)
[[Original Implementation]](https://github.com/google/mediapipe/tree/master/mediapipe/models#blazeface-face-detection-model)
