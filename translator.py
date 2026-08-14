import json

with open(r'data\fix_fields.json', 'r') as file:
    fields = json.load(file)
with open(r'data\fix_enums.json', 'r') as file:
    enums = json.load(file)

with open(r'data\log.json', 'r') as file:
    logs = json.load(file)

translated = {}
for log in logs:
    body = logs[log]['body']
    data = {}
    for tag in body:
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
        
    translated[log] = data

print(translated)