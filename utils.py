import http.client
import json

RAPIDAPI_KEY = "a5ca887219mshc7b3b054861e14ap1df056jsn7477c1004441"
RAPIDAPI_HOST = "chatgpt-42.p.rapidapi.com"

def generate_text(prompt):
    # Establish connection to the RapidAPI endpoint
    conn = http.client.HTTPSConnection(RAPIDAPI_HOST)
    
    # Prepare the payload with the provided prompt
    payload = json.dumps({
        "messages": [{"role": "user", "content": prompt}],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    })
    
    # Define headers including API key and content type
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST,
        'Content-Type': "application/json"
    }
    
    try:
        # Make the POST request to the ChatGPT API
        conn.request("POST", "/conversationgpt4-2", payload, headers)
        
        # Get the response from the API
        res = conn.getresponse()
        
        # Read the response data
        data = res.read()
        
        if res.status == 200:
            # Parse the JSON response
            result = json.loads(data.decode("utf-8"))
            
            # Extract and return the generated text
            return result.get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            # Handle API errors or unexpected responses
            print(f"Error: Unexpected response {res.status}, {data.decode('utf-8')}")
            return None
        
    except Exception as e:
        # Handle exceptions raised during HTTP request
        print(f"Error: {str(e)}")
        return None
    finally:
        # Close the connection
        conn.close()

# Example usage:
if __name__ == "__main__":
    prompt = "Write a short story about an astronaut exploring a new planet."
    generated_text = generate_text(prompt)
    if generated_text:
        print("Generated Text:")
        print(generated_text)
    else:
        print("Failed to generate text.")
