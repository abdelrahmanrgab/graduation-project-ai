from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserText(BaseModel):
    user_text: str

@app.post("/generate-schema/{schema_id}", response_model=dict)
def generate_schema_route(schema_id: int, input: UserText):
    """
    Generate a schema based on the schema ID and user input text.
    """
    user_text = input.user_text
    if not user_text:
        raise HTTPException(status_code=400, detail="user_text is required")

    if schema_id not in schemas:
        raise HTTPException(status_code=404, detail="Schema ID not found")

    schema = schemas[str(schema_id)]

    # Dynamically generate text and images for the schema
    schema["hero"]["title"] = generate_text(f"Suggest a name for a website about {user_text}")
    schema["hero"]["description"] = generate_text(f"Create a brief description for a website about {user_text}")
    schema["hero"]["imgUrl"] = search_image(f"Image for website about {user_text}")

    # Populate other fields as required

    return schema

# Start the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
