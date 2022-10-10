from deepface import DeepFace
from Detection.functions import names
from Detection.AI_model import models, getFeatureMap,threshold
from Detection.functions import dbImagePath

# image will come and id will be returned
def faceRecog_cus(file_path):
    try:
        for x in range(0,len(names)):
            img = dbImagePath + f'{x}.jpg'
            result = getFeatureMap(file_path,img)
            print(f"Face Recog : {result}")
            if result < threshold:
                index_to_Name = names[x]
                return index_to_Name
    except Exception as e:
        return f"Error Processing Recognization {e}"

def faceRecog_pre(file_path):
    try:
        result = DeepFace.find(img_path = file_path,
            db_path = dbImagePath, model_name = models[2],enforce_detection=False)
        similar_imgPath = str(result.iloc[0, 0])
    except Exception as e:
        return f"Face Not Found : {e}"
    try:    
        print(similar_imgPath)
        i = int(similar_imgPath[23:-4])
        index_to_Name = names[i]
    except Exception as e:
        return "Index to Image Failed"
    return index_to_Name
