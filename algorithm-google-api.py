#@author Caoimhe Harvey
import google_flight_api

API_KEY = google_flight_api.GoogleFlight('AIzaSyCrvAbvDnoQa21SEJGJO9l3rA3JHTT1vag')
desiredAirports = []
cheapestRoute = {}

startDate = input("Enter the first date of travel: ")
dateInterval = input("How many days will you likely spend in each place? ")

getAirports = True

print("Below please input the airport codes you wish to visit, type \"DONE\" when finished: ")
while getAirports == True:
    airCode = input()
    if (airCode == "DONE"):
        getAirports = False
    else:
        desiredAirports.append(airCode)

print(desiredAirports)

for key, value in cheapestRoute.items():
    print(key, value)
