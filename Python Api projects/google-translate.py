import requests

def translate_word():
    # Get user input for the word to translate
    word = input("Enter the word to translate: ")
    
    # Get user input for the target language
    print("Choose the target language:")
    print("1. Hindi")
    print("2. English")
    print("3. Spanish")
    print("4. Punjabi")
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Map the user choice to the language code
    language_codes = {'1': 'hi', '2': 'en', '3': 'es', '4': 'pa'}
    to_language = language_codes.get(choice)
    if not to_language:
        print("Invalid choice!")
        return
    
    url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

    payload = {
        "from": "auto",
        "to": to_language,
        "text": word
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "076439c01cmsh83529df627792f6p1742d3jsnfb2e4eed7953",
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        try:
            translated_word = response.json()['data']['translation']
            print(f"{word} -> {translated_word}")
        except KeyError:
            print("Translation not available.")
    else:
        print("Failed to translate. Please try again.")

if __name__ == "__main__":
    translate_word()
