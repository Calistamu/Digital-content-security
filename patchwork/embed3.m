clc;
clear all;
oi=imread('lenacolor.tif');%读入载体图像
ni=rgb2gray(oi);
wi=ni;
[row col]=size(wi);
wi=double(wi);
wi=wi(:);
n=floor((row*col)/10);
length=row*col;
rand('state',123);%产生随机数的密钥
a=rand(1,n);%产生N长度的随机数
d=2.3;%定义修改的分量
count=0;
k=1;
while k<=n
  if (a(1,k)>=0.5)
    wi(k*10,1)=wi(k*10,1)+d;
    wi(k*10-1,1)=wi(k*10-1,1)-d;
  end
  k=k+1;
end
for i=1:row
  for j=1:col
    wil(i,j)=wi(row*(j-1)+i,1);
  end
end
wil=uint8(wil);
imwrite(wil,'watermarked.bmp');
subplot(1,2,1);
imshow(ni);title('原始图像');%显示原始图像
subplot(1,2,2);
imshow(wil);title('水印图像')%显示新图像
  