import os


def getList(base_path,path):
    out_data = []
    if path == '/':
        path = base_path
    else :
        path = base_path+os.sep+(path)

    for l in os.listdir(path):
        item = {}
        item['name']=l
        print(l)
        print (os.path.getsize(path+os.sep+l))
        if os.path.isfile(path+os.sep+l):
            print ('FILE')
            item['type']='FILE'
            item['size'] = os.path.getsize(path+os.sep+l)
        else :
            print ('DIR')
            item['type'] = 'DIR'
        out_data.append(item)
    return out_data

def makeDir(path):
    pass