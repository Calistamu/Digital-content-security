clc;
clear all;
d=2.3;
r=1.5;%ȷ��һ����ֵ�����������ϵ�����������d*rʱ����ʾ��ˮӡ��Ϣ
wi=imread('lenacolor.tif');%����ͼ��
wi=double(wi);%��unit8תΪdouble,����tempaҲ��unit8���ͣ����ֵֻ�ܴ洢255
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
    disp('����ˮӡ');
else 
    disp('û��ˮӡ');
end