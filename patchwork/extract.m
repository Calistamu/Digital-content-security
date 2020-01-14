clc;
clear all;
d=2.3;
r=1.5;%确定一个阈值，当两个集合的样本差别大于d*r时，表示有水印信息
wi=imread('lenacolor.tif');%读入图像
wi=double(wi);%将unit8转为double,否则tempa也是unit8类型，最大值只能存储255
[row col]=size(wi);
tempa=0;
tempb=0;
count=0;
for i=1:row
    for j=1:col
        if mod(i+j,2)==0
            tempa
            tempa=tempa+wi(i,j);
            count=count+1;
        else 
            tempb=tempb+wi(i,j);
        end
    end
end
disp(tempa);
disp(tempb);
%avea=(tempa*2)/(row*col);
%aveb=(tempb*2)/(row*col);
value=2*count*d*(tempa-tempb);
n=sqrt(count);
if value>r*n*104
    watermark=1;
else 
    watermark=0;
end
if watermark==1
    disp('含有水印');
else 
    disp('没有水印');
end