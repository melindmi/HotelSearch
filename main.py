from hotelairportsearch_request import HotelAirportSearchRequest
from hotelairportsearch_response import HotelAirportSearchResponse
from search import Search
from parseconfig import ParseConfig
from parseuserinput import ParseUserInput

from datetime import date, timedelta

#parse the configuration file 
config = ParseConfig("config.ini")
baseURL = config.retrieveBaseUrl()
apikey  = config.retrieveApiKey()

#parse the user input file
userinput = ParseUserInput("userinput.json")
location = userinput.getLocation()

#check_in and chek_out date
check_in = date.today()
check_out = check_in + timedelta(1)	
	
#create the request
userRequest = HotelAirportSearchRequest(apikey, location, check_in, check_out)
userRequest = userinput.setOptionalRequestParameters(userRequest)

#call search with the request and the base url
src = Search(baseURL)
print(src.getRequestURL(userRequest.getRequestParameters()))

#parse the response
rsp = HotelAirportSearchResponse(src.getJsonResponse(userRequest.getRequestParameters()))
rsp.writeResponseOnFile("hotels_full_details.json")
rsp.writeMinDetailsResponseOnFile("hotels_min_details.json")
rsp.generateHtmlFromJsonResponse("hotels_min_details.html")
