import requests
from PIL import Image
from io import BytesIO
UNSPLASH_ACCESS_KEY='-t_MrYB3fgtLStQQikmfYFqXr2sJTrTBO5bPikYu7Tw'
from pyunsplash import PyUnsplash

# Replace with your Google Places API key
api_key = "AIzaSyBOh6EEAz-XNubH9bfsbzfj6LjPw4wOwqk"

# Replace with the name of the place you want to search for
place_name = "Niagara Falls"

# Define the Google Places API endpoint for place search
places_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

# Define the parameters for the place search
params = {
    "input": place_name,
    "inputtype": "textquery",
    "fields": "photos,formatted_address",
    "key": api_key,
}

# Send a request to the Google Places API to find the place
response = requests.get(places_url, params=params)

if response.status_code == 200:
    data = response.json()

    if "candidates" in data and len(data["candidates"]) > 0:
        place = data["candidates"][0]
        place_address = place.get("formatted_address", "Address not found")
        
        if "photos" in place:
            photo_reference = place["photos"][0]["photo_reference"]
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photoreference={photo_reference}&key={api_key}"
            response = requests.get(photo_url)

            if response.status_code == 200:
                image_data = response.content
                img = Image.open(BytesIO(image_data))
                img.show()
            else:
                print("Failed to retrieve photo")
        else:
            print(f"No photos found for {place_name}")
    else:
        print(f"Place not found: {place_name}")
else:
    print("Failed to retrieve place information")
