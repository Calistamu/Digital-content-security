clc;
clear;
oi=imread('watermarked.bmp');%����Ƕ��ˮӡ���ͼ��
wi=oi;
[row col]=size(wi);
wi=double(wi);
wi=wi(:);
n=floor((row*col)/10);
r=1.6;
rand('state',123);%�������������Կ
a=rand(1,n);%����N���ȵ������
d=2.3;%�����޸ĵķ���
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
  disp("����ˮӡ")
else
  disp("û��ˮӡ")
end
 