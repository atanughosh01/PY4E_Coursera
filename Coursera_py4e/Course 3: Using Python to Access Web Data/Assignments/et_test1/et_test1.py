""" for testing XML parsing using ElementTree """

import xml.etree.ElementTree as ET

data = '''<person>
<name>Atanu Ghosh</name>
<phone type="intl">+91-89272 08591</phone>
<email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print("\nName :", tree.find("name").text)
print("Phone :", tree.find("phone").text, ", Type :", tree.find("phone").get("type"))
print("Email :",tree.find("email").text, ", Attr :", tree.find("email").get("hide"))
