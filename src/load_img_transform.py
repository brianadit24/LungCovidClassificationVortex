import numpy as np
import cv2

def normalize(img):
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    img = np.array([(img[:,:,i] - mean[i]) / std[i] for i in range(len(mean))])

    return img

def transform_image(file):
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) < 3 else img
    img = cv2.resize(img, (224,224)).astype(np.float32)/255
    img = img[:,:,::-1]
    img = normalize(img)
    img = np.expand_dims(img, 0)

    return img