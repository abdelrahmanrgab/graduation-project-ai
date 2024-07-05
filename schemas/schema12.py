from utils import generate_text, search_image

def schema_12(user_text):
    return {
        "templateInfo": {
            "id": 12,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719850710/jammal_photos/vh9x6ll6nixpsybvxe5q.png",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719850811/jammal_photos/brginprtncegbiyr3wqf.png",
            "links": [
                {"title": "home", "url": "#"},
                {"title": "Features", "url": "#"},
                {"title": "About", "url": "#"},
                {"title": "Teams", "url": "#"},
                {"title": "contact", "url": "#"}
            ]
        },
        "hero": {
            "title": generate_text(f"generate title for this website in just 5 words {user_text}"),
            "description": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "buttonText": "Explore More",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719850606/jammal_photos/cela2eggopmbbsfgcylq.png",
            "imgUrl": search_image(f"I need an link for image to be used as wallpaper for a website about {user_text}")
        },
        "features": {
            "title": generate_text(f"Suggest a title for a feature in 10 words related to {user_text}"),
            "features": [
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719830119/jammal_photos/bya9nzubv9jbt5aukuax.png",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719827222/jammal_photos/ei4ppt3gybkh7l98hapt.png"
                },
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719850422/jammal_photos/rarjoggq9u01wohrff7f.png",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719827442/jammal_photos/qpz2eidko6xewm7arggi.png"
                },
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719850494/jammal_photos/x0bevimtd0kdrjap1acf.png",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1719827597/jammal_photos/bxmfbv8zmfjw7kbuewiu.png"
                }
            ]
        },
        "about": {
            "title": generate_text(f"ABOUT {user_text.upper()}"),
            "subtitle": generate_text(f"Subtitle for about section related to {user_text}"),
            "description": generate_text(f"Create a brief description in 20:25 words for an about section related to {user_text}"),
            "imgUrl": search_image(f"I need an image for the about section of a {user_text} website")
        },
        "team": {
            "title": "Our Teams",
            "members": [
                {"imgUrl": search_image("portrait of a team member")},
                {"imgUrl": search_image("portrait of another team member")},
                {"imgUrl": search_image("portrait of a third team member")},
                {"imgUrl": search_image("portrait of a fourth team member")}
            ],
            "buttonText": "See more here",
            "icon": "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855189/white-arrow_bmhias.png"
        },
        "contact": {
            "icons": [
                "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855279/msg-icon_admjx1.png",
                "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855301/mail-icon_cfnj5m.png",
                "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855333/phone-icon_ct28v1.png",
                "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855417/location-icon_ytfm0b.png",
                "https://res.cloudinary.com/di8kjrflu/image/upload/v1719855189/white-arrow_bmhias.png"
            ],
            "title": "Send us a message",
            "description": generate_text(f"Create a brief contact description related to {user_text}"),
            "contacts": [
                {"icon": 1, "text": "Contact@edusite.dev"},
                {"icon": 2, "text": "+1 123-456-7890"},
                {"icon": 3, "text": "77 Massachusetts Ave, Cambridge\nMA 02139, United States"}
            ]
        },
        "colors": {
            "templateColors": ["#ffffff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }
