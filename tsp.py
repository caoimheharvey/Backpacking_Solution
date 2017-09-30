#@author Caoimhe Harvey
#Python 2.7

from google_flight import google_flight_api
import datetime

def findBestRoute(array, start):
    g = google_flight_api.GoogleFlight('AIzaSyCoYPc7_vtNRlnCmGO8LB4DSQXblwLjhW4')

    temp = {}
    end = {}
    cheapest = array[0]
    for i in range(0,len(array)):
        if(cheapest != array[i]):
            data = {
                          "request": {
                            "slice": [
                              {
                                "origin": cheapest,
                                "destination": array[i],
                                "date": start
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
                            "refundable": 'false'
                          }
                        }
            g.get(data)
            lowestCost = g.getCost()
            print (lowestCost)
            temp.update({array[i]: str(lowestCost)})
            print(temp)
                    
    cheapest = min(temp, key = temp.get)
    print (cheapest)
    cheapestRoute.update({cheapest : temp[cheapest]})
    temp.clear()
    
desiredAirports = []
cheapestRoute = {}

print "Enter the first date of travel"
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
startDate = datetime.date(year, month, day)
print startDate
#startDate = datetime.date(year, month, day)
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

findBestRoute(desiredAirports,str(startDate))
    
for key, value in cheapestRoute.items():
    print key, value



