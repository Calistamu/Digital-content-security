import cv2
import numpy as np

alpha=25

def pHash(img):    
    #加载并调整图片为32x32灰度图片    
    img=cv2.cv2.resize(img,(32,32),interpolation=cv2.cv2.INTER_CUBIC)    
    img=cv2.cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
    img = img.astype(np.float32)    
    #离散余弦变换    
    img = cv2.cv2.dct(img)    
    img = img[0:8,0:8]    
    avg = 0    
    hash_str = ''     
    #计算均值    
    for i in range(8):        
        for j in range(8):            
            avg += img[i,j]    
        avg = avg/64     
    #获得hash    
    for i in range(8):        
        for j in range(8):            
            if  img[i,j]>avg:                
                hash_str=hash_str+'1'            
            else:                
                hash_str=hash_str+'0'                
    return hash_str 
def cmpHash(hash1,hash2):    
    n=0    
    if len(hash1)!=len(hash2):        
        return -1    
    for i in range(len(hash1)):        
        if hash1[i]!=hash2[i]:            
            n=n+1    
    return n 
#加载图片
img1=cv2.cv2.imread('C:/Users/karen/Documents/GitHub/Digital-content-security/hash-perception/img/2-1.jpg')
img2=cv2.cv2.imread('C:/Users/karen/Documents/GitHub/Digital-content-security/hash-perception/img/2-2.jpg')
#计算hash
hash1= pHash(img1)
hash2= pHash(img2)
#计算汉明距离
n=cmpHash(hash1,hash2)
similiarity = ''
if n<alpha:    
    similiarity = 'similar'
else:    
    similiarity = 'disimilar'
print('感知哈希算法：{}  {:s}'.format(n,similiarity))
