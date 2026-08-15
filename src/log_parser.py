import pandas as pd
import json


def parseLog(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        log = file.read()

    log = log.split('')

    curr = ''
    i = -1

    data = {}
    for element in log:
        element = element.replace("\n", "")
        if element == '':
            continue

        if element[:2] == "8=":
            i += 1
            curr = 'head'

        if element[:3] == "35=":
            curr = 'body'

        if element[:3] == "10=":
            curr = 'tail'

        if i not in data:
            data[i] = {'head': [], 'body': [], 'tail': []}

        data[i][curr].append(element)
    return data

def main():
    log_path = r".\data\fix_log1.txt"

    data = parseLog(log_path)
    
    with open(r".\data\log.json", "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()