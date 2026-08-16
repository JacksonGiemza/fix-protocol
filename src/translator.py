import json

def translateLog(log_path):
    with open(r'.\data\fix_fields.json', 'r') as file:
        fields = json.load(file)
    with open(r'.\data\fix_enums.json', 'r') as file:
        enums = json.load(file)
    with open(log_path, 'r') as file:
        logs = json.load(file)

    translated = {}
    for log in logs:
        message = logs[log]['head'] + logs[log]['body'] + logs[log]['tail']
        data = {}
        for tag in message:
            tag = tag.split('=')
            values = {
                    "tag": tag[0],
                    "raw": tag[1],
                }
            
            if tag[0] in enums:
                try:
                    values['value'] = enums[tag[0]][tag[1]]
                except KeyError:
                    values['value'] = None
            if tag[0] in fields:
                data[fields[tag[0]]['Name']] = values
            
        translated[log] = {'raw': logs[log]['raw'],
                           'fields': data}
    return translated


def main():
    log_path = r'.\data\log.json'
    data = translateLog(log_path)
    with open(r".\data\log_translated.json", "w") as file:
            json.dump(data, file)
            
if __name__ == "__main__":
    main()
