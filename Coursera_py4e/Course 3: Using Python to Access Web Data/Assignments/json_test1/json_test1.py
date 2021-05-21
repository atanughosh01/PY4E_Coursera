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
print("Type of INFO :", type(info))
print("Name :", info["name"])
print("Email Hidden? :", info["email"]["hide"])
print("Email is Gmail? :", info["email"]["isGmail"])
print("PIN :", info["address"]["location"]["pin"])
