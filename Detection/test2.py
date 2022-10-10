import numpy as np
from PIL import Image as im
import pickle
from functions import dbImagePath, names

# from deepface import DeepFace
# similar_imgPath = "Detection/savedImages//2.jpg"
# # result = DeepFace.find(img_path = 'Detection/savedImages/8.jpg', db_path = 'Detection/savedImages',enforce_detection=False)
# print(int(similar_imgPath[23:-4]))

# hey = "shah"

# def test():
#     global hey
#     hey = "HAH"
#     print(hey)
#     print("TeSING>>>")



# test()

filename = dbImagePath + 'dbImages'
infile = open(filename,'rb')
featureMaps = pickle.load(infile)
infile.close()
# print(featureMaps['1'])
# img = dbImagePath + f'{x}.jpg'
res = np.allclose(featureMaps['1'],featureMaps['2'])
print(res)