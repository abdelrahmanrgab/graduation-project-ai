from utils import generate_text, search_image

def schema_4(user_text):
    return {
        "templateInfo": {
            "id": 4,  # Adjusted to match the provided templateSlice1.json
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "links": [
                {"title": "Residencies", "url": "#"},
                {"title": "Our Value", "url": "#"},
                {"title": "Contact Us", "url": "#"},
                {"title": "Get Started", "url": "#"}
            ],
            "email4": "mailto:zainkeepscode@gmail.com",  # Added email4 to align with the provided JSON
            "buttonText": "Contact"  # Changed to align with the provided JSON
        },
        "hero": {
            "imgUrl": search_image(f"I need a link for an image to be used as wallpaper for a website about {user_text}"),
            "title": generate_text(f"generate title for this website in just 5 words {user_text}"),
            "description1": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "description2": generate_text(f"Provide another brief description in 15 words about {user_text}"),
            "buttonText": "Search",  # Changed to align with the provided JSON
            "stats": [
                {"title": "Premium Product", "start": "8880", "end": "9000"},
                {"title": "Happy Customer", "start": "1950", "end": "2000"},
                {"title": "Awards Winning", "start": "0", "end": "28"}
            ],
            "duration": "6",
            "icon": "+"
        },
        "features": {
            "title": "Our Value",
            "sub_title": "Value We Give to You",  # Added sub_title to align with the provided JSON
            "description1": "We are always ready to help by providing the best services for you.",
            "description2": "We believe a good place to live can make your life better",
            "features": [
                {
                    "icon": "💧",
                    "heading": generate_text(f"generate heading for a feature related to {user_text}"),
                    "detail": generate_text(f"generate detailed description in 20 words for a feature related to {user_text}")
                },
                {
                    "icon": "🩲",
                    "heading": generate_text(f"generate heading for a feature related to {user_text}"),
                    "detail": generate_text(f"generate detailed description in 20 words for a feature related to {user_text}")
                },
                {
                    "icon": "✔",
                    "heading": generate_text(f"generate heading for a feature related to {user_text}"),
                    "detail": generate_text(f"generate detailed description in 20 words for a feature related to {user_text}")
                }
            ],
            "imgUrl": search_image(f"I need an image to describe {user_text} as a feature")
        },
        "projects": {
            "title": "Best Choices",
            "sub_title": "Popular Residencies",  # Added sub_title to align with the provided JSON
            "projects": [
                {
                    "image": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "name": generate_text(f"generate only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "price": generate_text(f"generate a price for a project related to {user_text}"),
                    "detail": generate_text(f"generate a brief description in 10 words for a project related to {user_text}")
                },
                {
                    "image": search_image(f"I need an image to represent the name of the second project for a website about {user_text}"),
                    "name": generate_text(f"generate only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "price": generate_text(f"generate a price for a project related to {user_text}"),
                    "detail": generate_text(f"generate a brief description in 10 words for a project related to {user_text}")
                },
                {
                    "image": search_image(f"I need an image to represent the name of the third project for a website about {user_text}"),
                    "name": generate_text(f"generate only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "price": generate_text(f"generate a price for a project related to {user_text}"),
                    "detail": generate_text(f"generate a brief description in 10 words for a project related to {user_text}")
                }
            ]
        },
        "contact": {
            "title": "Contact Us",
            "sub_title": "Easy to contact us",  # Added sub_title to align with the provided JSON
            "description": "We are always ready to help by providing the best services for you. We believe a good place to live can make your life better",
            "email": "contact@interno.com",  # Changed to align with the provided JSON
            "phone": "(123) 125-858",  # Changed to align with the provided JSON
            "UrlImage": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703206872/jammal_photos/hqcx6ikyfgeuqe0vcset.jpg",  # Changed to align with the provided JSON
            "contacts": [
                {
                    "type": "Call",
                    "phone": "021 123 145 14",
                    "btn_contact": "Call now"
                },
                {
                    "type": "Chat",
                    "phone": "021 123 145 14",
                    "btn_contact": "Chat now"
                },
                {
                    "type": "Video Call",
                    "phone": "021 123 145 14",
                    "btn_contact": "Video Call now"
                },
                {
                    "type": "Message",
                    "phone": "021 123 145 14",
                    "btn_contact": "Message now"
                }
            ]
        },
        "cta": {
            "title": "Get started with Homyz",
            "description1": generate_text(f"Generate a short description (up to 15 words) for a CTA section about {user_text}"),
            "description2": generate_text(f"Generate another short description (up to 15 words) for a CTA section about {user_text}"),
            "buttonText": "Get Started",  # Changed to align with the provided JSON
            "email": "mailto:zainkeepscode@gmail.com"  # Changed to align with the provided JSON
        },
        "footer": {
            "logo": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703209942/jammal_photos/xd2ugq6yopzvjkw37qc7.png",  # Changed to align with the provided JSON
            "description": "Our vision is to make all people the best place to live for them.",
            "footerSections": [
                {
                    "title": "Services",
                    "links": [
                        {"title": "Property", "url": "#"},
                        {"title": "Services", "url": "#"},
                        {"title": "Product", "url": "#"},
                        {"title": "About Us", "url": "#"}
                    ]
                }
            ],
            "contacts": [
                {"value": "145 New York, FL 5467, USA"}  # Changed to align with the provided JSON
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]  # Changed to align with the provided JSON
        }
    }

# # Example usage
# user_text = "luxury real estate"
# schema = schema_1(user_text)
# print(json.dumps(schema, indent=2))
