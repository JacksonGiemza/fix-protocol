import xml.etree.ElementTree as ET
import json

def fieldsToDict(root):
    fields = {}
    for field in root.findall('Field'):
        tag_id = field.find('Tag').text

        tag_data = {
        }
        for elem in field.iter():
            if elem.tag == 'Tag' or elem.tag == 'Field':
                continue
            tag_data[elem.tag] = elem.text
        fields[tag_id] = tag_data

    return fields

def enumsToDict(root):
    enums = {}
    for enum in root.findall('Enum'):
        key = enum.find('Tag').text

        if key not in enums:
            enums[key] = {enum.find('Value').text: enum.find('SymbolicName').text}
        else:
            enums[key][enum.find('Value').text] = enum.find('SymbolicName').text
    return enums


def main():
    fields_path = r".\data\fix_repository\FIX.4.4\Base\Fields.xml"
    enums_path = r".\data\fix_repository\FIX.4.4\Base\Enums.xml"
    fields = ET.parse(fields_path)
    enums = ET.parse(enums_path)

    fields_data = fieldsToDict(fields)
    enums_data = enumsToDict(enums)

    with open(r".\data\fix_fields.json", "w") as file:
        json.dump(fields_data, file)

    with open(r".\data\fix_enums.json", "w") as file:
        json.dump(enums_data, file)

if __name__ == "__main__":
    main()

