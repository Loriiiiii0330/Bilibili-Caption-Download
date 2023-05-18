import requests
import json
import codecs

print('''
打开目标视频，随后右键-网页检查，点击network，点击清除；
随后打开字幕，在新刷新的项目中找到非web开头的，一般为数字开头
再复制headers里的requestURL即可
        ''')
url = input("输入目标url：")
title = input("输入目标标题：")
response = requests.get(url)

if response.status_code == 200:
    # 将response对象中的JSON字符串解析为Python对象
    data = json.loads(response.text)

    # 将Python对象转换为JSON字符串，并将Unicode编码转换为中文字符
    s = json.dumps(data, ensure_ascii=False)

    # 将JSON字符串写入文件
    with codecs.open("Target_Subtitle.txt", "w", "utf-8") as f:
        f.write(s)
else:
    print("Failed to download data")


f = open(r"E:\脚本\Target_Subtitle.txt","r", encoding="utf-8")
file_int = f.readlines()[0]
file_pro = file_int.split('}')

keyword = '"content": "'

with open(title+"output字幕.txt", "w") as file:
    for line in file_pro:
        if keyword in line:
            index = line.index(keyword)
            # 如果关键词 ", 存在，则使用rstrip()方法将其后面的所有内容去掉
            result = line[index + len(keyword) : line.rindex('",')].rstrip('')
            print(result)
            file.write(result + '\n')

