import xmltodict


def print_xml(xml):

    print(xml)
    for student in xml["data"]["student"]:
        if student["@name"] == "Sinha":
            print(student)
            student["id"] = 400
            print(student)
    print(xml)

    with open("test.xml", "w") as file:
        file.write(xmltodict.unparse(xml))

if __name__ == '__main__':
    file = open("test.xml", "r+")
    xml_string = file.read()
    dict = xmltodict.parse(xml_string)
    print_xml(dict)
    file.close()
