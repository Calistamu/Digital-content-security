clc;
clear all;
oi=imread('lenacolor.tif');%��������ͼ��
ni=rgb2gray(oi);
wi=ni;
[row col]=size(wi);
wi=double(wi);
wi=wi(:);
n=floor((row*col)/10);
length=row*col;
rand('state',123);%�������������Կ
a=rand(1,n);%����N���ȵ������
d=2.3;%�����޸ĵķ���
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
imshow(ni);title('ԭʼͼ��');%��ʾԭʼͼ��
subplot(1,2,2);
imshow(wil);title('ˮӡͼ��')%��ʾ��ͼ��
  