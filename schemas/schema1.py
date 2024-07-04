from utils import generate_text, search_image

def schema_1(user_text):
    return {
        "templateInfo": {
            "id": 1,
            "title": generate_text(f"generate just only one  name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"generate just only one a description for a website in just 10 words about {user_text}"),
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
            "title": generate_text(f"generate just only one title for this website in just 5 words {user_text}"),
            "description": generate_text(f"Create just only one a brief description for a website in just 20 words about {user_text}"),
            "buttonText": "Get Started",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"I need a link for an image to be used as wallpaper for a website about {user_text}")
        },
        "services": {
            "services": [
                {
                    "title": generate_text(f"generate just only one title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_one_xvd7d6.svg"
                },
                {
                    "title": generate_text(f"generate just only one title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in just 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_two_dptua1.svg"
                },
                {
                    "title": generate_text(f"generate just only one title name for a service related to {user_text}"),
                    "description": generate_text(f"Create a brief description in just 15 words for a service related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_three_v71ltg.svg"
                }
            ]
        },
        "features": {
            "title": generate_text(f"generate just only one a title for a feature in 10 words related to {user_text}"),
            "description": generate_text(f"Create just only one a brief description in 20-25 words for a feature related to {user_text}"),
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
                    "opinion": generate_text(f"Generate just only one a brief description in 10-15 words for a client who used our services about {user_text}")
                },
                {
                    "name": "Raymond Galario",
                    "location": "Sydney, Australia",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate just only one a brief description in 10-15 words for a client who used our services about {user_text}")
                },
                {
                    "name": "Benny Roll",
                    "location": "Sydney, New York",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate just only one a brief description in 10-15 words for a client who used our services about {user_text}")
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
            "description": generate_text(f"Create just only one a brief description for a projects section in 20 words about {user_text}"),
            "projects": [
                {
                    "title": generate_text(f"Generate just only one a project title related to {user_text}"),
                    "description": generate_text(f"Create just only one a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate just only one a project title related to {user_text}"),
                    "description": generate_text(f"Create just only one a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate just only one a project title related to {user_text}"),
                    "description": generate_text(f"Create just only one a brief description for a project in 10 words related to {user_text}"),
                    "imgUrl": search_image(f"I need an image for a project related to {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"Generate just only one a project title related to {user_text}"),
                    "description": generate_text(f"Create just only one a brief description for a project in 10 words related to {user_text}"),
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
            "description": "It is a long established fact that a reader will be distracted by the of readable content of a page when lookings at its layouts the points of using.",
            "items": [
                {
                    "title": "Let’s Get Solution For Building Construction Work",
                    "subtitle": "Kitchen Design",
                    "description": "26 December, 2022",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718041/templates/template_one/article1.f88f54e6a4cdbf340b36_l3ujjw.png",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                },
                {
                    "title": "Low Cost Latest Invented Interior Designing Ideas.",
                    "subtitle": "Living Design",
                    "description": "22 December, 2022",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article2.43be768543cb8cfeaf07_atvwjd.png",
                },
                {
                    "title": "Best For Any Office & Business Interior Solution",
                    "subtitle": "Interior Design",
                    "description": "25 December, 2022",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article3.f759fde0c85f3fb92b22_c2tqkv.png",
                },
            ],
        },
        "team": {
            "title": "Our Team Members",
            "members": [
                {
                    "memberId": "1",
                    "name": "Nattasha",
                    "email": "julie@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
                    "medias": [
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
                    ]
                },
                {
                    "memberId": "2",
                    "name": "Julie",
                    "email": "julie@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
                    "medias": [
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
                    ]
                },
                {
                    "memberId": "3",
                    "name": "Alex",
                    "email": "julie@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
                    "medias": [
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
                    ]
                },
                {
                    "memberId": "4",
                    "name": "John",
                    "email": "julie@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
                    "medias": [
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                        {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
                    ]
                }
            ]
        },
        "pricing": {
            "title": "Pricing & Plan",
            "description": "Home / Pricing",
            "plans": [
                {
                    "title": "Design advices",
                    "price": "29",
                    "timeUnit": "month",
                    "moneyUnit": "$",
                    "features": ["General living space advices", "Renovation advices", "Interior design advices", "Furniture reorganization", "Up to 5 hours meetings"],
                    "buttonText": "Get Started",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1709586475/Vector_urtrep.svg"
                },
                {
                    "title": "Design advices",
                    "price": "39",
                    "timeUnit": "month",
                    "moneyUnit": "$",
                    "features": ["Complete home redesign", "Interior and exterior works", "Modular interior planning", "Kitchen design", "Garages organization"],
                    "buttonText": "Get Started",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg"
                },
                {
                    "title": "Furniture design",
                    "price": "59",
                    "timeUnit": "month",
                    "moneyUnit": "$",
                    "features": ["Furniture for living room", "Furniture refurbishment", "Sofas and armchairs", "Tables and chairs", "Kitchens"],
                    "buttonText": "Get Started",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1709586475/Vector_urtrep.svg"
                }
            ]
        },
        "cta": {
            "title": "Wanna join the interno?",
            "description": "It is a long established fact  will be distracted.",
            "buttonText": "Contact With Us",
            "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1709586475/Vector_urtrep.svg"
        },
        "footer": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "description": "It is a long established fact that a reader will be distracted lookings.",
            "medias": [
                {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg", "url": "https://facebook.com"},
                {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg", "url": "https://x.com"},
                {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg", "url": "https://linkedin.com"},
                {"icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg", "url": "https://instagram.com"}
            ],
            "footerSections": [
                {
                    "title": "Services",
                    "links": [
                        {"title": "Kitchen", "url": "#"},
                        {"title": "Living Area", "url": "#"},
                        {"title": "Bathroom", "url": "#"},
                        {"title": "Dining Hall", "url": "#"},
                        {"title": "Bedroom", "url": "#"}
                    ]
                },
                {
                    "title": "Sections",
                    "links": [
                        {"title": "About Us", "url": "#"},
                        {"title": "Projects", "url": "#"},
                        {"title": "Our Team", "url": "#"},
                        {"title": "Contact Us", "url": "#"},
                        {"title": "Services", "url": "#"}
                    ]
                }
            ],
            "contacts": [
                {"value": "55 East Birchwood Ave. Brooklyn, New York 11201"},
                {"value": "contact@interno.com"},
                {"value": "(123) 125-858"}
            ]
        },
        "colors": {
            "templateColors": ["#ffffff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }