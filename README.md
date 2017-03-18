[DESCRIPTION]

This is a simple application that uses the sandbox.amadeus.com Hotel API to find a small selection of hotels near airport X for the traveller to select from.

[USER GUIDE]

The application was writer in Python 3 (Python 3.6.0)

Not build in modules used by the application: requests, json2html

Modules installation tips:

	1. for Linux: pip install requests
	2. for Windows: ...Python\Python36-32\Scripts> easy_install.exe requests
(same for json2html module)

Run:

python main.py

Input:

1. In the config.ini file add your personal API key in the [USER] section
2. The userinput.json file include the parameters of the request queries. For more details about those parameters check:
https://sandbox.amadeus.com/travel-innovation-sandbox/apis/get/hotels/search-airport#sm-example-block

The check_in and check_out date cannot be give by the user. The check_in date is consider to be today date and the chekc_out date is tomorrow date.

Output:

The application will generate 3 files:
1. hotel_full_details.json => including the full response in a json format
2. hotel_min_details.json => including , for each hotel retrieved, only a minimum amount of information 
3. hotel_min_details.html => a html page that displays the minimum amount of information for each hotel retrieved, in a tabular form

 
