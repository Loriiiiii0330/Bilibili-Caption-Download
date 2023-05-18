import requests
import json
import codecs

url = "https://i0.hdslb.com/bfs/ai_subtitle/prod/65431085210776561965c148c7979fd16727553031de8fe37df"
response = requests.get(url)

# 将response对象中的JSON字符串解析为Python对象
data = json.loads(response.text)

# 将Python对象转换为JSON字符串，并将Unicode编码转换为中文字符
s = json.dumps(data, ensure_ascii=False)

# 将JSON字符串写入文件
with codecs.open("data.txt", "w", "utf-8") as f:
    f.write(s)