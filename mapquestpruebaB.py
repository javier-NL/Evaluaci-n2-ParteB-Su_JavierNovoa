import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "rXeHR6sM3pd5Q243aNO7gGM1ejZqsuua"

while True:
   comienzo = input("Ubicacion Inicial: ")
   if comienzo == "salir" or comienzo == "s":
       break
   termino = input("Ubicacion de destino: ")
   if termino == "salir" or termino == "s":
        break

   url = main_api + urllib.parse.urlencode({"key" :key, "from" :comienzo, "to" :termino})
   print("URL: " + (url))
   
   json_data = requests.get(url).json()
   json_status = json_data ["info"] ["statuscode"]
   
   if json_status == 0:
       print("Estado de la API: " + str(json_status) + "= Una llamada de ruta exitosa.\n")
       print("=============================================")
       print("Como llegar desde " + (comienzo) + " a " + (termino))
       print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
       print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
       print("=============================================")
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
           print("=============================================\n")       
   elif json_status == 402:
        print("**********************************************")
        print("Codigo de estado: " + str(json_status) + "; Entradas de usuario no validas para una o ambas ubicaciones.")
        print("**********************************************\n")
   elif json_status == 611:
        print("**********************************************")
        print("Codigo de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
   else:
        print("************************************************************************")
        print("Codigo de estado: " + str(json_status) + "; Referia a:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
         

       
  



