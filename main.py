import json
import math

f = open('/home/kali/Загрузки/sepsis_json/split/newDataset (2).json')
d = json.load(f)
df = []

part_len = int(input())  #количество частей
length = int(len(d) / part_len)  #расчетный объем массива массивов

print(len(d))

for i in range(part_len):
    test = []
    train = []
    count = 0
    for item in d:
        count += 1
        if math.ceil(count/length) - 1 == i:
            test.append(item)
        else:
            train.append(item)

    print(len(test))
    print(len(train))

    f1 = open("/home/kali/Загрузки/sepsis_json/split/test"+str(i+1)+".json", 'w', encoding='utf-8')
    json.dump(test, f1, indent=4, ensure_ascii=False)

    f2 = open("/home/kali/Загрузки/sepsis_json/split/train"+str(i+1)+".json", 'w', encoding='utf-8')
    json.dump(train, f2, indent=4, ensure_ascii=False)
