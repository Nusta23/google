import requests

# Function to get coffee shop details
def get_coffee_shop_details(place_id, api_key):
    # Google Places API endpoint for Place Details
    endpoint = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={api_key}"
    
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        details = response.json()
        
        if details.get("status") == "OK":
            result = details.get("result", {})
            
            # Extracting necessary details
            name = result.get("name", "N/A")
            address = result.get("formatted_address", "N/A")
            neighborhood = result.get("vicinity", "N/A")
            rating = result.get("rating", "N/A")
            reviews = result.get("user_ratings_total", "N/A")
            price_level = result.get("price_level", "N/A")
            website = result.get("website", "N/A")
            maps_url = result.get("url", "N/A")
            opening_hours = result.get("opening_hours", {}).get("weekday_text", "N/A")
            
            # Formatting the output
            shop_info = f"""\
            Name: {name}
            Address: {address}
            Neighborhood: {neighborhood}
            Rating: {rating}
            Reviews: {reviews}
            Price Level: {price_level}
            Opening Hours: {", ".join(opening_hours) if opening_hours != "N/A" else "N/A"}
            Google Maps URL: {maps_url}
            Website: {website}
            """
            
            return shop_info
        else:
            return f"Error: {details.get('status')}"
    else:
        return f"Error: HTTP {response.status_code}"

# Replace 'your_api_key' with your actual Google API key and 'place_id' with the place ID
api_key = 'your_api_key'
place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'  # Replace with actual place ID

# Get the coffee shop details
details = get_coffee_shop_details(place_id, api_key)
print(details)
