#!/bin/python
# -*- coding=utf-8 - *-
import cv2
import numpy as np

spread_width=5
alpha=10

#字符串转二进制且已扩频
def get_key(strr):
    str = ''
    for i in range(len(strr)):
        str = str+'{0:08b}'.format(ord(strr[i]))
    s=''
    for i in str:
        for j in range(spread_width):
            s=s+i
    return s

#嵌入水印
def embed(path,watercode,newpath):
    image_array = cv2.cv2.imread(path)#读取图像
    image_yuv=cv2.cvtColor(image_array,cv2.cv2.COLOR_BGR2YCR_CB) #色彩空间转换
    image_y=image_array[:,:,0]#提取y向量
    hanglength=image_y.shape[0]#获得行数
    lielength=image_y.shape[1]#获得列数
    flag=0#判断水印是否结束
    k=0#水印数组下标

    for i in range(0,hanglength,8):
        for j in range(0,lielength,8):
           #不满足8*8分块的不嵌入
            if i+8>hanglength:
                break
            if j+8>lielength:
                break

            array=np.zeros((8,8))#生成一个8*8的数组
            array=image_y[i:i+8,j:j+8].copy()#拷贝数组
            #print(array)#测试数据用
            array_float=np.float32(array)#转成浮点数
            arraydct=cv2.cv2.dct(array_float)#dct转换
            #print(arraydct)#测试数据用

            #水印嵌入
            intk=int(watercode[k])
            #print(intk)#测试数据用
            #a>b表示嵌入1，a<b表示嵌入0
            #如果嵌入为1,不满足a>b，交换;交换后判断如果a-b<alpha,a+=alpha
            if intk==1:
              if arraydct[4, 3] < arraydct[5, 2]:
                arraydct[4, 3], arraydct[5, 2] = arraydct[5, 2],arraydct[4, 3]
                if arraydct[4, 3] - arraydct[5, 2] < alpha:
                  arraydct[4, 3] += alpha
                elif arraydct[4, 3] == arraydct[5, 2]:
                  arraydct[4, 3] += alpha
            #如果嵌入为0,不满足a<b，交换;交换后判断如果b-a<alpha,a-=alpha
            elif intk==0:
              if arraydct[4, 3] > arraydct[5, 2]:
                arraydct[4, 3], arraydct[5, 2] = arraydct[5, 2], arraydct[4, 3]
                if arraydct[5, 2] - arraydct[4, 3] < alpha:
                  arraydct[4, 3] -= alpha
                elif arraydct[4, 3] == arraydct[5, 2]:
                  arraydct[4, 3] -= alpha

            arrayidct=cv2.cv2.idct(arraydct)#idct
            image_y[i:i+8,j:j+8]=arrayidct.copy()#放回原有的块中

            #判断是否水印结束，如果结束退出，否则下标+1
            if k==len(watercode)-1:
                flag=1
                break
            else :
                k+=1

        if flag==1:
            break

    image_array[:,:,0]=image_y#放回原数组
    image_newarray=cv2.cvtColor(image_array,cv2.cv2.COLOR_BGR2YCR_CB) #色彩空间转回
    cv2.cv2.imwrite(newpath,image_array)#存图

#提取
def extract(newpath):
    image_array=cv2.cv2.imread(newpath)
    #image_yuv=cv2.cv2.cvtColor(image_array,cv2.cv2.COLOR_BGR2YCR_CB)
    image_y=image_array[:,:,0]
    hanglength=image_y.shape[0]
    lielength=image_y.shape[1]

#提取水印
    watercode=''
    flaghang=0
    k=0
    for i in range(0,hanglength,8):
        for j in range(0,lielength,8):
            if i+8>hanglength:
                flaghang=1
                break
            if j+8>lielength:
                break
            array=np.zeros((8,8))#生成一个8*8的数组
            array_needdct=image_y[i:i+8,j:j+8].copy()#拷贝数组
            array_float=np.float32(array_needdct)
            arraydct=cv2.cv2.dct(array_float)
            #arraydct=cv2.dct(array_needdct)
            a=arraydct[1,0]
            b=arraydct[2,0]
            if a>b:
                watercode=watercode+'1'
            elif a<=b:
                watercode=watercode+'0'
        if flaghang==1:
            break
#水印缩减成原来的水印     
    j=0
    count1=0
    count0=0
    watercodeshort=''
    for i in watercode:
        if i=='1':
            count1+=1
            j+=1
        elif i=='0':
            count0+=1
            j+=1
        if j==5:
            if count1>count0:
                watercodeshort=watercodeshort+'1'
            else:
                watercodeshort=watercodeshort+'0'
            j=0
            count1=0
            count0=0
    #水印转化为字符
    j=0
    watermark=''
    for i in watercodeshort:
       w=''
       w=w+i
       j+=1
       if(j==8):
        j=0
        char=chr(int(w,2))  
        watermark+=char
        w=''
    
    print(watermark)

if __name__=='__main__':
        pictureurl='C:\\Users\\karen\\Desktop\\water\\lenacolor.bmp'#原图
        newpictureurl='C:\\Users\\karen\\Desktop\\water\\lenawatered.bmp'#嵌入水印后图
        key=get_key('chao')#水印内容
        #print(key)
        embed(pictureurl,key,newpictureurl)#嵌入
        extract(newpictureurl)#提取
   