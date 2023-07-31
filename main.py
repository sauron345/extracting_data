import requests


def is_date(text: str):
    if len(text) == 10:
        return all(char.isdigit() or char == '-' for char in text)
    return False


r = requests.get('https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD')
json_item, date = '', ''
dates = []

with open('json_data.txt', 'w+') as f:
    f.write(str(r.json()))
    f.seek(0)  # 0 - set iteration at the beginning of the file, 1 - set iteration at the current file position
    # 2 - set iteration at the end of the file

    while True:
        ch = f.read(1)
        if not ch:
            break
        json_item += ch
        if "item" in json_item and 'T' in json_item:
            start_i = json_item.index("item")
            end_i = json_item.index("T")
            if ch == ',':
                for ch in json_item[start_i : end_i]:
                    if ch.isdigit() or ch == '-':
                        date += ch
                if is_date(date):
                    dates.append(date)
                json_item, date = '', ''

print(dates)
