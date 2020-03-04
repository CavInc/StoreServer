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
        if (l.find(".") == 0):
            continue
        if os.path.isfile(path+os.sep+l):
            print ('FILE')
            item['type']='FILE'
            item['size'] = os.path.getsize(path+os.sep+l)
        else :
            print ('DIR')
            item['type'] = 'DIR'
        out_data.append(item)
    return out_data

def makeDir(base_path,path,name):
    out_data = {}
    if path == '/':
        mk_path = base_path + os.sep + name
    else :
        mk_path = base_path + os.sep + path + os.sep + name
    if os.access(mk_path,os.F_OK) != True :
        os.mkdir(mk_path)
        out_data['status'] = True
    else :
        out_data['status'] = False
        out_data['msg'] = 'Directory exists'
    return out_data