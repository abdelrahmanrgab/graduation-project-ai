from utils import generate_text, search_image

def schema_1(user_text):
    return {
        "templateInfo": {
            "id": 1,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"generate a description for a website in just 10 words about {user_text}"),
            "imgUrl": search_image(f"generate an image URL for a website about {user_text}")
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "links": [
                {"title": "home", "url": "#"},
                {"title": "pages", "url": "#"},
                {"title": "services", "url": "#"},
                {"title": "projects", "url": "#"},
                {"title": "blog", "url": "#"},
                {"title": "contact", "url": "#"}
            ]
        },
        "hero": {
            "title": generate_text(f"generate title for this website in just 5 words {user_text}"),
            "description": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "buttonText": "Get Started",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"I need a link for an image to be used as wallpaper for a website about {user_text}")
        },
        "services": {
            "services": [
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_one_xvd7d6.svg"
                },
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in just 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_two_dptua1.svg"
                },
                {
                    "title": generate_text(f"generate just only title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in just 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_three_v71ltg.svg"
                }
            ]
        },
        "features": {
            "title": generate_text(f"Suggest a title for a feature in 10 words related to {user_text}"),
            "description": generate_text(f"Create a brief description in 20-25 words for a feature related to {user_text}"),
            "phone": "012345678",
            "buttonText": "Get Free Estimate",
            "icons": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813236/templates/template_one/Call_gqvv4l.svg",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg"
            ],
            "imgUrl": search_image(f"I need an image to describe {user_text} as a feature")
        },
        "testimonials": {
            "title": "What the People Think About Us",
            "testimonials": [
                {
                    "name": "Nattasha Mith",
                    "location": "Sydney, USA",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate a brief description in 10-15 words for a client who used our services about {user_text}")
                },
                {
                    "name": "Raymond Galario",
                    "location": "Sydney, Australia",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate a brief description in 10-15 words for a client who used our services about {user_text}")
                },
                {
                    "name": "Benny Roll",
                    "location": "Sydney, New York",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate a brief description in 10-15 words for a client who used our services about {user_text}")
                }
            ]
        },
        "logos": {
            "companies": [
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/01_p78hjd.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/02_mnw1ps.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/03_fiplpx.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/04_pg8flc.svg", "url": "https://x.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/05_prt3gi.svg", "url": "https://x.com"}
            ]
        },
        "projects": {
            "title": "Follow Our Projects",
            "description": generate_text(f"Create a brief description for a projects section in 20 words about {user_text}"),
            "projects": [
                {
                    "title": generate_text(f"Generate a project title related to {user_text}"),
                    "description": generate_text(f"Create a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate a project title related to {user_text}"),
                    "description": generate_text(f"Create a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate a project title related to {user_text}"),
                    "description": generate_text(f"Create a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate a project title related to {user_text}"),
                    "description": generate_text(f"Create a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                }
            ]
        },
        "statistics": {
            "statistics": [
                {"title": "Years Of Experience", "value": "12"},
                {"title": "Success Projects", "value": "85"},
                {"title": "Active Projects", "value": "15"},
                {"title": "Happy Customers", "value": "95"}
            ]
        },
        "items": {
            "title": "Articles & News",
            "description": generate_text(f"Create a brief description for an articles section in 20 words about {user_text}"),
            "items": [
                {
                    "title": generate_text(f"Generate a title for an article related to {user_text}"),
                    "subtitle": generate_text(f"Generate a subtitle for an article related to {user_text}"),
                    "description": generate_text(f"Generate a publication date for an article related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for an article related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate a title for an article related to {user_text}"),
                    "subtitle": generate_text(f"Generate a subtitle for an article related to {user_text}"),
                    "description": generate_text(f"Generate a publication date for an article related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for an article related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate a title for an article related to {user_text}"),
                    "subtitle": generate_text(f"Generate a subtitle for an article related to {user_text}"),
                    "description": generate_text(f"Generate a publication date for an article related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for an article related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                }
            ]
        },
        "contact": {
            "title": "Get In Touch",
            "description": generate_text(f"Create a brief description for a contact section in 10 words about {user_text}"),
            "address": "66 broklyn Street, New York",
            "email": "example@email.com",
            "phone": "+07 554 332 322",
            "imgUrl": search_image(f"I need an image to represent contact related to {user_text}")
        },
        "social": {
            "title": "Follow Us On",
            "icons": [
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701717448/templates/template_one/fb_cjmkfw.svg", "url": "https://facebook.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701717448/templates/template_one/Vector_oplddv.svg", "url": "https://twitter.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701717448/templates/template_one/in_rkmxz6.svg", "url": "https://linkedin.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701717448/templates/template_one/ig_uqknkl.svg", "url": "https://instagram.com"},
                {"imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701717448/templates/template_one/tik_nl3bzx.svg", "url": "https://tiktok.com"}
            ]
        }
    }



