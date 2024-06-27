from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from utils import generate_text, search_image

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

# Define a Pydantic model for the request body
class UserText(BaseModel):
    user_text: str

# Define a function to handle the POST request at `/generate-schema`
@app.post("/generate-schema", response_model=dict)
def generate_schema_route(input: UserText):
    """
    Generate a schema for a hero section of a website based on user input text.
    """
    user_text = input.user_text
    if not user_text:
        raise HTTPException(status_code=400, detail="user_text is required")

    # Generate text for different sections of the website
    title = generate_text(f"Suggest a name for a website about {user_text}")
    description = generate_text(f"Create a brief description for a website about {user_text}")

    # Define the schema for the website
    schema = {
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "links": [
                {"title": "home", "url": "#"},
                {"title": "pages", "url": "#"},
                {"title": "services", "url": "#"},
                {"title": "projects", "url": "#"},
                {"title": "blog", "url": "#"},
                {"title": "contact", "url": "#"},
            ],
        },
        "hero": {
            "title": title,
            "description": description,
            "buttonText": "Get Started",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"I need an image to be used as wallpaper for a website about {user_text}"),
        },
        "services": {
            "services": [
                {
                    "title": generate_text(f"Suggest a title for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_one_xvd7d6.svg",
                }
            ],
        },
        "features": {
            "title": generate_text(f"Suggest a title for a feature related to {user_text}"),
            "description": generate_text(f"Create a brief description for a feature related to {user_text}"),
            "phone": "012345678",
            "buttonText": "Get Free Estimate",
            "icons": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813236/templates/template_one/Call_gqvv4l.svg",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            ],
            "imgUrl": search_image(f"I need an image to describe {user_text} as a feature"),
        },
        "testimonials": {
            "title": "What the People Thinks About Us",
            "testimonials": [
                {
                    "name": "Nattasha Mith",
                    "location": "Sydney, USA",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate a brief description for a client who used our services about {user_text}"),
                }
            ],
        },
        "logos": {
            "companies": [
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/01_p78hjd.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/02_mnw1ps.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/03_fiplpx.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/04_pg8flc.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/05_prt3gi.svg", "url": "https://x.com"},
            ],
        },
        "projects": {
            "title": "Follow Our Projects",
            "description": "It is a long established fact that a reader will be distracted by readable content when looking at its layout points.",
            "projects": [
                {
                    "title": generate_text(f"Suggest a title for a section about projects related to {user_text}"),
                    "description": generate_text(f"Write a brief description for the projects section of a {user_text} website"),
                    "imgUrl": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                }
            ],
        },
        "statistics": {
            "statistics": [
                {"title": "Years Of Experience", "value": "12"},
                {"title": "Success Projects", "value": "85"},
                {"title": "Active Projects", "value": "15"},
                {"title": "Happy Customers", "value": "95"},
            ],
        },
        "items": {
            "title": "Articles & News",
            "description": "It is a long established fact that a reader will be distracted by readable content when looking at its layout points.",
            "items": [
                {
                    "title": "Let’s Get Solution For Building Construction Work",
                    "subtitle": "Kitchen Design",
                    "description": "26 December,2022 ",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718041/templates/template_one/article1.f88f54e6a4cdbf340b36_l3ujjw.png",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                },
                {
                    "title": "Low Cost Latest Invented Interior Designing Ideas.",
                    "subtitle": "Living Design",
                    "description": "22 December,2022 ",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article2.43be768543cb8cfeaf07_atvwjd.png",
                },
                {
                    "title": "Best For Any Office & Business Interior Solution",
                    "subtitle": "Interior Design",
                    "description": "25 December,2022 ",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article3.f759fde0c85f3fb92b22_c2tqkv.png",
                },
            ],
        },
        "team": {
            "title": "Our Team Members",
            "members": [
                {
                    "id": "1",
                    "name": "Nattasha",
                    "email": "nattasha@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811338/templates/template_one/person_one_hkiznb.png",
                },
                {
                    "id": "2",
                    "name": "John Doe",
                    "email": "johndoe@email.com",
                    "location": "Marketing, USA",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811338/templates/template_one/person_two_ub3fcq.png",
                },
                {
                    "id": "3",
                    "name": "Hana",
                    "email": "hana@email.com",
                    "location": "Design, UK",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811338/templates/template_one/person_three_s7axuh.png",
                },
                {
                    "id": "4",
                    "name": "Nattasha",
                    "email": "nattasha@email.com",
                    "location": "CEO, Canada",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811338/templates/template_one/person_four_ykpibk.png",
                },
            ],
        },
        "contact": {
            "title": "Get In Touch",
            "description": "Contact us via email or phone, or visit us in person at our office.",
            "phone": "123-456-7890",
            "email": "info@example.com",
            "address": "123 Street, City, Country",
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701812099/templates/template_one/contact_x1kuxk.png",
        },
    }

    return schema

# Start the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


