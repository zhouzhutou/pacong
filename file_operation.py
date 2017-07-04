import os

class FileOperation(object):

    def getFileNameList(self,dirPath):
        fileNameList=[]
        fileNameList=os.listdir(dirPath)
        return fileNameList

    def rename(self, dirPath, oldName, newName):
        os.rename(os.path.join(dirPath,oldName),os.path.join(dirPath,newName))