import pymongo
import os
from pymongo.mongo_client import MongoClient
from flask import Flask
from flask import redirect 
from flask import render_template
from flask import url_for
from PIL import Image
from io import BytesIO
from pymongo import DESCENDING
from flask import make_response

app = Flask(__name__, #__name__代表目前執行的模組
    static_folder="templates",
    static_url_path="/pelab" #http ://127.0.0.1:5051/pelab/index.html
    ) 

uri = "mongodb+srv://pelab_root:root8281@atlascluster.yet8e7d.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster" #資料庫所在位置
client = MongoClient(uri) #step2

@app.route("/") #連線到tset執行這裡
def test():
    return redirect("/pelab/index.html") #直接導向到http ://127.0.0.1:5051/pelab/index.html

# 發送一個ping確認連線成功
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Hey! You are a loser! Error : "+str(e))

db = client.MQTT #選擇操作MQTT資料庫 (可以自選)

part1_collection = db.part1 #選擇操作的 part1 集合 (可以自選)
@app.route("/pelab/ambline")
def part1_latest_image():
     latest_img_1 = part1_collection.find_one({}, sort=[('_id', -1)])

     if latest_img_1:
        image_binary = latest_img_1.get('image', b'') # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary)) #二進制轉圖片
            image1_path = os.path.join(app.static_folder, 'image1.png') #生成臨時名稱存到static
            image.save(image1_path)
            return render_template("env_temp.html", image_url_1=url_for('static', filename='image1.png')) #使用static裡的路徑顯示在前端

     return render_template("env_temp.html") # 沒圖繼續顯示html基礎設置
     
        # 設定緩存更新圖片
     response = make_response(render_template('env_temp.html', image_url_1=image_url_1))
     response.headers['Cache-Control'] = 'no-cache'

     return response
     
part2_collection = db.part2 #選擇操作的 part2 集合 (可以自選)
@app.route("/pelab/amblong")
def part2_latest_image():
     latest_img_2 = part2_collection.find_one({}, sort=[('_id', -1)])

     if latest_img_2:
        image_binary = latest_img_2.get('image', b'') # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary)) #二進制轉圖片
            image2_path = os.path.join(app.static_folder, 'image2.png') #生成臨時名稱存到static
            image.save(image2_path)
            return render_template("env_long.html", image_url_2=url_for('static', filename='image2.png')) #使用static裡的路徑顯示在前端

     return render_template("env_long.html") # 沒圖繼續顯示html基礎設置
     
        # 設定緩存更新圖片
     response = make_response(render_template('env_long.html', image_url_2=image_url_2))
     response.headers['Cache-Control'] = 'no-cache'

     return response

part3_collection = db.part3 #選擇操作的 part3 集合 (可以自選)
@app.route("/pelab/objline")
def part3_latest_image():
     latest_img_3 = part3_collection.find_one({}, sort=[('_id', -1)])

     if latest_img_3:
        image_binary = latest_img_3.get('image', b'') # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary)) #二進制轉圖片
            image3_path = os.path.join(app.static_folder, 'image3.png') #生成臨時名稱存到static
            image.save(image3_path)
            return render_template("obj_temp.html", image_url_3=url_for('static', filename='image3.png')) #使用static裡的路徑顯示在前端

     return render_template("obj_temp.html") # 沒圖繼續顯示html基礎設置
     
        # 設定緩存更新圖片
     response = make_response(render_template('obj_temp.html', image_url_3=image_url_3))
     response.headers['Cache-Control'] = 'no-cache'

     return response

part4_collection = db.part4 #選擇操作的 part4 集合 (可以自選)
@app.route("/pelab/objlong")
def part4_latest_image():
    latest_img_4 = part4_collection.find_one({}, sort=[('_id', -1)])

    if latest_img_4:
        image_binary = latest_img_4.get('image', b'') # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary)) #二進制轉圖片
            image4_path = os.path.join(app.static_folder, 'image4.png') #生成臨時名稱存到static
            image.save(image4_path)
            return render_template("obj_long.html", image_url_4=url_for('static', filename='image4.png')) #使用static裡的路徑顯示在前端

    return render_template("obj_long.html") # 沒圖繼續顯示html基礎設置
     
        # 設定緩存更新圖片
    response = make_response(render_template('obj_long.html', image_url_4=image_url_4))
    response.headers['Cache-Control'] = 'no-cache'

    return response

part5_collection = db.part5 #選擇操作的 part5 集合 (可以自選)
@app.route("/pelab/bucline")
def part5_latest_image():
     latest_img_5 = part5_collection.find_one({}, sort=[('_id', -1)])

     if latest_img_5:
        image_binary = latest_img_5.get('image', b'') # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary)) #二進制轉圖片
            image5_path = os.path.join(app.static_folder, 'image5.png') #生成臨時名稱存到static
            image.save(image5_path)
            return render_template("buc_temp.html", image_url_5=url_for('static', filename='image5.png')) #使用static裡的路徑顯示在前端

        return render_template("buc_temp.html") # 沒圖繼續顯示html基礎設置
     
        # 設定緩存更新圖片
        response = make_response(render_template('buc_temp.html', image_url_5=image_url_5))
        response.headers['Cache-Control'] = 'no-cache'

        return response

part6_collection = db.part6 #選擇操作的 part6 集合 (可以自選)
@app.route("/pelab/buclong")
def part6_latest_image():
    latest_img_6 = part6_collection.find_one({}, sort=[('_id', -1)])

    if latest_img_6:
        image_binary = latest_img_6.get('image', b'')  # 取得最新圖片的二進制碼
        if image_binary:
            image = Image.open(BytesIO(image_binary))  # 二進制轉圖片
            image6_path = os.path.join(app.static_folder, 'image6.png')  # 生成臨時名稱存到static
            image.save(image6_path)
            return render_template("buc_long.html", image_url_6=url_for('static', filename='image6.png'))  # 使用static裡的路徑顯示在前端

    # 沒圖繼續顯示html基礎設置
    return render_template("buc_long.html")

    # 設定緩存更新圖片
    response = make_response(render_template('buc_long.html', image_url_6=image_url_6))
    response.headers['Cache-Control'] = 'no-cache'

    return response


txt1_collection = db.odd 
@app.route("/pelab/ambnum")
def txt1_latest_data():
    all_data_cursor = txt1_collection.find({}, sort=[('_id', DESCENDING)])
    latest_data_1_cursor = all_data_cursor.limit(100)
    latest_data_1_list = list(latest_data_1_cursor)[::-1]
    return render_template("env_num.html", data=latest_data_1_list)

txt2_collection = db.even 
@app.route("/pelab/objnum")
def txt2_latest_data():
    all_data_cursor = txt2_collection.find({}, sort=[('_id', DESCENDING)])
    latest_data_2_cursor = all_data_cursor.limit(100)
    latest_data_2_list = list(latest_data_2_cursor)[::-1]
    return render_template("obj_num.html", data=latest_data_2_list)

txt3_collection = db.thr 
@app.route("/pelab/bucnum")
def txt3_latest_data():
    all_data_cursor = txt3_collection.find({}, sort=[('_id', DESCENDING)])
    latest_data_3_cursor = all_data_cursor.limit(100)
    latest_data_3_list = list(latest_data_3_cursor)[::-1]
    return render_template("buc_num.html", data=latest_data_3_list)

if __name__ == "__main__": #如果以主程式運行
    app.run(port=5051) #啟動伺服器
    
