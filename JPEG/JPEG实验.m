%����psnr-q����
quality_array=zeros(1,100);  
psnr_array=zeros(1,100);  
f=imread('C:\Users\karen\Desktop\study\test\lenacolor.tif');  
for q=1:1:100     %qΪ��������  
   f1_path=strcat('C:\Users\karen\Desktop\study\test\jpged\lenajpged',num2str(q),'.jpg');     %f1_pathΪѹ����ͼƬ��·��  
   imwrite(f,f1_path,'quality',q)      %�ò�ͬ���������ӽ���ѹ��  
   f1=imread(f1_path);        %����ѹ�����ͼƬ   
   peaksnr=psnr(f,f1);  
   quality_array(q)=q;  
   psnr_array(q)=peaksnr;  
end  
plot(quality_array,psnr_array);  

%����ɫͼƬתΪ�Ҷ�ͼ
f=imread('C:\Users\karen\Desktop\study\test\lenacolor.tif');%�����ɫͼƬ
I=rgb2ntsc(f);%��ɫ�ռ�ת��
I1=I(:,:,1);%ȡY����
imwrite(I1,'C:\Users\karen\Desktop\study\test\lenagrey.tif');%����Ҷ�ͼƬ
%��ͼ��Ҷ�ֵתΪһά����
f=imread('C:\Users\karen\Desktop\study\test\lenagrey.tif');
f_length=length(f(:))
%�õ����f_length =262144

f_array=reshape(f,1,f_length);

%%���Ҷ�ֱ��ͼ
f=imread('C:\Users\karen\Desktop\study\test\lenagrey.tif');%ԭͼת��Ϊ�Ҷ�ͼ
imhist(f);%����ԭ�Ҷ�ͼ��ֱ��ͼ

f1=imread('C:\Users\karen\Desktop\study\test\jpged\lenajpged25.jpg');
I=rgb2ntsc(f1);%��ɫ�ռ�ת��
I1=I(:,:,1);%ȡY����
imwrite(I1,'C:\Users\karen\Desktop\study\test\jpgedgrey\jpgedgrey25.jpg');%����Ҷ�ͼƬ
gray1=imread('C:\Users\karen\Desktop\study\test\jpgedgrey\jpgedgrey25.jpg');%����filename1ת���ɵĻҶ�ͼ
imhist(gray1)%�����Ҷ�ͼ��ֱ��ͼ

%��ȡx���������DCTϵ������DCT����nsf5_simulation.m�Ļ�����
try
    jobj = jpeg_read(COVER); % JPEG image structure
    DCT = jobj.coef_arrays{1}; % DCT plane
    f=DCT(128:192,256:320);%ȡ�����ӿ�
    imwrite(f,'C:\Users\karen\Desktop\study\test\nsf5_simulation\jpgednoidct.jpg')
    f1=idct2(f);%��dct
    imwrite(f1,'C:\Users\karen\Desktop\study\test\nsf5_simulation\jpgedidct.jpg');%��ͼ
catch
    error('ERROR (problem with the cover image)');
end