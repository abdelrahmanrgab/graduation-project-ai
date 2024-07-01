from utils import generate_text, search_image

def schema_3(user_text):
    return {
        "templateInfo": {
            "id": 3,
            "title": generate_text(f"Generate a title related to {user_text}"),
            "description": generate_text(f"Generate a description related to {user_text}"),
            "imgUrl": search_image(f"Generate an image related to {user_text}")
        },
        "navbar": {
            "logos": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1705928879/jammal_photos/vqliep1jh8zlgkmwkewx.png",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1705931744/jammal_photos/fbb4rdapofxl04oewfc3.png"
            ],
            "links": ["Home", "Programs", "Why us", "Plans", "Testimonials"]
        },
        "hero": {
            "Subtitle": generate_text(f"Generate a subtitle related to {user_text}"),
            "imgUrl": search_image(f"Generate an image related to {user_text}"),
            "title": generate_text(f"Generate a title related to {user_text}"),
            "description": generate_text(f"Generate a description related to {user_text}"),
            "statistics": [
                {
                    "count": "+140",
                    "description": generate_text(f"Generate a description related to {user_text}")
                },
                {
                    "count": "+978",
                    "description": generate_text(f"Generate a description related to {user_text}")
                },
                {
                    "count": "+50",
                    "description": generate_text(f"Generate a description related to {user_text}")
                }
            ],
            "Button": {
                "primaryButton": generate_text(f"Generate a button text related to {user_text}"),
                "secondaryButton": generate_text(f"Generate a button text related to {user_text}"),
                "actionButton": generate_text(f"Generate a button text related to {user_text}")
            }
        },
        "projects": {
            "title": [
                { "Subtitle": generate_text(f"Generate a subtitle related to {user_text}") },
                { "Subtitle": generate_text(f"Generate a subtitle related to {user_text}") },
                { "Subtitle": generate_text(f"Generate a subtitle related to {user_text}") }
            ],
            "actionButton": generate_text(f"Generate a button text related to {user_text}"),
            "imgUrl": search_image(f"Generate an image related to {user_text}"),
            "descriptions": [
                {
                    "heading": generate_text(f"Generate a heading related to {user_text}"),
                    "details": generate_text(f"Generate details related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate a heading related to {user_text}"),
                    "details": generate_text(f"Generate details related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate a heading related to {user_text}"),
                    "details": generate_text(f"Generate details related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate a heading related to {user_text}"),
                    "details": generate_text(f"Generate details related to {user_text}")
                }
            ]
        },
        "features": {
            "Subtitle": generate_text(f"Generate a subtitle related to {user_text}"),
            "title": generate_text(f"Generate a title related to {user_text}"),
            "imgUrl": [search_image(f"Generate an image related to {user_text}") for _ in range(8)],
            "statistics": [
                {"description": generate_text(f"Generate a description related to {user_text}")} for _ in range(5)
            ]
        },
        "pricing": {
            "title": [
                { "Subtitle": generate_text(f"Generate a subtitle related to {user_text}") } for _ in range(3)
            ],
            "description": generate_text(f"Generate a description related to {user_text}"),
            "actionButton": generate_text(f"Generate a button text related to {user_text}"),
            "imgUrl": search_image(f"Generate an image related to {user_text}"),
            "plans": [
                {
                    "name": generate_text(f"Generate a name related to {user_text}"),
                    "price": price,
                    "features": [generate_text(f"Generate a feature related to {user_text}") for _ in range(3)]
                } for price in ["25", "30", "45"]
            ]
        },
        "testimonials": {
            "title": {
                "mainTitle": generate_text(f"Generate a title related to {user_text}"),
                "primaryTitle": generate_text(f"Generate a title related to {user_text}"),
                "secondaryTitle": generate_text(f"Generate a title related to {user_text}")
            },
            "imgUrl": [search_image(f"Generate an image related to {user_text}") for _ in range(2)],
            "testimonials": [
                {
                    "imgUrl": search_image(f"Generate an avatar image related to {user_text}"),
                    "review": generate_text(f"Generate a review related to {user_text}"),
                    "name": generate_text(f"Generate a name related to {user_text}"),
                    "status": generate_text(f"Generate a status related to {user_text}")
                } for _ in range(3)
            ]
        },
        "cta": {
            "title": [
                { "Subtitle": generate_text(f"Generate a subtitle related to {user_text}") } for _ in range(4)
            ],
            "actionButton": generate_text(f"Generate a button text related to {user_text}")
        },
        "footer": {
            "imgUrl": search_image(f"Generate an image related to {user_text}"),
            "medias": [
                {
                    "icon": search_image(f"Generate an icon for {platform} related to {user_text}"),
                    "url": f"https://{platform}.com"
                } for platform in ["github", "linkedin", "instagram"]
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }

# Example Usage
# print(schema_3("fitness and wellness"))