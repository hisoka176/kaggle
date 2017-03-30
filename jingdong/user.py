#encoding:utf-8
import sys
reload(sys)
import numpy as np
sys.setdefaultencoding('utf-8')

def loadData(filepath):
    data = list()
    with open(filepath) as f:
        
        for index,line in enumerate(f.readlines()):
            if index==0:
                print(line)
                continue
            line = line.rstrip('\r\n')
            array = line.split(',')
            array = [i.rstrip('\xcb\xea')  for i in array]
            data.append(array)
            
        return np.array(data)

def info():
    
if __name__=='__main__':
    filepath = r'/home/DATASET/JData_User.csv'
    data = loadData(filepath)
    print(data.shape)
    print(data[:,1])
    
