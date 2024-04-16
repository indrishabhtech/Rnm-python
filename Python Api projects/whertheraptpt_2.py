import requests

def get_weather(location):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
    querystring = {"city": location}  # Specify the city instead of lat and lon
    headers = {
        "X-RapidAPI-Key": "076439c01cmsh83529df627792f6p1742d3jsnfb2e4eed7953",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        # Extract specific details you're interested in from the response
        filtered_data = {
            "timezone": data["timezone"],
            "city_name": data["city_name"],
            "current_weather": data["data"][0]  # Example: Get only the details for the current time
        }
        return filtered_data
    else:
        return "Error fetching weather data"

# Ask the user to input the city location
location = input("Enter city location: ")

# Call the function with the user-provided location
weather_info = get_weather(location)
print(weather_info)
