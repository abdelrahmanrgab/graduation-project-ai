from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import generate_text

# Create a new FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Pydantic model for request body
class GenerateSchemaRequest(BaseModel):
    user_text: str

# Pydantic model for response body
class HeroSchema(BaseModel):
    title: str
    imgUrl: str
    buttonText: str = "Get Started"
    icon: str
    description: str

# Define a root path to verify the server is running
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Define a function to handle the POST request at `/generate-schema`
@app.post("/generate-schema", response_model=HeroSchema)
def generate_schema_route(req_body: GenerateSchemaRequest):
    """
    Generate a schema for a hero section of a website based on user input text.
    """
    user_text = req_body.user_text
    title = generate_text(f"Suggest a title for a website about {user_text}")
    description = generate_text(f"Create a brief description for a website about {user_text}")
    
    hero = {
        'title': title,
        'imgUrl': "imgUrl",  # Replace with actual image URL logic
        'buttonText': "Get Started",
        'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
        'description': description,
    }
    
    return HeroSchema(**hero)

# Optional: Mount FastAPI app if not running with uvicorn
#    if __name__ == '__main__':
 #    import uvicorn
  #   uvicorn.run(app, host='127.0.0.1', port=8000)
