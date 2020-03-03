import json
from flask import Flask,abort
from flask import request,Response

from api.workdirectory import getList

app = Flask(__name__)

BASE_DIR = app.root_path

STORAGE_PATH = '/home/cav'

def resp(code,data):
   return Response(
     status=code,
     mimetype="application/json",
     response=(data)
   )


# получить список файлов и каталогов (в качестве параметра корень или каталог родитель)
# в json передаем путь
@app.route('/',methods=['POST'])
def getListFiles():
    res = {};
    print (request.headers)
    if not request.json:
        abort(400)
    print (request.json)
    jbj = request.json
    data = getList(STORAGE_PATH,jbj['path']);
    print (data)
    res['files'] = data
    print(json.dumps(res))
    return resp(200, "{}")

# получить файл (параметр порный путь к файлу)
def getFiles():
    pass

# сохранить файл (полный путь,название файла)
def setStoreFile():
    pass

# создать каталог (полный путь,название)
def createDir():
    pass

# удалить файл/каталог (полный путь)
def deleteFileOrDir():
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')