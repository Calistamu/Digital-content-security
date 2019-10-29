%原理：选取两个集合，修改集合之间的某种关系来携带水印信息
clc;
clear all;
oi=imread('lenacolor.tif');%读入载体图像
[row col]=size(oi);
d=2.3;%定义修改的分量
wi=oi;
%选取数据组成两个集合，且两个集合之间具有相同图像系数
%横纵坐标之和为偶加常量，奇减常量
count=0;
for i=1:row     
    for j=1:col
        if mod(i+j,2)==0
            wi(i,j)=wi(i,j)+d;
            count=count+1;
        else
            wi(i,j)=wi(i,j)-d;
        end
    end
end
disp(count);
imwrite(oi,'lenawatered.bmp');
subplot(1,2,1),imshow('lenacolor.tif'),title('原始图像');
subplot(1,2,2),imshow('lenawatered.bmp'),title('水印图像');