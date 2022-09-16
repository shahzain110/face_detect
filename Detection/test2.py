from deepface import DeepFace
import numpy as np
from AI_model import models
# 0.9999948143959045 babr
# 0.9999961853027344

# print(max(0.9999948143959045,0.9999961853027344 ))
# backends = [
#   'opencv', 
#   'ssd', 
#   'dlib', 
#   'mtcnn', 
#   'retinaface', 
#   'mediapipe'
# ]

array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])

face = DeepFace.verify(img1_path = array1, img2_path= array2, model_name = models[1])

print(face)