from gradio_client import Client
import json
import requests
import time

client = Client("alanchen1115/gemini_api")

def generate_text(prompt):
    def check(prompt, attempt=1):
        try:
            result = client.predict(prompt=prompt, api_name="/predict")
            # Check if the result indicates quota exhaustion
            if result == "429 Resource has been exhausted (e.g. check quota).":
                if attempt <= 3:  # Reduce the number of retries to 3
                    wait_time = 5  # Use a fixed backoff time (5 seconds)
                    print(f"Rate limited. Retrying attempt {attempt} in {wait_time} seconds...")
                    time.sleep(wait_time)
                    return check(prompt, attempt + 1)
                elif attempt <= 5:
                    wait_time = 60  # After 3 attempts, wait for a longer period (1 minute)
                    print(f"Extended wait due to persistent rate limiting. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    return check(prompt, attempt + 1)
                else:
                    print("Maximum retry attempts reached. Quota exhausted.")
                    return None
            else:
                return result

        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            return None

    return check(prompt)

def search_image(image_name):
    api_key = 'AIzaSyCUiG8Cm9TdIKasE4Ruasd0ZmLPgjSZ-nY'
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





# import http.client
# import json
# import requests

# def generate_text(prompt):
#     conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

#     payload = {
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "system_prompt": "",
#         "temperature": 0.7,
#         "top_k": 5,
#         "top_p": 0.9,
#         "max_tokens": 50,
#         "web_access": False
#     }

#     headers = {
#         'x-rapidapi-key': "ac6e9260b6mshd8d7dfb0752163cp1033e8jsnae6eea61d73d",
#         'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
#         'Content-Type': "application/json"
#     }

#     try:
#         json_payload = json.dumps(payload)
#         conn.request("POST", "/conversationgpt4-2", json_payload, headers)
#         res = conn.getresponse()
#         data = res.read()

#         if res.status == 200:
#             response_data = json.loads(data.decode("utf-8"))

#             return response_data["result"]
#         else:
#             print(f"Error: {res.status}, {res.reason}")
#             print(f"Response: {data.decode('utf-8')}")
#             return None

#     except Exception as e:
#         print(f"Exception occurred: {str(e)}")
#         return None
#     finally:
#         conn.close()

# def search_image(image_name):
#     api_key = 'AIzaSyDAqHqVO9fRiESqLeQjslNh53ZiV36rgqI'
#     cx = '7266ebe81ea1a4367'

#     try:
#         def get_google_custom_search_url():
#             base_url = 'https://www.googleapis.com/customsearch/v1'
#             params = {
#                 'key': api_key,
#                 'cx': cx,
#                 'q': image_name,
#                 'searchType': 'image',
#                 'num': 1
#             }
#             return f'{base_url}?{requests.compat.urlencode(params)}'

#         url = get_google_custom_search_url()
#         response = requests.get(url)

#         if response.ok:
#             data = response.json()
#             items = data.get('items', [])
#             if items:
#                 return items[0]['link']
#             else:
#                 return None
#         else:
#             print(f"Error: {response.status_code}, {response.reason}")
#             print(f"Response: {response.text}")
#             return None

#     except Exception as e:
#         print(f"Exception occurred: {str(e)}")
#         return None


# # Example usage:
# if __name__ == "__main__":
#     prompt = "Write a short story about an astronaut exploring a new planet."
#     generated_text = generate_text(prompt)
#     if generated_text:
#         print("Generated Text:")
#         print(generated_text)
#     else:
#         print("Failed to generate text.")

#     image_name = "Get in shape and boost your energy levels with our personalized fitness programs and state-of-the-art equipment. Start your fitness journey today!"
#     image_url = search_image(image_name)
#     if image_url:
#         print("Image URL:")
#         print(image_url)
#     else:
#         print("Failed to retrieve image URL.")



