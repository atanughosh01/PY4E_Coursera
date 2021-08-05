""" for testing XML parsing using ElementTree  """

import xml.etree.ElementTree as ET

data = '''<stuff>
    <users>
        <user x="1">
            <id>007</id>
            <name>Atanu</name>
        </user>
        <user x="7">
            <id>066</id>
            <name>John</name>
        </user>
        <user>
            <name>Rajib</name>
        </user>
    </users>
</stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall("users/user")
# print("\nUser List :", lst)
print("\nNumber of Users :", len(lst))
for item in lst:
    print("\nUser Number :", lst.index(item)+1)
    print("Name :", item.find("name").text)

    try:
        print("Id :", item.find("id").text)
    except:
        print("ID : None")

    print("Attribute :", item.get("x"))
