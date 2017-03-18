import configparser

class ParseConfig():
	
	def __init__(self, filename):
		self.config = configparser.ConfigParser()
		self.config.read(filename)
			
	
	def retrieveBaseUrl(self):
		"""retrive and return the base URL by parsing the config.ini file
		"""
	
		try:
			url = self.config["DEFAULT"]["url"] + self.config["DEFAULT"]["api"]
		except KeyError:
			raise KeyError("The url must be set in the DEFAULT section of config.ini")

		try:
			api = self.config["DEFAULT"]["api"]
		except KeyError:
			raise KeyError("The api must be set in the DEFAULT section of config.ini")	

		baseURL = url + api
	 
		return baseURL	


	def retrieveApiKey(self):
		"""retrieve and return the api key by parsing the config.ini file
		"""
	
		try:
			apikey = self.config["USER"]["apikey"]
		except KeyError:
			raise KeyError("Your personal api key must be set in the USER section of config.ini")
	
		return apikey