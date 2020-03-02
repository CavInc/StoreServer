from flask import Flask,abort
from flask import request,Response

app = Flask(__name__)

BASE_DIR = app.root_path

def resp(code,data):
   return Response(
     status=code,
     mimetype="application/json",
     response=(data)
   )


# получить список файлов и каталогов (в качестве параметра корень или каталог родитель)

# получить файл (параметр порный путь к файлу)

# сохранить файл (полный путь,название файла)

# создать каталог (полный путь,название)

# удалить файл/каталог (полный путь)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')