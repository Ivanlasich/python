import json

json_string = '{"favorited": false, "contributors": null}'
'{"favorited": false, "contributors": null}'
value = json.loads(json_string)
print(value)
json_dump = json.dumps(value)
print(json_dump)