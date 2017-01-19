#Caoimhe Harvey

from skyscanner.skyscanner import Flights
flights_service = Flights('<Your API Key>')

# http://stackoverflow.com/questions/7047790/how-can-i-input-data-into-a-webpage-to-scrape-the-resulting-output-using-python

#QPX Express API Key
QAPI_key = 'AIzaSyC74E3Vu_dY0ZfxMIhQlXonC8yklxhVYqU'

#user_airports get's the airport list from the user of the
#airport codes they wish to visit and stores in an array
user_airports = []
#end_route stores the final key (airport) value (cost) pair
#with the best way to get from A to B
end_route = {}

#index for starting point
start_point = 2

#controls input
get_airports = False;

date_interval = input("Enter the average length of time you will spend at each destination: ")
start_date = input("Enter the start date of this journey: ")
while get_airports == False:
    airport = input("Input the Airport codes to where you'd like to go: ")
    
    if (airport == 'N'):
        get_airports = True;
    else:
        print("\nTo exit enter 'N'")
        user_airports.append(airport)
        
print (user_airports)

end = best_route(user_start, user_airports)
#output final route and cost
for key, value in end_route.items() :
    print (key, value)

#algorithm to find the best route
def best_route(index, array):
    temp = {}

    for i in array:
        #need to create getCost function taking Airport code as parameter
        #destCost = getCost(index, array[i])
        #search
        result = flights_service.get_result(
            currency='EUR',
            locale='en-GB',
            originplace= index + '-sky',
            destinationplace= array[i] + '-sky',
            outbounddate = start_date,
            adults=1).parsed

        print(result)
        temp.update({array[i]:result})

    #get minimum cost from temp dictionary here
    minAirport = min(temp, key = temp.get)
    
    #add minimum cost to end_route
    end_route.update({minAirport : temp[minAirport]})
    
    user_airports.remove(array[index])
    start_route = minAirport
    temp.clear()
        
    if (len(user_airports) != 0):
        best_route(start_route, user_airports)
