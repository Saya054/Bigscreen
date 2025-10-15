import os
import shutil
'''
判断文件是否存在
'''
# mkdir基础版本，用来确认是否存在对应文件用的
def ExistFile(path,filename,type):
    path = repath(path)
    file = path +'\\'+filename+'.'+type
    res = os.path.exists(file)
    if not res:
        return False
    else:
        return True
#  检验zip包是否都存在用的
def Existfiles(file):
    res = os.path.exists(file)
    if not res:
        return False
    else:
        return True
# 判断是否有对应文件夹用的
def ExistFloader(path):
    path = repath(path)
    folder =  os.path.exists(path)
    if not folder:
        return False
    else:
        return True
'''
变更名字
'''
def repath(path):
    newpath = path.replace('/','\\')
    return newpath

'''
获取信息
'''
# 从路径中剥离文件名字用的
def getFilename(filepath):
    filepath = repath(filepath)
    if filepath != '':
        filewhole = filepath.split('\\')[-1]
        filename = filewhole.split('.')[0]
        return filename
    else:
        return False
def getFilePathList(path, filetype):
    pathList = []
    path = repath(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                pathList.append(os.path.join(root, file))
    return pathList  # 输出以filetype为后缀的列表
# 获取上级目录用的
def getparentpath(path):
    parent_path = os.path.dirname(path)
    return parent_path
## 从路径中剥离文件带后缀的名字用
def getRealFilename(filepath):
    filepath = repath(filepath)
    if filepath != '':
        filewhole = filepath.split('\\')[-1]
        return filewhole
    else:
        return False
# 根据文件路径值去除类型后缀，得到文件名字
'''
对文件操作
'''
# 创建文件路径（没有就创建）
def mkdir(path):
    path = repath(path)
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        try:
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # print("---  目录生成中...  ---")
            # print("---  OK  ---")
            return 'Create file Success'
        except Exception as e:
            # print('非法的目录名')
            return 'Invalid FileName'
    else:
        # print(f"---  {path}目录已存在！  ---")
        return 'Exists'
# 移动文件
def transform(path1,filename1,path2,filename2):
    path1 = repath(path1)
    path2 = repath(path2)
    filepath1 = path1+'\\'+filename1
    filepath2 = path2+'\\'+filename2
    try:
        shutil.move(filepath1, filepath2)
        return True
    except Exception as e:
        return False
def transformnew(file1,file2):
    try:
        shutil.move(file1, file2)
        return True
    except Exception as e:
        print(e)
        return False
# 删除文件用的
def removefile(path):
    try:
        shutil.rmtree(path)
        return True
    except Exception as e:
        return False
# 删除文件夹下文件
def del_file(path_data):
    path_data = repath(path_data)
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)
# 更改文件名字
def Bakrenamefile(filepath):
    res = os.path.exists(filepath)
    if res:
        filepath = repath(filepath)
        if filepath != '':
            filewhole = filepath.split('\\')[-1]
            filename = filewhole.split('.')[0]
            newfilename =  filename +'_bak'+'.'+filewhole.split('.')[-1]
            newfilepath = filepath.replace(filewhole,newfilename)
            try:
                os.rename(filepath,newfilepath)
                return newfilepath
            except:
                return False
# 重命名文件用的，实际没用到这个函数
def renamefile(filepath,newfilepath):
    res = os.path.exists(filepath)
    if res:
        try:
            os.rename(filepath, newfilepath)
        except:
            return False
# DBmode下的移动
def DBtransform(filepath1,filepath2):
    try:
        shutil.move(filepath1, filepath2)
        return True
    except Exception as e:
        return False