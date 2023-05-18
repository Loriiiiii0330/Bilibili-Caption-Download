import re 
relink = '<a href="(.*)">(.*)</a>'
info = '<a href="http://www.baidu.com">baidu</a>'
cinfo = re.findall(relink,info)
print(cinfo)