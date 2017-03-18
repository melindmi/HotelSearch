class HotelAirportSearchRequest():

	def __init__(self, apikey, location, check_in, check_out):
		self.apikey = apikey
		self.location = location
		self.check_in = check_in
		self.check_out = check_out
		self.radius = None
		self.lang = None
		self.currency = None
		self.chain = None
		self.max_rate = None
		self.number_of_results = None
		self.all_rooms = None 
		self.show_sold_out = None
		self.amenity = None	
			
	
	def getRequestParameters(self):
		"""construct a dictionary with the request parameters
		"""
		res = {}
		res["apikey"] = self.apikey
		res["location"] = self.location
		res["check_in"] = self.check_in
		res["check_out"] = self.check_out
		if(self.radius != None):
			res["radius"] = self.radius
		if(self.lang != None):	
			res["lang"] = self.lang
		if(self.currency != None):
			res["currency"] = self.currency	
		if(self.chain !=None):
			res["chain"] = self.chain
		if(self.max_rate != None):
			res["max_rate"] = self.max_rate
		if(self.number_of_results != None):
			res["number_of_results"] = self.number_of_results
		if(self.all_rooms !=None):
			res["all_rooms"] = self.all_rooms
		if(self.show_sold_out != None):
			res["show_sold_out"] = self.show_sold_out
		if(self.amenity != None):
			res["amenity"] = self.amenity
			
		
		return res
		
	