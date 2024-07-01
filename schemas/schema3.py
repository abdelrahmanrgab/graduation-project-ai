from utils import generate_text, search_image


def schema_3(user_text):
    return {
        "templateInfo": {
            "id": 3,
            "title": generate_text(f"Generate only name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"Generate a short description in just 10 words about {user_text}"),
            "imgUrl": search_image(f"Find an image link to be used as wallpaper for a website about {user_text}")
        },
        "navbar": {
            "logos": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1705928879/jammal_photos/vqliep1jh8zlgkmwkewx.png",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1705931744/jammal_photos/fbb4rdapofxl04oewfc3.png"
            ],
            "links": ["Home", "Programs", "Why us", "Plans", "Testimonials"]
        },
        "hero": {
            "Subtitle": generate_text(f"Generate title for this website in just 5 words about {user_text}"),
            "imgUrl": search_image(f"Find an image link to be used as wallpaper for a website about {user_text}"),
            "title": generate_text(f"Generate title for this website in just 5 words about {user_text}"),
            "description": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "statistics": [
                {
                    "count": "+140",
                    "description": generate_text(f"Create a brief description in just 5 words about {user_text}")
                },
                {
                    "count": "+978",
                    "description": generate_text(f"Create a brief description in just 5 words about {user_text}")
                },
                {
                    "count": "+50",
                    "description": generate_text(f"Create a brief description in just 5 words about {user_text}")
                }
            ],
            "Button": {
                "primaryButton": "Get Started",
                "secondaryButton": generate_text(f"Generate button text in 2 words for {user_text}"),
                "actionButton": generate_text(f"Generate button text in 2 words for {user_text}")
            }
        },
        "projects": {
            "title": [
                { "Subtitle": generate_text(f"Generate subtitle in 5 words for {user_text}") },
                { "Subtitle": generate_text(f"Generate subtitle in 5 words for {user_text}") },
                { "Subtitle": generate_text(f"Generate subtitle in 5 words for {user_text}") }
            ],
            "actionButton": generate_text(f"Generate button text in 2 words for {user_text}"),
            "imgUrl": search_image(f"Find an image related to {user_text}"),
            "descriptions": [
                {
                    "heading": generate_text(f"Generate just the title name for a project related to {user_text}"),
                    "details": generate_text(f"Create a brief description in 15 words for a project related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate just the title name for a project related to {user_text}"),
                    "details": generate_text(f"Create a brief description in 15 words for a project related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate just the title name for a project related to {user_text}"),
                    "details": generate_text(f"Create a brief description in 15 words for a project related to {user_text}")
                },
                {
                    "heading": generate_text(f"Generate just the title name for a project related to {user_text}"),
                    "details": generate_text(f"Create a brief description in 15 words for a project related to {user_text}")
                }
            ]
        },
        "features": {
            "Subtitle": generate_text(f"Generate a subtitle in 5 words highlighting key features of {user_text}"),
            "title": generate_text(f"Generate a main title in 5 words for the features section focusing on {user_text}"),
            "imgUrl": [search_image(f"Find an image representing a key feature of {user_text}") for _ in range(8)],
            "statistics": [
                {"description": generate_text(f"Provide a brief description in 5 words of a feature related to {user_text}")} for _ in range(5)
            ]
        },
        "pricing": {
            "title": [
                { "Subtitle": generate_text(f"Generate a subtitle introducing pricing plans in 5 words for {user_text}") } for _ in range(3)
            ],
            "description": generate_text(f"Write a clear description of pricing options in 10 words for {user_text}"),
            "actionButton": generate_text(f"Generate a call-to-action button text in 2 words for {user_text}"),
            "imgUrl": search_image(f"Find an image representing pricing plans for {user_text}"),
            "plans": [
                {
                    "name": generate_text(f"Generate a plan name in 3 words related to {user_text}"),
                    "price": price,
                    "features": [generate_text(f"List a feature in 5 words included in the plan related to {user_text}") for _ in range(3)]
                } for price in ["25", "30", "45"]
            ]
        },
        "testimonials": {
            "title": {
                "mainTitle": generate_text(f"Generate a main title in 5 words for the testimonials section about {user_text}"),
                "primaryTitle": generate_text(f"Generate a primary title in 5 words for customer testimonials related to {user_text}"),
                "secondaryTitle": generate_text(f"Write a secondary title in 5 words for user reviews about {user_text}")
            },
            "imgUrl": [search_image(f"Find an image representing customer satisfaction with {user_text}") for _ in range(2)],
            "testimonials": [
                {
                    "imgUrl": search_image(f"Find an avatar image for a satisfied customer of {user_text}"),
                    "review": generate_text(f"Write a positive review in 10 words from a customer about {user_text}"),
                    "name": generate_text(f"Generate a name for a customer in 2 words who is happy with {user_text}"),
                    "status": generate_text(f"Generate a status or role in 2 words for a customer who uses {user_text}")
                } for _ in range(3)
            ]
        },
        "cta": {
            "title": [
                { "Subtitle": generate_text(f"Generate a subtitle in 5 words for a call-to-action related to {user_text}") } for _ in range(4)
            ],
            "actionButton": generate_text(f"Generate a call-to-action button text in 2 words to engage with {user_text}")
        },
        "footer": {
            "imgUrl": search_image(f"Find a footer background image that represents {user_text}"),
            "medias": [
                {
                    "icon": search_image(f"Find an icon for {platform} related to {user_text}"),
                    "url": f"https://{platform}.com"
                } for platform in ["github", "linkedin", "instagram"]
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }
