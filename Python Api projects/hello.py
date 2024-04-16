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
    
    
    
    
    import requests
    
    url = "https://rnmguide.netlyfy.app/json/dummy.json"
    
    querystring = {"question_id" :"question" ,"answer_id" :"answer"}
    
    headers = {
        
        "json-API-key":
        "loeremwi3iewoiediwieoeie",
        "json-API-Host":
            "dfjskgksfgk.rnmguide.netlify.app"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    print(response.json)
    
    
    import requests
    
    url = ""
    
    querystring = { "id" :"name" , "email" : "password"}
    
    headers = {
        " Api key" :
            "uifdsi" , 
        "Api - Host" :
        
        
            "xyz.com"
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
