import json

# json.loads sirve para convertir el contenido de un json a python
# json.load también pero con archivos

# json.dumps sirve para convertir el contenido de un python a json
# json.dump también pero con archivos

data = json.loads('{"name": "Alice", "age": 30}')
# text = json.dumps(data, indent=2)
archivo = "prueba.json"
with open(archivo, "w") as file:
    # file.write(text)
    json.dump(data, file, indent=2)

# ------------- Hacen lo mismo ------------------------

# import json

# data = json.loads('{"name": "Alice", "age": 30}')
# text = json.dumps(data, indent=2)

# with open(archivo, "w") as file:
#     file.write(text)