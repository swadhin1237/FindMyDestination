import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/getNearByAirports"

querystring = {"lat":"19.242218017578125","lng":"72.85846156046128"}

headers = {
	"X-RapidAPI-Key": "dfac622ff3msh5650dd6f3de63e6p1185eejsna79c050b7dc7",
	"X-RapidAPI-Host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()['data']['current']['skyId'])