import google_flight_api as gf
import datetime

start_date = datetime.datetime.now()
end_date = datetime.datetime.now()
start_date += datetime.timedelta(days=2)
end_date += datetime.timedelta(days=7)

g = gf.GoogleFlight('AIzaSyCrvAbvDnoQa21SEJGJO9l3rA3JHTT1vag')
data = {
          "request": {
            "slice": [
                {
                  "origin": "PVD",
                  "destination": "MCO",
                  "date": start_date.strftime("%Y-%m-%d")  #"2017-08-04"
                },
                {
                  "origin": "MCO",
                  "destination": "PVD",
                  "date": end_date.strftime("%Y-%m-%d") #"2017-08-24"
                }
            ],
            "passengers": {
              "adultCount": 1,
              "infantInLapCount": 0,
              "infantInSeatCount": 0,
              "childCount": 0,
              "seniorCount": 0
            },
            "solutions": 20,
            "refundable": 'false'
          }
        }
g.get(data)
