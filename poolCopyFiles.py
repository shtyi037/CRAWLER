import os
import hashlib
from multiprocessing import Pool,Manager

def copyFile(fileName, srcPath, destPath, q):
    if not os.path.exists(srcPath):
        print("scrPath %s is not exist "%srcPath)
        return False

    #如果目錄路徑不存在,創建新資料夾
    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except:
            print("destPath %s make error"%destPath)
            return False

    #構造源文件路徑名和目標文件路徑名
    srcFileName = srcPath+'/'+fileName
    destFileName = destPath+'/'+fileName

    #拷貝文件的過程
    with open(srcFileName, 'rb') as fr:
        with open(destFileName, 'wb') as fw:
            for i in fr:
                fw.write(i)

    #把剛剛拷貝完的文件添加到隊列中
    q.put(fileName)
    return True
    
#對文件做hash
CHUCKSIZE = 4096
def hashFile(fileName):
    h = hashlib.sha256()
    with  open(fileName, 'rb') as f:
        while True:
            chunk = f.read(CHUCKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


if __name__ =="__main__":
    srcPath = input("請輸入您要拷貝的文件目錄:")
    destPath = srcPath+"- 副本"

    while os.path.exists(destPath):
        destPath = destPath+"- 副本"

    #返回指定路徑下的文件和文件夾列表
    allFileNames = os.listdir(srcPath)
    allNum = len(allFileNames)
    num = 0
    q = Manager().Queue() # 注意：这里进程池中交互数据需要使用Manager进行托管
    pool = Pool()

    for i in allFileNames:
        #異步非阻塞
            pool.apply_async(func=copyFile, args=(i, srcPath, destPath,q))
    pool.close()
    while num < allNum:
        fileName = q.get()
        num += 1
        rate = num/allNum*100 # 计算当前的进度

        #再主進程中用hasg算法檢驗文件
        srcFileName = srcPath+'/'+fileName
        destFileName = destPath+'/'+fileName
        if (hashFile(srcFileName) == hashFile(destFileName)):
            print("%s copied ok"%srcFileName)
        else:
            print("%s copied failed"%srcFileName)

        # print("Current rate is %.1f%%"%rate)
        print("Current rate is %.2f%%"%rate)

    pool.join()
    print("Copy Files Done")