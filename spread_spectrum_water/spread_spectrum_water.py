#!/bin/python
# -*- coding=utf-8 - *-
import cv2
import numpy as np
import numpy as np
import math

spread_width=5
alpha=10
def get_key1(strr):
    str = ''
    for i in range(len(strr)):
        str = str+'{0:08b}'.format(ord(strr[i]))
    s=''
    for i in str:
            s=s+i
    return s
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
            else:
              print("请输入正确的水印值，0或1。")
            arrayidct=cv2.cv2.idct(arraydct)#idct
            image_y[i:i+8,j:j+8]=arrayidct.copy()#放回原有的块中

            #判断是否水印结束，如果结束退出，否则下标+1
            if k==len(watercode)-1:
                flag=1
                break
            else:
                k+=1

        if flag==1:
            break

    image_array[:,:,0]=image_y#y向量放回
    image_newarray=cv2.cvtColor(image_array,cv2.cv2.COLOR_BGR2YCR_CB) #色彩空间转回
    cv2.cv2.imwrite(newpath,image_array)#存图

#提取
def extract(newpath,water):
    image_array=cv2.cv2.imread(newpath)#读取水印图片
    image_yuv=cv2.cv2.cvtColor(image_array,cv2.cv2.COLOR_BGR2YCR_CB)#色彩空间转换
    image_y=image_array[:,:,0]#提取y向量
    hanglength=image_y.shape[0]#获得行数
    lielength=image_y.shape[1]#获得列数
    waterlength=len(water)
#提取水印
    watercode=''#初始化水印
    flag=0
    k=0
    for i in range(0,hanglength,8):
        for j in range(0,lielength,8):

            if i+8>hanglength:
                break
            if j+8>lielength:
                break

            array=np.zeros((8,8))#生成一个8*8的数组
            array=image_y[i:i+8,j:j+8].copy()#拷贝数组
            array_float=np.float32(array)
            arraydct=cv2.cv2.dct(array_float)

            #根据数对关系提取出水印
            if arraydct[4,3]>arraydct[5,2]:
                watercode=watercode+'1'
            elif arraydct[4,3]<arraydct[5,2]:
                watercode=watercode+'0'
            
            if k==waterlength-1:
                    flag=1
                    break
            else:
                    k+=1

        if flag==1:
            break
    #print(watercode)#测试数据用

    right=0
    wrong=0
    for i in range(0,waterlength):
        if watercode[i]==water[i]:
            right+=1
        else:
            wrong+=1
    print("正检率：",right/waterlength)
    print("误检率：",wrong/waterlength)

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
            count0+=0
            j+=1
        if j==5:
            if count1>count0:
                watercodeshort=watercodeshort+'1'
            else:
                watercodeshort=watercodeshort+'0'
            j=0
            count1=0
            count0=0
    #print(watercodeshort)#测试数据用

#水印二进制转化为字符串并打印
    j=0
    watermark=''
    w=''
    for i in watercodeshort:
       w=w+i
       j+=1
       if(j==8):
           j=0
           char=chr(int(w,2))  
           watermark+=char
           w=''
    
    print(watermark)  

def psnr(img1, img2):
   mse = np.mean((img1*1.0- img2*1.0) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)

if __name__=='__main__':
        pictureurl='C:\\Users\\karen\\Documents\\GitHub\\Digital-content-security\\spread_spectrum_water\\testpic\\test1.bmp'#原图
        newpictureurl='C:\\Users\\karen\\Documents\\GitHub\\Digital-content-security\\spread_spectrum_water\\wateredpic\\watered1.bmp'#嵌入水印后图
        #key=get_key1('chao')#没有扩频的水印
        #print('没有扩频的水印：\n')
        #print(key)
        #keycode=''
        #for i in range(1,100):
            #keycode=keycode+'chao'
        key=get_key('chao')#水印内容
            #print(key)#测试数据用
        embed(pictureurl,key,newpictureurl)#嵌入
        extract(newpictureurl,key)#提取
            #img1=cv2.imread(pictureurl)
            #img2=cv2.imread(newpictureurl)
            #psnr=psnr(img1,img2)
            #print(psnr)
            #print('\n')
   