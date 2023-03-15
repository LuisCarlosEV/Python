import requests, pprint

#EndPoint del microservicio
url = "http://api.open-notify.org/iss-now.json"

#Utilizamos la funcion get() para realizar una llamada GET
#La funcion get() retorna una respuesta

response = requests.get(url)


#Mostrar el codigo de estado HTTP
#Mostrar el codigo de estado HTTP en modo texto utilzando REASON
print(f"Codigo de Estado: ", response.status_code)
print(f"Estado:", response.reason)