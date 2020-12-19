import requests
f = requests.get('http://23.101.7.45:5005/').text
if f.index("SDSLabs") < f.index("Doxepticons"):
    print("true")
else:
    print("false")