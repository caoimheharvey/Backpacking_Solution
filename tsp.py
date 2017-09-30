#@author Caoimhe Harvey
#Python 2.7

from google_flight import google_flight_api
import datetime

API = google_flight_api.GoogleFlight('')
desiredAirports = []
cheapestRoute = {}

startDate = input("Enter the first date of travel (YYYY-MM-DD): ")
dateInterval = input("How many days will you likely spend in each place? ")

getAirports = True

print "Below please input the airport codes you wish to visit, type \"DONE\" when finished: "
while getAirports == True:
    airCode = raw_input()
    if (airCode == "DONE"):
        getAirports = False
    else:
        desiredAirports.append(airCode)
print(desiredAirports)


for key, value in cheapestRoute.items():
    print key, value


def findBestRoute(index, array):
    temp = {}

    for i in array:
        #try if array + 1 is out of bounds then break loop
        json_request = {
                    {
                  "request": {
                    "slice": [
                      {
                        "origin": array[i],
                        "destination": array[i+1],
                        "date": startDate
                      }
                    ],
                    "passengers": {
                      "adultCount": 1,
                      "infantInLapCount": 0,
                      "infantInSeatCount": 0,
                      "childCount": 0,
                      "seniorCount": 0
                    },
                    "solutions": 1,
                    "refundable": false
                  }
                }
        API.get(json_request)
        lowestCost = API.getCost()
        temp.update({array[1]: str(lowestCost)})
