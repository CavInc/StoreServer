import json

import os
from flask import Flask, abort, send_from_directory
from flask import request,Response

from api.workdirectory import getList, makeDir, deleteFileOrDirectory, storeFile

app = Flask(__name__)

BASE_DIR = app.root_path

app.secret_key = b'\x9b\x18n\xa5_\xe3\xcc\xa7Wx\xb2\xfa\xeb\x83~?\xaa\x8f\x10A\xf5+#\x85'

STORAGE_PATH = '/home/cav/x/ServerTest'

def resp(code,data):
   return Response(
     status=code,
     mimetype="application/json",
     response=(data)
   )


# получить список файлов и каталогов (в качестве параметра корень или каталог родитель)
# в json передаем путь
@app.route('/api/getfiles',methods=['POST'])
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
@app.route("/api/getfile/<filename>")
def getFiles(filename):
    print (request.cookies)
    #print imgid
    if (filename is None):
        abort(404)

    print (filename)
    #uploads = os.path.join(STORAGE_PATH, app.config['IMG_FOLDER'])
    uploads = STORAGE_PATH
    try:
        return send_from_directory(directory=uploads, filename=filename)
    except Exception as e:
        print (e)
        abort(404)
    pass

# сохранить файл (полный путь,название файла)
@app.route("/api/sendfile",methods=['POST'])
def setStoreFile():
    print (request.form)
    print (request.files)

    storeFile(request.form,request.files,STORAGE_PATH)
    return resp(200, "{}")

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
    print (jbj)
    res = deleteFileOrDirectory(STORAGE_PATH,jbj['name'])
    return resp(200, json.dumps(res))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')