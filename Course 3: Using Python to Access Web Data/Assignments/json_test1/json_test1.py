""" for testing json parsing using json package """

import json

data = """ {
    "name" : "Atanu",
    "phone" : {
        "type" : "intl",
        "number" : "+91-(99887)-76655"
    },
    "email" : {
        "isGmail" : true,
        "hide" : "yes"
    },
     "address" : {
        "country" : "India",
        "location" : {
            "city" : "Kol",
            "pin" : "700 032"
        }
    }
} """

info = json.loads(data)
print("\nINFO :", info)
print("\nType of INFO :", type(info))
print("\nName :", info["name"])
print("Email Hidden? :", info["email"]["hide"])
print("Email is Gmail? :", info["email"]["isGmail"])
print("PIN :", info["address"]["location"]["pin"])

print("\n----------------------------------------------\n")

msg = """[
    {
        "id" : "007",
        "x" : "01",
        "name" : "Atanu"
    },
    {
        "id" : "066",
        "x" : "22",
        "name" : "Atanu"
    }
]"""

msg_info = json.loads(msg)
print(f"Message Info : {msg_info}")
print(f"Message Info[0] : {msg_info[0]}\nMessage Info[1] : {msg_info[1]}")
print("User Count :", len(msg_info))
for content in msg_info:
    print("Name :", content["name"])
    print("ID :", content["id"])
    print("Attr :", content["x"])
