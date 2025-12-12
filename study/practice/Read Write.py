import json

# txt 파일 읽고 쓰기
# 읽기 : r / 쓰기 : w / 추가 : a
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write("hisadfasdf")
with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print(text)

# json
data = {"name" : "Lingard", "age" : 34}

with open('user.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2) # indent 들여쓰기, ensure_ascii 인쇄불가능한 문자 escape처리 여부
    
with open("user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
