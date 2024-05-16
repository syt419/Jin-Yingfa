from flask import Flask
from flask import redirect #載入redirect函式

app = Flask(__name__, #__name__代表目前執行的模組
    static_folder="www",
    static_url_path="/pelab" #http ://127.0.0.1:5051/pelab/index.html
    ) 

@app.route("/") #連線到tset執行這裡
def test():
    return redirect("/pelab/index.html") #直接導向到http ://127.0.0.1:5051/pelab/index.html

if __name__ == "__main__": #如果以主程式運行
    app.run(port=5051) #啟動伺服器