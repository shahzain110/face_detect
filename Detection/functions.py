import psycopg2
import requests
import os

# Global Variables/Array
global names


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
    save_path = 'Detection/savedImages/'
    print("DOWNLOADING IMAGES NOW > > > >")
    cursor.execute('SELECT image_url,name FROM public."Detection_image_db"')
    all_records = cursor.fetchall()
    for index,item in enumerate(all_records):
        names.append(item[1])
        response = requests.get(item[0])
        file_name = f"{index}.jpg"
        completeName = os.path.join(save_path, file_name)
        file1 = open(completeName, "wb")
        file1.write(response.content)
        file1.close

getAllData()