import json

SOH = "\x01"

def parseLog(path):
    with open(path, "r", encoding="utf-8") as file:
        raw_text = file.read()

    raw_messages = raw_text.split()
    elements = raw_text.split(SOH)

    messages = {}
    message_index = -1
    section = None

    for element in elements:
        element = element.strip()

        if not element:
            continue

        if element.startswith("8="):
            message_index += 1
            section = "head"

        elif element.startswith("35="):
            section = "body"

        elif element.startswith("10="):
            section = "tail"

        if message_index not in messages:
            messages[message_index] = {
                "head": [],
                "body": [],
                "tail": [],
                "raw": raw_messages[message_index]
            }

        messages[message_index][section].append(element)

        if section == "tail":
            val_data = validateMessage(messages[message_index])
            messages[message_index]["validation"] = val_data
            break

    return messages

def validateMessage(message):
    head = message['head']
    body = message['body']
    tail = message['tail']

    SOH = "\x01"
    listed_body_length = int(head[1].split('=')[1])
    body_length = len((SOH.join(body) + SOH).encode("ascii"))

    listed_check_sum = int(tail[0].split('=')[1])
    check_sum = sum(("".join(head) + SOH.join(body) + SOH).replace(r"\x01", "\x01").encode("ascii")) % 256

    return {
        'body_length': {'actual': body_length,
                        'listed': listed_body_length,
                        'valid': body_length == listed_body_length},
        'check_sum': {'actual': check_sum,
                      'listed': listed_check_sum,
                      'valid': check_sum == listed_check_sum},
    }


def main():
    log_path = r".\data\fix_log1.txt"

    print(parseLog(log_path))
    
    # with open(r".\data\log.json", "w") as file:
    #     json.dump(data, file)

if __name__ == "__main__":
    main()