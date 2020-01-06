
# def fenhang(infile,outfile):
#     infopen = open(infile,'r',encoding='utf-8')
#     outopen = open(outfile,'w',encoding='utf-8')
#     lines = infopen.readlines()
#     i = 1
#     for line in lines:
#         line = line.strip("\n")
#         if i % 2 == 0:
#             outopen.write(line)
#         else:
#             outopen.write(line)
#         if i%2==0:
#             outopen.write("\n")
#         i += 1
#     infopen.close()
#     outopen.close()
# fenhang("4.txt","3.txt")
#
# def clearBlankLine():
#     file1 = open('2.txt', 'r', encoding='utf-8') # 要去掉空行的文件
#     file2 = open('4.txt', 'w', encoding='utf-8') # 生成没有空行的文件
#     try:
#         for line in file1.readlines():
#             if line == '\n':
#                 line = line.strip("\n")
#             file2.write(line)
#     finally:
#         file1.close()
#         file2.close()
# if __name__ == '__main__':
#     clearBlankLine()

import re                                                 #使用正则库
# 打开文件
fo = open("匹配人名.txt", "r",encoding='utf-8') # 需要匹配的人名
co = open("2.txt", "r",encoding='utf-8')  #导入的聊天记录文件
target = co.readlines()                       #读取所有world文件中的行
for line in fo.readlines():                       #依次读取每行
    line = line.strip()                           #去掉每行头尾空白
    match_Result = re.search(line, "%s" %  target, re.M | re.I) #使用正则表达式来获取相同的字符串
   #正则匹配开始，使用search可以将全部符合条件的字符集都找出来
    if not match_Result:
        print(line) #输出不在此次名单的人名
# 关闭文件
fo.close()
co.close()


