%绘制psnr-q曲线
quality_array=zeros(1,100);  
psnr_array=zeros(1,100);  
f=imread('C:\Users\karen\Desktop\study\test\lenacolor.tif');  
for q=1:1:100     %q为质量因子  
   f1_path=strcat('C:\Users\karen\Desktop\study\test\jpged\lenajpged',num2str(q),'.jpg');     %f1_path为压缩后图片的路径  
   imwrite(f,f1_path,'quality',q)      %用不同的质量因子进行压缩  
   f1=imread(f1_path);        %读入压缩后的图片   
   peaksnr=psnr(f,f1);  
   quality_array(q)=q;  
   psnr_array(q)=peaksnr;  
end  
plot(quality_array,psnr_array);  

%将彩色图片转为灰度图
f=imread('C:\Users\karen\Desktop\study\test\lenacolor.tif');%读入彩色图片
I=rgb2ntsc(f);%颜色空间转换
I1=I(:,:,1);%取Y分量
imwrite(I1,'C:\Users\karen\Desktop\study\test\lenagrey.tif');%保存灰度图片
%将图像灰度值转为一维矩阵
f=imread('C:\Users\karen\Desktop\study\test\lenagrey.tif');
f_length=length(f(:))
%得到结果f_length =262144

f_array=reshape(f,1,f_length);

%%画灰度直方图
f=imread('C:\Users\karen\Desktop\study\test\lenagrey.tif');%原图转化为灰度图
imhist(f);%画出原灰度图的直方图

f1=imread('C:\Users\karen\Desktop\study\test\jpged\lenajpged25.jpg');
I=rgb2ntsc(f1);%颜色空间转换
I1=I(:,:,1);%取Y分量
imwrite(I1,'C:\Users\karen\Desktop\study\test\jpgedgrey\jpgedgrey25.jpg');%保存灰度图片
gray1=imread('C:\Users\karen\Desktop\study\test\jpgedgrey\jpgedgrey25.jpg');%读入filename1转化成的灰度图
imhist(gray1)%画出灰度图的直方图

%提取x宏块量化后DCT系数，逆DCT，在nsf5_simulation.m的基础上
try
    jobj = jpeg_read(COVER); % JPEG image structure
    DCT = jobj.coef_arrays{1}; % DCT plane
    f=DCT(128:192,256:320);%取矩阵子块
    imwrite(f,'C:\Users\karen\Desktop\study\test\nsf5_simulation\jpgednoidct.jpg')
    f1=idct2(f);%逆dct
    imwrite(f1,'C:\Users\karen\Desktop\study\test\nsf5_simulation\jpgedidct.jpg');%存图
catch
    error('ERROR (problem with the cover image)');
end