import requests

url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

payload = {
	"from": "auto",
	"to": "en",
	"text": "xin chào"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "076439c01cmsh83529df627792f6p1742d3jsnfb2e4eed7953",
	"X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())