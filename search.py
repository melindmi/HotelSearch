import requests
from requests import Request

class Search:

	def __init__(self, baseUrl):
		self.baseUrl = baseUrl
		
	def getRequestURL(self, parameters):
		"""return the complete URL
		"""
		reqUrl = Request(url=self.baseUrl, params=parameters).prepare().url
		return reqUrl
		
	
	def getResponse(self, parameters):
		"""return the response of the GET request
		"""
		rsp = requests.get(url=self.baseUrl, params=parameters)
		return rsp
		
	def getJsonResponse(self, parmeters):
		"""return the JSON response of the GET request
		"""
		rsp = self.getResponse()
		return rsp.json()
		
		