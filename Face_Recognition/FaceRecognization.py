from deepface import DeepFace
from Detection.functions import names
from Detection.AI_model import models, getFeatureMap,threshold

# Input image will come and id will be returned

def faceRecog_cus():
    imagePath = 'Detection/UserSavedImg/0.jpg'
    for x in range(0,len(names)):
        img2 = f'Detection/savedImages/{x}.jpg'
        result = getFeatureMap(imagePath,img2)
        print(f"Face Recog : {result}")
        if result < threshold:
            index_to_Name = names[x]
            return index_to_Name


def faceRecog_pre():
    imagePath = 'Detection/UserSavedImg/0.jpg'
    result = DeepFace.find(img_path = imagePath, db_path = 'Detection/savedImages/', model_name = models[2])
    similar_imgPath = str(result.iloc[0, 0])
    i = int(similar_imgPath[23:-4])
    index_to_Name = names[i]
    return index_to_Name
