from utils import generate_text, search_image

def schema_1(user_text):
    return {
        "templateInfo": {
            "id": 1,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "links": [
                {
                    "title": "home",
                    "url": "#"
                },
                {
                    "title": "pages",
                    "url": "#"
                },
                {
                    "title": "services",
                    "url": "#"
                },
                {
                    "title": "projects",
                    "url": "#"
                },
                {
                    "title": "blog",
                    "url": "#"
                },
                {
                    "title": "contact",
                    "url": "#"
                }
            ]
        },
        "hero": {
            "title": generate_text(f"generate title for this website in just 5 words {user_text}"),
            "description": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "buttonText": "Get Started",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"I need an link for image to be used as wallpaper for a website about {user_text}")
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
                    "description": generate_text(f"Create a brief description in just 15  words for a service related to {user_text}"), 
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
            "description": generate_text(f"Create a brief description in 20 : 25 words for a feature related to {user_text}"),
            "phone": "012345678",
            "buttonText": "Get Free Estimate",
            "icons": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813236/templates/template_one/Call_gqvv4l.svg",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg"
            ],
            "imgUrl": search_image(f"I need an image to describe {user_text} as a feature")
        },
        "testimonials": {
            "title": "What the People Thinks About Us",
            "testimonials": [
                {
                    "name": "Nattasha Mith",
                    "location": "Sydney, USA",
                    "imgUrl": search_image("portrait of a client"),
                    "opinion": generate_text(f"Generate a brief description for in 10 : 15 words aclient who used our services about {user_text}")
                },
                {
                    "name": "Raymond Galario",
                    "location": "Sydney, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808853/templates/template_one/Photo_1_zsyklb.jpg",
                    "opinion":  generate_text(f"Generate a brief description for in 10 : 15 words a client who used our services about {user_text}")
                },
                {
                    "name": "Benny Roll ",
                    "location": "Sydney, New York",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808853/templates/template_one/Photo_1_zsyklb.jpg",
                    "opinion":  generate_text(f"Generate a brief description for in 10 : 15 words a client who used our services about {user_text}")
                }
            ]
        },
        "logos": {
            "companies": [
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/01_p78hjd.svg",
                    "url": "https://x.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/02_mnw1ps.svg",
                    "url": "https://x.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/03_fiplpx.svg",
                    "url": "https://x.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/04_pg8flc.svg",
                    "url": "https://x.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808449/templates/template_one/05_prt3gi.svg",
                    "url": "https://x.com"
                }
            ]
        },
        "projects": {
            "title": "Follow Our Projects",
            "description": "It is a long established fact that a reader will be distracted by the of readable content of page  lookings at its layouts  points.",
            "projects": [
                {
                    "title": generate_text(f"generate only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "description": generate_text(f"just Write a brief description in 2 words for the projects section of a {user_text} website"),
                    "imgUrl": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"generate another only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "description": generate_text(f"just Write a brief description in 2 words like Decor / Artchitecture for the projects section of a {user_text} website"),
                    "imgUrl": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"generate another only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "description": generate_text(f"just Write a brief description in 2 words like Decor / Artchitecture for the projects section of a {user_text} website"),
                    "imgUrl": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"generate another only title name in 2 or 3 words for a section about projects related to {user_text}"),
                    "description": generate_text(f"Write a brief description in 2 words like Decor / Artchitecture for the projects section of a {user_text} website"),
                    "imgUrl": search_image(f"I need an image to represent the name of the first project for a website about {user_text}"),
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                }
            ]
        },
        "statistics": {
            "statistics": [
                {
                    "title": "Years Of Experience",
                    "value": "12"
                },
                {
                    "title": "Success Projects",
                    "value": "85"
                },
                {
                    "title": "Active Projects",
                    "value": "15"
                },
                {
                    "title": "Happy Customers",
                    "value": "95"
                }
            ]
        },
        "items": {
            "title": "Articles & News",
            "description": "It is a long established fact that a reader will be distracted by the of readable content of a page when lookings at its layouts the points of using.",
            "items": [
                {
                    "title": generate_text(f"generate only title name for a section about items like (Let’s Get Solution For Building Construction Work) related to {user_text}"),
                    "subtitle": generate_text(f"generate only subtitle name for a section about items like (Kitchan Design) related to {user_text}"),
                    "description": "26 December,2022 ",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718041/templates/template_one/article1.f88f54e6a4cdbf340b36_l3ujjw.png",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg"
                },
                {
                    "title": generate_text(f"generate only title name for a section about items like (Let’s Get Solution For Building Construction Work) related to {user_text}"),
                    "subtitle": generate_text(f"generate only subtitle name for a section about items like (Kitchan Design) related to {user_text}"),
                    "description": "22 December,2022 ",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article2.43be768543cb8cfeaf07_atvwjd.png"
                },
                {
                    "title": generate_text(f"generate only title name for a section about items like (Let’s Get Solution For Building Construction Work) related to {user_text}"),
                    "subtitle": generate_text(f"generate only subtitle name for a section about items like (Kitchan Design) related to {user_text}"),
                    "description": "25 December,2022 ",
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718889/templates/template_one/Vector_5_nzmfwn.svg",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701718042/templates/template_one/article3.f759fde0c85f3fb92b22_c2tqkv.png"
                }
            ]
        },
        "team": {
            "title": "Our Team Members",
            "members": [
                {
                    "id": "1",
                    "name": "Nattasha",
                    "email": "julie@email.com",
                    "location": "Design, Australia",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
                    "medias": [
                        {
                            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
                            "url": "https://facebook.com"
                        },
                        {
                            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
                            "url": "https://x.com"
                        },
                        {
                            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
                            "url": "https://linkedin.com"
                        },
                        {
                            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
                            "url": "https://instagram.com"
                        }
                    ]
                }
            ]
        }
    }