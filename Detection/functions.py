import psycopg2
import requests
import os

# Global Variables/Array
global names
dbImagePath = 'Detection/dbImages/'

try:
    connection = psycopg2.connect(user="shahzain",
                                    password="admin",
                                    host="localhost",
                                    port="5432",
                                    database="face_detect")
    cursor = connection.cursor()
except Exception as e:
    print(e)

# Stores Images Locally & Store Names in array
names = []

def getAllData():
    print("DOWNLOADING IMAGES NOW > > > >")
    try:
        cursor.execute('SELECT image_url,name FROM public."Detection_image_db"')
        all_records = cursor.fetchall()
        for index,item in enumerate(all_records):
            names.append(item[1])
            response = requests.get(item[0])
            file_name = f"{index}.jpg"
            completeName = os.path.join(dbImagePath, file_name)
            file1 = open(completeName, "wb")
            file1.write(response.content)
            file1.close
    except Exception as e:
        print(f"Unable to download Images {e}")

# for downloading image
def downloadFile(file_path, img_01):
    try:
        f = open(file_path, 'wb')
        f.write(img_01)
        f.close()
        return True
    except Exception as e:
        return False

getAllData()