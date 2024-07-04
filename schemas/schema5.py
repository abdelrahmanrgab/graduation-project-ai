from utils import generate_text, search_image

def schema_5(user_text):
    return {
        "templateInfo": {
            "id": 5,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703101139/logo_ytwn3z.jpg",
            "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703106705/menu-svgrepo-com_mgpt72.svg",
            "buttonText": "contact",
            "links": [
                {"title": "Home", "url": "#"},
                {"title": "About", "url": "#"},
                {"title": "Offers", "url": "#"},
                {"title": "Seats", "url": "#"},
                {"title": "Destinations", "url": "#"}
            ]
        },
        "hero": {
            "title": generate_text(f"generate title for this website in just 5 words {user_text}"),
            "imgUrl": search_image(f"I need a link for an image to be used as wallpaper for a website about {user_text}"),
            "videoUrl": "https://res.cloudinary.com/dmcdea0b9/video/upload/v1703110566/heroVideo_z23a38.mp4"
        },
        "features": {
            "title": generate_text(f"Suggest a title for a feature in 10 words related to {user_text}"),
            "subtitle": "travel support",
            "description": generate_text(f"Create a brief description in 20-25 words for a feature related to {user_text}"),
            "imgUrl": search_image(f"I need an image to describe {user_text} as a feature"),
            "features": [
                {"title": "Travel requirement for Dubai", "description": "Find help with booking and travel plans, see what to expect during the journey.", "number": "01"},
                {"title": "Travel requirement for Dubai", "description": "Find help with booking and travel plans, see what to expect during the journey.", "number": "02"},
                {"title": "Travel requirement for Dubai", "description": "Find help with booking and travel plans, see what to expect during the journey.", "number": "03"}
            ]
        },
        "services": {
            "title": generate_text(f"generate just only title name for a service related to {user_text}"),
            "services": [
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": generate_text(f"Create a brief description in 15 words for a service related to {user_text}"), "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703114489/calendar_ry8vjw.svg"},
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": generate_text(f"Create a brief description in 15 words for a service related to {user_text}"), "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703114500/ShieldCheck_tmepkt.svg"},
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": generate_text(f"Create a brief description in 15 words for a service related to {user_text}"), "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703114509/BookmarkCheckFill_jwdtcd.svg"}
            ]
        },
        "blogs": {
            "title": "Unaccompanied minor lounge",
            "imgUrl": search_image(f"I need an image for a blog about {user_text}"),
            "blogs": [
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": "Find help with booking and travel plans, see what to expect during the journey."},
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": "Find help with booking and travel plans, see what to expect during the journey."},
                {"title": generate_text(f"generate just only title name for a service related to {user_text}"), "description": "Find help with booking and travel plans, see what to expect during the journey."},
                {"title": generate_text(f"generate just only title name for a service related to{user_text}"), "description": "Find help with booking and travel plans, see what to expect during the journey."}
            ]
        },
        "team": {
            "title": "Top travelers of this month!",
            "members": [
                {"name": "IsraTech", "destinationImage": search_image(f"destination image for {user_text}"), "travelerImage": search_image("portrait of a traveler"), "socialLink": "@Isratech"},
                {"name": "IsraTech", "destinationImage": search_image(f"destination image for {user_text}"), "travelerImage": search_image("portrait of a traveler"), "socialLink": "@Isratech"},
                {"name": "IsraTech", "destinationImage": search_image(f"destination image for {user_text}"), "travelerImage": search_image("portrait of a traveler"), "socialLink": "@Isratech"},
                {"name": "IsraTech", "destinationImage": search_image(f"destination image for {user_text}"), "travelerImage": search_image("portrait of a traveler"), "socialLink": "@Isratech"}
            ]
        },
        "cta": {
            "title": "Subscribe Newsletter & get Latest News",
            "inputPlaceholder": "enter your email address",
            "buttonText": "Subscribe"
        },
        "footer": {
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1703101139/logo_ytwn3z.jpg",
            "description": "Your mind should be stronger than your feelings, fly!",
            "medias": [
                {"icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                {"icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                {"icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                {"icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
            ],
            "footerSections": [
                {
                    "title": "Information",
                    "links": [
                        {"title": "Home", "url": "#"},
                        {"title": "Explore", "url": "#"},
                        {"title": "Flight State", "url": "#"},
                        {"title": "Travel", "url": "#"},
                        {"title": "Check-In", "url": "#"},
                        {"title": "Manage your booking", "url": "#"}
                    ]
                },
                {
                    "title": "Quick Guide",
                    "links": [
                        {"title": "FAQ", "url": "#"},
                        {"title": "How To", "url": "#"},
                        {"title": "Features", "url": "#"},
                        {"title": "Baggage Us", "url": "#"},
                        {"title": "Route Map", "url": "#"},
                        {"title": "Our Communities", "url": "#"}
                    ]
                },
                {
                    "title": "Information",
                    "links": [
                        {"title": "Chauffer", "url": "#"},
                        {"title": "Our partners", "url": "#"},
                        {"title": "Destination", "url": "#"},
                        {"title": "Careers", "url": "#"},
                        {"title": "Transportation", "url": "#"},
                        {"title": "Programme Rules", "url": "#"}
                    ]
                }
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }
 

