import http.client
import json
import requests

def generate_text(prompt):
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    }

    headers = {
        'x-rapidapi-key': "67ef3ec93emsh2fb26541af41f49p1869e9jsn620aac640986",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    try:
        json_payload = json.dumps(payload)
        conn.request("POST", "/conversationgpt4-2", json_payload, headers)
        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            response_data = data.decode("utf-8")
            return response_data
        else:
            print(f"Error: {res.status}, {res.reason}")
            print(f"Response: {data.decode('utf-8')}")
            return None

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None
    finally:
        conn.close()

def search_image(image_name):
    api_key = 'AIzaSyDAqHqVO9fRiESqLeQjslNh53ZiV36rgqI'
    cx = '7266ebe81ea1a4367'

    try:
        def get_google_custom_search_url():
            base_url = 'https://www.googleapis.com/customsearch/v1'
            params = {
                'key': api_key,
                'cx': cx,
                'q': image_name,
                'searchType': 'image',
                'num': 1
            }
            return f'{base_url}?{requests.compat.urlencode(params)}'

        url = get_google_custom_search_url()
        response = requests.get(url)

        if response.ok:
            data = response.json()
            items = data.get('items', [])
            if items:
                return items[0]['link']
            else:
                return None
        else:
            print(f"Error: {response.status_code}, {response.reason}")
            print(f"Response: {response.text}")
            return None

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None

# Example usage:
if __name__ == "__main__":
    prompt = "Write a short story about an astronaut exploring a new planet."
    generated_text = generate_text(prompt)
    if generated_text:
        print("Generated Text:")
        print(generated_text)
    else:
        print("Failed to generate text.")

    image_name = "astronaut on new planet"
    image_url = search_image(image_name)
    if image_url:
        print("Image URL:")
        print(image_url)
    else:
        print("Failed to retrieve image URL.")
