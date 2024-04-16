import requests

def get_love_percentage(first_name, second_name):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    querystring = {"sname": first_name, "fname": second_name}
    headers = {
        "X-RapidAPI-Key": "076439c01cmsh83529df627792f6p1742d3jsnfb2e4eed7953",
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data['result']  # Only return the result message
    else:
        return "Error fetching love percentage"

if __name__ == "__main__":
    # Get names from user input
    first_name = input("Enter your name: ")
    second_name = input("Enter your partner's name: ")
    
    # Call the function with the provided names
    result = get_love_percentage(first_name, second_name)
    print(result)
