# spread_spectrum_water
* spread_spectrum_water.py 水印嵌入与提取代码
* testpic 测试原图文件夹
* wateredpic 嵌入水印后的图片文件夹
* result 十幅图片的水印嵌入与嵌入结果以及性能分析
## 代码说明
spread_width=5 #扩频幅度  
alpha=10 #水印阈值  
get_key() #字符串转二进制字符串，二进制字符串扩频spread_width倍，即‘101’→‘111110000011111’  
embed() #嵌入函数，分成8*8块进行dct，选取块中数对(a,b)(此处选取[4,3]与[5,2]的值作比较),如果a>b,表示嵌入1，如果a\<\b，表示嵌入0。  
extract()   
#提取函数，根据embed()函数中选取的数对关系，比较a和b，a>b，水印字符串watercode加上'1'，a\<\b,watercode加上'0'。  
#watercode缩频，即'111110000011111'→'101'，缩频思想是根据spread_width对watercode进行分段，比较1与0的个数，谁多watercodeshort加上谁。  
#缩频后的watercodeshort二进制字符串转字符串并打印输出。  
#性能测试:提取到的扩频后水印序列watercode与原有扩频后水印序列water进行二进制字符串对比，得出正检率和误检率
#缺陷：当有错时，可能无法提取出正确的字符串

