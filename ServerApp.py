import json
from flask import Flask,abort
from flask import request,Response

from api.workdirectory import getList, makeDir, deleteFileOrDirectory

app = Flask(__name__)

BASE_DIR = app.root_path

STORAGE_PATH = '/home/cav/x/ServerTest'

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
    return resp(200, json.dumps(res))

# получить файл (параметр порный путь к файлу)
@app.route("/api/getfile")
def getFiles():
    pass

# сохранить файл (полный путь,название файла)
def setStoreFile():
    pass

# создать каталог (полный путь,название)
@app.route("/api/createdir",methods=['POST'])
def createDir():
    if not request.json:
        abort(400)
    jbj = request.json
    res = makeDir(STORAGE_PATH,jbj['path'],jbj['name'])
    print (res)
    return resp(200,json.dumps(res))

# удалить файл/каталог (полный путь)
@app.route("/api/deleteitem",methods=['POST'])
def deleteFileOrDir():
    if not request.json:
        abort(400)
    jbj = request.json
    res = deleteFileOrDirectory(STORAGE_PATH,jbj['name'])
    return resp(200, json.dumps(res))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')