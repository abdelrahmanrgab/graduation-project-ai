from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from pydantic import BaseModel
# from utils import generate_text, search_image
from schemas.schema1 import schema_1
from schemas.schema2 import schema_2
from schemas.schema3 import schema_3
from schemas.schema4 import schema_4
from schemas.schema5 import schema_5
from schemas.schema6 import schema_6


app = FastAPI()

class UserInput(BaseModel):
    user_text: str
    TemplateId: int

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


def select_schema(template_id, user_text):
    schema_functions = {
        1: schema_1,
        2: schema_2,
        3:schema_3,
        4:schema_4,
        5:schema_5,
        6:schema_6
         
    }
    
    schema_function = schema_functions.get(template_id)
    if not schema_function:
        raise HTTPException(status_code=404, detail="Template ID not found")
    
    return schema_function(user_text)
@app.post("/generate-schema")
def generate_schema(user_input: UserInput):
    user_text = user_input.user_text
    template_id = user_input.TemplateId

    selected_schema = select_schema(template_id, user_text)
    return selected_schema

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

