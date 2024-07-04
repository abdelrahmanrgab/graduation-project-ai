from utils import generate_text, search_image

def schema_3(user_text):
    return {
        "templateInfo": {
            "id": 3,
            "title": generate_text(f"Create just only a title in 2-3 words for a website about {user_text}"),
            "description": generate_text(f"Generate just only a short description in 10-15 words summarizing what the website about {user_text} offers"),
            "imgUrl": search_image(f"Find a suitable logo image for a website focused on {user_text}")
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1705928879/jammal_photos/vqliep1jh8zlgkmwkewx.png",
            "links": [
                {"title": "Home", "url": "home"},
                {"title": "Programs", "url": "programs"},
                {"title": "Why us", "url": "WhyUs"},
                {"title": "Plans", "url": "Plans"},
                {"title": "Testimonials", "url": "Testimonials"},
            ]
        },
        "hero": {
            "title": generate_text(f"Generate just only a compelling main title in 5-7 words for the hero section about {user_text}"),
            "subtitle": generate_text(f"Generate just only an engaging subtitle in 5-7 words for the hero section about {user_text}"),
            "imgUrl": search_image(f"Locate a high-quality hero image related to {user_text} for the website"),
            "description": generate_text(f"Generate just only a brief description in 20-30 words highlighting the key message for the hero section about {user_text}"),
            "heros": [
                {"title": "+140", "subtitle": "EXPERT COACHS"},
                {"title": "+978", "subtitle": "MEMBERS JOINED"},
                {"title": "+50", "subtitle": "FITNESS PROGRAMS"},
            ],
            "buttonText": "Get Started",
            "linkText": "Learn More",
            "text": "Join now",
        },
        "projects": {
            "title": "EXPLORE OUR",
            "subtitle": "PROGRAMS",
            "description": "TO SHAPE YOU",
            "buttonText": "Join Now",
            "imgUrl": search_image(f"Generate just only an appealing image for the Programs section related to {user_text}"),
            "projects": [
                {
                    "title": generate_text(f"Generate just only a project title in 3-5 words for Strength Training related to {user_text}"),
                    "description": generate_text(f"Generate just only a brief description in 15-20 words for the Strength Training project about {user_text}"),
                },
                {
                    "title": generate_text(f"Generate just only a project title in 3-5 words for Cardio Training related to {user_text}"),
                    "description": generate_text(f"Generate just only a brief description in 15-20 words for the Cardio Training project about {user_text}"),
                },
                {
                    "title": generate_text(f"Generate just only a project title in 3-5 words for Fat Burning related to {user_text}"),
                    "description": generate_text(f"Generate just only a brief description in 15-20 words for the Fat Burning project about {user_text}"),
                },
                {
                    "title": generate_text(f"Generate just only a project title in 3-5 words for Health Fitness related to {user_text}"),
                    "description": generate_text(f"Generate just only a brief description in 15-20 words for the Health Fitness project about {user_text}"),
                },
            ],
        },
        "features": {
            "title": generate_text(f"Generate just only a concise title in 5-7 words for the features section about {user_text}"),
            "subtitle": generate_text(f"Generate just only a subtitle in 5-7 words summarizing the key features of {user_text}"),
            "imgs": [
                search_image(f"Find a feature image 1 that represents {user_text}"),
                search_image(f"Find a feature image 2 that represents {user_text}"),
                search_image(f"Find a feature image 3 that represents {user_text}"),
                search_image(f"Find a feature image 4 that represents {user_text}"),
                search_image(f"Find a feature image 5 that represents {user_text}"),
                search_image(f"Find a feature image 6 that represents {user_text}"),
                search_image(f"Find a feature image 7 that represents {user_text}"),
                search_image(f"Find a feature image 8 that represents {user_text}"),
            ],
            "features": [
                {"description": "OVER 140+ EXPERT COACHS"},
                {"description": "TRAIN SMARTER AND FASTER THAN BEFORE"},
                {"description": "1 FREE PROGRAM FOR NEW MEMBER"},
                {"description": "RELIABLE PARTNERS"},
                {"description": "OUR PARTNERS"},
            ],
        },
        "pricing": {
            "title": generate_text(f"Generate just only a title in 5-7 words for the pricing section about {user_text}"),
            "subtitle": generate_text(f"Generate just only a subtitle in 5-7 words explaining the pricing plans for {user_text}"),
            "text": generate_text(f"Generate just only a brief description in 10-15 words summarizing the pricing options for {user_text}"),
            "description": generate_text(f"Generate just only a detailed description in 20-30 words for the pricing section about {user_text}"),
            "buttonText": "Join Now",
            "imgUrl": search_image(f"Find a relevant image for the pricing section related to {user_text}"),
            "plans": [
                {
                    "title": generate_text(f"Generate just only a title in 3-5 words for the Basic Plan related to {user_text}"),
                    "price": "25",
                    "features": [
                        generate_text(f"Generate just only a feature in 5-7 words for the Basic Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Basic Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Basic Plan about {user_text}"),
                    ],
                },
                {
                    "title": generate_text(f"Generate just only a title in 3-5 words for the Premium Plan related to {user_text}"),
                    "price": "30",
                    "features": [
                        generate_text(f"Generate just only a feature in 5-7 words for the Premium Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Premium Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Premium Plan about {user_text}"),
                    ],
                },
                {
                    "title": generate_text(f"Generate just only a title in 3-5 words for the Pro Plan related to {user_text}"),
                    "price": "45",
                    "features": [
                        generate_text(f"Generate just only a feature in 5-7 words for the Pro Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Pro Plan about {user_text}"),
                        generate_text(f"Generate just only another feature in 5-7 words for the Pro Plan about {user_text}"),
                    ],
                },
            ],
        },
        "testimonials": {
            "title": generate_text(f"Generate just only a title in 5-7 words for the testimonials section about {user_text}"),
            "subtitle": generate_text(f"Generate just only a subtitle in 5-7 words highlighting customer experiences with {user_text}"),
            "description": generate_text(f"Generate just only a brief description in 15-20 words summarizing customer feedback about {user_text}"),
            "imgs": [
                search_image(f"Find a testimonial image 1 that represents customer experiences with {user_text}"),
                search_image(f"Find a testimonial image 2 that represents customer experiences with {user_text}"),
            ],
            "testimonials": [
                {
                    "name": "MATHEW HENDRICKSON",
                    "subtitle": "ENTREPRENEUR",
                    "description": "I made the right choice by choosing the Fitclub and by choosing the right plan and program I already achieved my ideal body!",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702986897/jammal_photos/xbinalf2qg4aqqhhpeif.png",
                },
                {
                    "name": "JOHN KEVIN",
                    "subtitle": "COACH",
                    "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi ipsam, ab itaque nam perferendis impedit sint",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702986859/jammal_photos/cwtimzgptwqccvycipw0.jpg",
                },
                {
                    "name": "FRANKLIN",
                    "subtitle": "CUSTOMER",
                    "description": "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minima aspernatur quod voluptatem",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702986807/jammal_photos/pnlbsd6lankxv5xc9px5.jpg",
                },
            ],
        },
        "cta": {
            "title": "READY TO",
            "subtitle": "LEVEL UP",
            "description": "YOUR BODY ",
            "text": "WITH US?",
            "buttonText": "Join Now",
        },
        "footer": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702990991/jammal_photos/isxpadjx12ja5wqaqzsk.png",  # logo
            "medias": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702990946/jammal_photos/op32ysn37afrbyyvzlpo.png",
                    "url": "https://github.com/login?client_id=45872a44c0e55c462eed&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D45872a44c0e55c462eed%26scope%3Duser%253Aemail%252Cread%253Aorg%26state%3Dgithub",
                },  
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702991031/jammal_photos/ttvjziej5llydncutm9u.png",
                    "url": "https://www.linkedin.com/login/ar",
                },  
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1702991055/jammal_photos/mt2lapqflvpafmnfpree.png",
                    "url": "https://instagram.com",
                },  
            ],
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"],
        },
    }
