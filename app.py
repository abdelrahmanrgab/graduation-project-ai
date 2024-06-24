from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import generate_text , search_image

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

# Define a root path to verify the server is running
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Define a function to handle the POST request at `/generate-schema`
@app.post("/generate-schema", response_model=dict)
def generate_schema_route(user_text: str):
    """
    Generate a schema for a hero section of a website based on user input text.
    """
    if not user_text:
        raise HTTPException(status_code=400, detail="user_text is required")

    title = generate_text(f"Suggest a title for a website about {user_text}")
    description = generate_text(f"Create a brief description for a website about {user_text}")
    
    hero = {
        'title': title,
        'imgUrl': search_image(f"i need image which used as wallpaper for website about {user_text}"), 
        'buttonText': "Get Started",
        'icon': "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
        'description': description,
    }
    
    return hero

# Optional: Mount FastAPI app if not running with uvicorn
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='127.0.0.1', port=8000)
