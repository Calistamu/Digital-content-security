%ԭ��ѡȡ�������ϣ��޸ļ���֮���ĳ�ֹ�ϵ��Я��ˮӡ��Ϣ
clc;
clear all;
oi=imread('lenacolor.tif');%��������ͼ��
[row col]=size(oi);
d=2.3;%�����޸ĵķ���
wi=oi;
%ѡȡ��������������ϣ�����������֮�������ͬͼ��ϵ��
%��������֮��Ϊż�ӳ������������
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
subplot(1,2,1),imshow('lenacolor.tif'),title('ԭʼͼ��');
subplot(1,2,2),imshow('lenawatered.bmp'),title('ˮӡͼ��');