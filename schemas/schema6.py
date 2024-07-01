import random
from datetime import datetime
from utils import generate_text, search_image

def schema_6(user_text):
    return {
        "templateInfo": {
            "id": 6,
            "title": generate_text(f"Generate a 2-word name for a fitness website about {user_text}"),
            "description": generate_text(f"Create a brief description for a fitness website in 20 words about {user_text}"),
            "imgUrl": search_image(f"Fitness website logo related to {user_text}")
        },
        "navbar": {
            "logo": search_image(f"Minimalist fitness logo icon for {user_text}"),
            "searchIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095771/jammal_photos/kedw9coptwqkovrsssd1.svg",
            "shoppingIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
            "menuIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095877/jammal_photos/rwbeynsg3bftgrjqaqnf.svg",
            "links": [
                {"title": "Home", "url": "#"},
                {"title": "About", "url": "#"},
                {"title": "Menu", "url": "#"},
                {"title": "Recipes", "url": "#"},
                {"title": "Contact", "url": "#"}
            ]
        },
        "hero": {
            "buttonText": generate_text(f"Generate a 2-word call-to-action for {user_text}"),
            "heros": [
                {
                    "id": "01",
                    "title": generate_text(f"Create a 5-word title for the main hero section about {user_text}"),
                    "description": generate_text(f"Write a 15-word description for the main hero section about {user_text}"),
                    "imgUrl": search_image(f"Fitness hero image for {user_text}")
                },
                {
                    "id": "02",
                    "title": generate_text(f"Create a 5-word title for the second hero section about {user_text}"),
                    "description": generate_text(f"Write a 15-word description for the second hero section about {user_text}"),
                    "imgUrl": search_image(f"Another fitness hero image for {user_text}")
                },
                {
                    "id": "03",
                    "title": generate_text(f"Create a 5-word title for the third hero section about {user_text}"),
                    "description": generate_text(f"Write a 15-word description for the third hero section about {user_text}"),
                    "imgUrl": search_image(f"Third fitness hero image for {user_text}")
                }
            ]
        },
        "menu": {
            "Title": generate_text(f"Generate a 3-word title for the fitness menu section about {user_text}"),
            "Card": {
                "shoppingIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
                "rateIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1706352872/jammal_photos/v02eynmgkqv3wkrbhnda.svg",
                "valueName": "Price: $"
            },
            "Menus": [
                {
                    "id": "01",
                    "title": generate_text(f"Generate a 1-word title for a fitness menu item related to {user_text}"),
                    "price": 25,
                    "imgUrl": search_image(f"Fitness menu item image for {user_text}")
                },
                {
                    "id": "02",
                    "title": generate_text(f"Generate another 1-word title for a fitness menu item related to {user_text}"),
                    "price": 250,
                    "imgUrl": search_image(f"Another fitness menu item image for {user_text}")
                },
                {
                    "id": "03",
                    "title": generate_text(f"Generate a third 1-word title for a fitness menu item related to {user_text}"),
                    "price": 45,
                    "imgUrl": search_image(f"Third fitness menu item image for {user_text}")
                },
                {
                    "id": "04",
                    "title": generate_text(f"Generate a fourth 1-word title for a fitness menu item related to {user_text}"),
                    "price": 75,
                    "imgUrl": search_image(f"Fourth fitness menu item image for {user_text}")
                }
            ]
        },
        "products": {
            "menuTitle": generate_text(f"Generate a 3-4 word title for the menu section related to {user_text}"),
            "Card": {
                "shoppingIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
                "rateIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1706352872/jammal_photos/v02eynmgkqv3wkrbhnda.svg",
                "valueName": "Price: $"
            },
            "filterContent": [
                {
                    "title": generate_text(f"Generate a 2-word category name for {user_text} products"),
                    "content": [
                        {
                            "id": str(i+1).zfill(2),
                            "title": generate_text(f"Generate a 1-2 word product name for {user_text} category 1, item {i+1}"),
                            "price": round(random.uniform(10, 300), 2),
                            "imgUrl": search_image(f"{user_text} product image for category 1, item {i+1}")
                        } for i in range(8)
                    ]
                },
                {
                    "title": generate_text(f"Generate another 2-word category name for {user_text} products"),
                    "content": [
                        {
                            "id": str(i+9).zfill(2),
                            "title": generate_text(f"Generate a 1-2 word product name for {user_text} category 2, item {i+1}"),
                            "price": round(random.uniform(10, 300), 2),
                            "imgUrl": search_image(f"{user_text} product image for category 2, item {i+1}")
                        } for i in range(8)
                    ]
                },
                {
                    "title": generate_text(f"Generate a third 2-word category name for {user_text} products"),
                    "content": [
                        {
                            "id": str(i+17).zfill(2),
                            "title": generate_text(f"Generate a 1-2 word product name for {user_text} category 3, item {i+1}"),
                            "price": round(random.uniform(10, 300), 2),
                            "imgUrl": search_image(f"{user_text} product image for category 3, item {i+1}")
                        } for i in range(8)
                    ]
                },
                {
                    "title": generate_text(f"Generate a fourth 2-word category name for {user_text} products"),
                    "content": [
                        {
                            "id": str(i+25).zfill(2),
                            "title": generate_text(f"Generate a 1-2 word product name for {user_text} category 4, item {i+1}"),
                            "price": round(random.uniform(10, 300), 2),
                            "imgUrl": search_image(f"{user_text} product image for category 4, item {i+1}")
                        } for i in range(8)
                    ]
                },
                {
                    "title": generate_text(f"Generate a fifth 2-word category name for {user_text} products"),
                    "content": [
                        {
                            "id": str(i+33).zfill(2),
                            "title": generate_text(f"Generate a 1-2 word product name for {user_text} category 5, item {i+1}"),
                            "price": round(random.uniform(10, 300), 2),
                            "imgUrl": search_image(f"{user_text} product image for category 5, item {i+1}")
                        } for i in range(8)
                    ]
                }
            ]
        },
        "features": {
            "title": generate_text(f"Generate a 3-4 word question about the identity of {user_text}"),
            "imgUrl": search_image(f"Representative image for {user_text} business"),
            "description": generate_text(f"Create a 7-10 word tagline about the benefits of {user_text}"),
            "info": generate_text(f"Write a 15-20 word statement about commitment to excellence for {user_text}"),
            "cards": [
                {
                    "icon": search_image(f"Icon for {feature} related to {user_text}"),
                    "title": generate_text(f"Generate a 2-3 word title for {feature} feature of {user_text}"),
                    "description": generate_text(f"Write a 8-10 word description for {feature} feature of {user_text}")
                } for feature in ["delivery", "customer service", "security", "support"]
            ]
        },
        "testimonials": {
            "title": generate_text(f"Generate a 5-7 word title for customer testimonials about {user_text}"),
            "imgUrl": search_image(f"Customer testimonial background image for {user_text}"),
            "cards": [
                {
                    "content": generate_text(f"Write a 20-25 word testimonial for {user_text} from perspective of a {role}"),
                    "name": generate_text(f"Generate a full name for a {role}"),
                    "role": role
                } for role in ["customer", "business partner", "employee"]
            ]
        },
        "cta": {
            "title": generate_text(f"Generate a 3-4 word call-to-action title for {user_text} app"),
            "description": generate_text(f"Write a 10-12 word compelling description for downloading the {user_text} app"),
            "info": generate_text(f"Create a 20-25 word detailed description of the benefits of the {user_text} app"),
            "imgUrl": search_image(f"Mobile app mockup for {user_text}"),
            "googleButton": {
                "title": "Google Play",
                "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703106187/jammal_photos/bm7fqpnzrwtkawffbci3.svg"
            },
            "appleButton": {
                "title": "Apple Store",
                "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703106097/jammal_photos/gmyir4uguaz6ejvw3s3t.svg"
            }
        },
        "footer": {
            "logo": search_image(f"Logo for {user_text}"),
            "imgUrl": search_image(f"Footer background image for {user_text}"),
            "description": generate_text(f"Write a 15-20 word description about {user_text} for the footer"),
            "copyright": f"Copyright {datetime.now().year}, {generate_text(f'Generate a 2-3 word company name for {user_text}')}. All rights reserved",
            "footerSections": [
                {
                    "title": "Info Links",
                    "links": [
                        {"title": link, "url": "#"} for link in ["Terms & Conditions", "Privacy Policy", "Return & Refund", "Payment Method"]
                    ]
                },
                {
                    "title": "Quick Links",
                    "links": [
                        {"title": generate_text(f"Generate a 1-2 word link name related to {user_text}"), "url": "#"} for _ in range(4)
                    ]
                }
            ],
            "contacts": [
                {
                    "value": generate_text(f"Generate a fictional address for {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108316/jammal_photos/oe8rjvrg0ckgohix2b6v.svg"
                },
                {
                    "value": generate_text(f"Generate a fictional email for {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108228/jammal_photos/opdhewds9do1znaaj5li.svg"
                },
                {
                    "value": generate_text(f"Generate a fictional phone number for {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108367/jammal_photos/y2583eh76th902gnzlje.svg"
                }
            ]
        },
        "colors": {
            "templateColors": [
                generate_text(f"Generate a dark color hex code for {user_text}"),
                generate_text(f"Generate another dark color hex code for {user_text}"),
                generate_text(f"Generate a vibrant color hex code for {user_text}"),
                generate_text(f"Generate another vibrant color hex code for {user_text}"),
                "#fff",
                generate_text(f"Generate a light gray color hex code for {user_text}")
            ]
        }
    }
