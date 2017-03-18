import json
from json2html import *

class HotelAirportSearchResponse:
	
	def __init__(self, jsonrsp):
		self.jsonrsp = jsonrsp
		
	def printFullResponse(self):
		print(self.jsonrsp)
	
	def getHotelMinDetails(self):
		""" return a dictionary including information extracted from the full response
			this information is considered to be the minimum a user would want to know at this point
			about each hotel retrieved
			- property name (the hotel name)
			- hotel coordinates: longitude and latitude
			- hotel address
			- city
			- daily rate amount and currency
			- contact information: the phone number	
		"""
		listrsp=[]
		if "results" in self.jsonrsp:
			for r in self.jsonrsp["results"]:
				rspdic={}
				rspdic["property_name"] = r["property_name"]
				rspdic["latitude"] = r["location"]["latitude"]
				rspdic["longitude"] = r["location"]["longitude"]
				rspdic["address"] = r["address"]["line1"]
				rspdic["city"] = r["address"]["city"]
				rspdic["daily_rate"] = {}
				rspdic["daily_rate"]["amount"] = r["min_daily_rate"] ["amount"]
				rspdic["daily_rate"]["currency"] = r["min_daily_rate"]["currency"]
				for c in r["contacts"]:
					if(c["type"] == "PHONE"):
						rspdic["phone"] = c["detail"]
				listrsp.append(rspdic)
		elif "message" in jsonrsp:
			rspdic={}
			rspdic["message"] = jsonrsp["message"]
			listrsp.append(rspdic)
			
		res={}	
		res["hotels"] = listrsp
		
		return res
		
	def writeMinDetailsResponseOnFile(self, filename):
		f = open(filename, "w")
		rsp = json.dumps(self.getHotelMinDetails(), indent = 4) 
		f.write(rsp)
		f.close()
	
	def writeResponseOnFile(self, filename):
		f = open(filename, "w")
		rsp = json.dumps(self.jsonrsp, indent = 4)
		f.write(rsp)
		f.close()
		
	def generateHtmlFromJsonResponse(self, filename):
		f =open(filename, "w")
		res = self.getHotelMinDetails()
		jsonRsp = json.dumps(res, indent=4)
		html = json2html.convert(json = jsonRsp)
		f.write(html)
		f.close()