import requests

# Define the URL of the API endpoint you want to interact with
url = 'https://api.example.com/data'

# Make a GET request to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (usually in JSON format)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
