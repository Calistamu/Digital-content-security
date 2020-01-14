clc;
clear;
oi=imread('watermarked.bmp');%读入嵌入水印后的图像
wi=oi;
[row col]=size(wi);
wi=double(wi);
wi=wi(:);
n=floor((row*col)/10);
r=1.6;
rand('state',123);%产生随机数的密钥
a=rand(1,n);%产生N长度的随机数
d=2.3;%定义修改的分量
count=0;
k=1;
tempa=0;
tempb=0;
while k<=n
  if(a(1,k)>=0.5)
    tempa=tempa+wi(k*10,1);
    tempb=tempb+wi(k*10-1,1);
    count=count+1;
  end
  k=k+1;
end
avea=tempa/count;
aveb=tempb/count;
if((avea-aveb)>r*d)
  disp("含有水印")
else
  disp("没有水印")
end
 