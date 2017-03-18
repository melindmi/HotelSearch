import json

class ParseUserInput():
	
	def __init__(self, filename):	
		self.userinput=open(filename).read()
		self.jsonReq = json.loads(self.userinput)
	
	def getLocation(self):
		"""get the location enter by the user
		The location is a mandatory attribut for the query request
		"""
		if "location" not in self.jsonReq:
			raise KeyError("Missing the mandatory attribute 'location'")
	
		location = self.jsonReq["location"]
		
		return location
		
	def setOptionalRequestParameters(self, req):
		"""set the optional request parameters if they are present in the userinput file
		"""

		if(self.jsonReq["radius"] != None):
			setattr(req, "radius", self.jsonReq["radius"])
		if(self.jsonReq["lang"] != None):	
			setattr(req, "lang", self.jsonReq["lang"])
		if(self.jsonReq["currency"]!= None):
			setattr(req, "currency", self.jsonReq["currency"])	
		if(self.jsonReq["chain"]!=None):
			setattr(req, "chain", self.jsonReq["chain"])
		if(self.jsonReq["max_rate"] != None):
			setattr(req, "max_rate", self.jsonReq["max_rate"])
		if(self.jsonReq["number_of_results"] != None):
			setattr(req, "number_of_results", self.jsonReq["number_of_results"])
		if(self.jsonReq["all_rooms"] !=None):
			setattr(req, "all_rooms", self.jsonReq["all_rooms"])
		if(self.jsonReq["show_sold_out"] != None):
			setattr(req, "show_sold_out", self.jsonReq["show_sold_out"])
		if(self.jsonReq["amenity"] != None):
			setattr(req, "amenity", self.jsonReq["amenity"])	
	
		return req			