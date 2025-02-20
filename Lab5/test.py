import re
import json

res = {
    "branch": "",
    "bin": "",
    "nds-series": "",
    "kassa": "",
    "smena": "",
    "sequence_number": "",
    "check_number": "",
    "kassir": "",
    "items": [],
    "ИТОГО" : "",
    "Фискальный признак" : "",
    "Time" : "",
    "Addres" : "",
    "ИНК ОФД" : "",
    "Код ККМ КГД" : "",
    "ЗНМ" : ""
 }

current_item = None

with open('row.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    line = line.strip()

    print(line)

    if re.search(r"Филиал ТОО EUROPHARMA Астана", line):
        res["branch"] = line
    elif re.search(r"БИН", line):
        res["bin"] = re.split(r"БИН ", line)[1]
    elif re.search(r"НДС Серия", line):
        res["nds-series"] = re.split(r"НДС Серия ", line)[1]
    elif re.search(r"Касса", line):
        res["kassa"] = re.split(r"Касса ", line)[1]
    elif re.search(r"Смена", line):
        res["smena"] = re.split(r"Смена ", line)[1]
    elif re.search(r"Порядковый номер чека №", line):
        res["sequence_number"] = re.split(r"Порядковый номер чека №", line)[1]
    elif re.search(r"Чек №", line):
        res["check_number"] = re.split(r"Чек №", line)[1]
    elif re.search(r"Кассир", line):
        res["kassir"] = re.split(r"Кассир ", line)[1]
    elif re.match(r"^\d+\.", line):
        if current_item:
            res["items"].append(current_item)
        current_item = {
            "id": re.sub(r"\.$", "", line),
            "name": "",
            "price": "",
            "quantity": "",
            "sum": ""
        }
    elif re.search(r" x ", line):
        quantity, price = re.split(r" x ", line)
        current_item["quantity"] = quantity.strip()
        current_item["price"] = price.strip()
    elif re.search(r"Стоимость", line):
        sum_value = lines[i + 1].strip()
        current_item["sum"] = sum_value
    elif re.search(r"ИТОГО:", line):
        end_value = lines[i + 1].strip()
        res["ИТОГО"] = end_value
    elif re.search(r"Фискальный признак:", line):
        f_value = lines[i + 1].strip()
        res["Фискальный признак"] = end_value
    elif re.search(r"Время:", line):
        res["Time"] = re.split(r"Время: ", line)[1]
    elif re.search(r"г. ", line):
        res["Addres"] = line
    elif re.search(r"ИНК ОФД: ", line):
        res["ИНК ОФД"] = re.split(r"ИНК ОФД: ", line)[1]
    elif re.search(r"Код ", line):
        res["Код ККМ КГД"] = line.split(' ')[-1]
    elif re.search(r"ЗНМ: ", line):
        res["ЗНМ"] = line.split(r"ЗНМ: ")[1]
    elif current_item and not current_item["name"]:
        current_item["name"] = line

if current_item:
    res["items"].append(current_item)

json_data = json.dumps(res, ensure_ascii=False, indent=4)

with open('receipt.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
