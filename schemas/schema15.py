from utils import generate_text, search_image

def schema_15(user_text):
    return {
        "templateInfo": {
            "id": 15,
            "title": generate_text(f"Generate just only one name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"Generate just only one description for a website in just 10 words about {user_text}"),
            "imgUrl": search_image(f"Generate an image URL for a website about {user_text}")
        },
        "navbar": {
            "imgUrl": search_image("Generate an image URL for a logo of developer portfolio"),
            "links": [
                {"title": "Home", "url": "hero"},
                {"title": "Services", "url": "services"},
                {"title": "Skills", "url": "projects"},
                {"title": "Testimonials", "url": "testimonials"},
                {"title": "Contact", "url": "contact"}
            ]
        },
        "hero": {
            "sectionId": "hero",
            "imgUrl": search_image(f"Generate an image URL for a hero image for {user_text}"),
            "text": "HELLO MY NAME IS",
            "name": generate_text(f"Generate just only one developer name specializing in {user_text}"),
            "subtitle": generate_text(f"Generate just only one subtitle about {user_text}"),
            "description": generate_text(f"Generate just only one description about developer's experience and skills related to {user_text}"),
            "medias": [
                {"icon": search_image("Generate an image URL for a social media icon"), "url": "https://x.com/?lang-en="},
                {"icon": search_image("Generate an image URL for a social media icon"), "url": "https://play.google.com/store/apps/details?id=xyz.be.customer&hl=en_US&pli=1"},
                {"icon": search_image("Generate an image URL for a social media icon"), "url": "https://www.dribble.com/"}
            ],
            "title": generate_text(f"Generate just only one title with experience details for {user_text}"),
            "jop": generate_text(f"Generate just only one projects completed related to {user_text}"),
            "buttonText": "DOWNLOAD CV",
            "linkText": "MY SKILLS"
        },
        "services": {
            "sectionId": "services",
            "title": generate_text(f"Generate just only one title for services section about {user_text}"),
            "subtitle": "My Services",
            "buttonText": "See Pricing",
            "imgUrl": search_image(f"Generate an image URL for services section for {user_text}"),
            "services": [
                {
                    "title": generate_text(f"Generate just only one service title related to {user_text}"),
                    "subtitle": generate_text(f"Generate just only one service subtitle related to {user_text}"),
                    "description": generate_text(f"Generate just only one service description related to {user_text}")
                },
                {
                    "title": generate_text(f"Generate just only one service title related to {user_text}"),
                    "subtitle": generate_text(f"Generate just only one service subtitle related to {user_text}"),
                    "description": generate_text(f"Generate just only one service description related to {user_text}")
                },
                {
                    "title": generate_text(f"Generate just only one service title related to {user_text}"),
                    "subtitle": generate_text(f"Generate just only one service subtitle related to {user_text}"),
                    "description": generate_text(f"Generate just only one service description related to {user_text}")
                }
            ]
        },
        "features": {
            "sectionId": "features",
            "title": "PROFESSIONAL SKILLS",
            "subtitle": "My Talent",
            "features": [
                {
                    "title": "PHP",
                    "number": "85",
                    "description": generate_text(f"Generate just only one skill description related to PHP and {user_text}")
                },
                {
                    "title": "JavaScript",
                    "number": "65",
                    "description": generate_text(f"Generate just only one skill description related to JavaScript and {user_text}")
                },
                {
                    "title": "WordPress",
                    "number": "60",
                    "description": generate_text(f"Generate just only one skill description related to WordPress and {user_text}")
                },
                {
                    "title": "Python",
                    "number": "50",
                    "description": generate_text(f"Generate just only one skill description related to Python and {user_text}")
                },
                {
                    "title": "React",
                    "number": "70",
                    "description": generate_text(f"Generate just only one skill description related to React and {user_text}")
                },
                {
                    "title": "Adobe XD",
                    "number": "85",
                    "description": generate_text(f"Generate just only one skill description related to Adobe XD and {user_text}")
                }
            ]
        },
        "projects": {
            "sectionId": "projects",
            "title": "PORTFOLIO",
            "subtitle": "My Cases",
            "buttonText": "See Pricing",
            "linkText": "VIEW MORE",
            "imgUrl": search_image(f"Generate an image URL for projects section for {user_text}"),
            "categories": ["All", "VIDEO", "PHOTOGRAPHY", "BRANDING"],
            "projects": [
                {
                    "title": "BRANDING",
                    "subtitle": "Zorro",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for branding project about {user_text}")
                },
                {
                    "title": "BRANDING",
                    "subtitle": "Gooir",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for branding project about {user_text}")
                },
                {
                    "title": "VIDEO",
                    "subtitle": "Explore",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for video project about {user_text}")
                },
                {
                    "title": "VIDEO",
                    "subtitle": "Stay Fit",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for video project about {user_text}")
                },
                {
                    "title": "PHOTOGRAPHY",
                    "subtitle": "Kana",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for photography project about {user_text}")
                },
                {
                    "title": "PHOTOGRAPHY",
                    "subtitle": "Mozar",
                    "description": generate_text(f"Generate just only one project description related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for photography project about {user_text}")
                }
            ]
        },
        "cta": {
            "sectionId": "cta",
            "title": "RESUME",
            "subtitle": "My Story",
            "imgs": [
                search_image(f"Generate an image URL for resume section about {user_text}"),
                search_image(f"Generate an image URL for resume section about {user_text}")
            ],
            "educations": [
                {
                    "title": "CoderHouse Courses",
                    "subtitle": "Backend Programming",
                    "year": "2014 - 2016",
                    "description": generate_text(f"Generate just only one education description related to {user_text}"),
                    "category": "education"
                },
                {
                    "title": "Lviv National Academy of Arts",
                    "subtitle": "Faculty of Design",
                    "year": "2012 - 2014",
                    "description": generate_text(f"Generate just only one education description related to {user_text}"),
                    "category": "education"
                },
                {
                    "title": "IT Future",
                    "subtitle": "High School",
                    "year": "2010 - 2012",
                    "description": generate_text(f"Generate just only one education description related to {user_text}"),
                    "category": "education"
                }
            ],
            "experiences": [
                {
                    "title": "UI Head & Manager",
                    "subtitle": "Soft Tech Inc.",
                    "year": "2020 - 2022",
                    "description": generate_text(f"Generate just only one experience description related to {user_text}"),
                    "category": "experience"
                },
                {
                    "title": "UI / UX Specialist",
                    "subtitle": "Kana Design Studio",
                    "year": "2018 - 2020",
                    "description": generate_text(f"Generate just only one experience description related to {user_text}"),
                    "category": "experience"
                },
                {
                    "title": "Plugins Developer",
                    "subtitle": "Fiverr.com",
                    "year": "2016 - 2018",
                    "description": generate_text(f"Generate just only one experience description related to {user_text}"),
                    "category": "experience"
                }
            ]
        },
        "testimonials": {
            "sectionId": "testimonials",
            "title": "CLIENTS",
            "subtitle": "My Testimonials",
            "buttonText": "See Pricing",
            "imgUrl": search_image(f"Generate an image URL for testimonials section about {user_text}"),
            "testimonials": [
                {
                    "name": generate_text(f"Generate just only one name of a satisfied client about {user_text}"),
                    "subtitle": generate_text(f"Generate just only one subtitle for client about {user_text}"),
                    "description": generate_text(f"Generate just only one testimonial from a client about {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for a client portrait for {user_text}")
                },
                {
                    "name": generate_text(f"Generate just only one name of a satisfied client about {user_text}"),
                    "subtitle": generate_text(f"Generate just only one subtitle for client about {user_text}"),
                    "description": generate_text(f"Generate just only one testimonial from a client about {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for a client portrait for {user_text}")
                },
                {
                    "name": generate_text(f"Generate just only one name of a satisfied client about {user_text}"),
                    "subtitle": generate_text(f"Generate just only one subtitle for client about {user_text}"),
                    "description": generate_text(f"Generate just only one testimonial from a client about {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for a client portrait for {user_text}")
                }
            ]
        },
        "pricing": {
            "sectionId": "pricing",
            "title": "PRICING",
            "subtitle": "MY Price Board",
            "plans": [
                {
                    "title": generate_text(f"Generate just only one title for plan section related to {user_text}"),
                    "price": "39",
                    "description": generate_text(f"Generate just only one description for plan section related to {user_text}"),
                    "timeUnit": "hour",
                    "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
                },
                {
                    "title": generate_text(f"Generate just only one title for plan section related to {user_text}"),
                    "price": "259",
                    "description": generate_text(f"Generate just only one description for plan section related to {user_text}"),
                    "timeUnit": "Week",
                    "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
                },
                {
                    "title": generate_text(f"Generate just only one title for plan section related to {user_text}"),
                    "price": "1.249",
                    "description": generate_text(f"Generate just only one description for plan section related to {user_text}"),
                    "timeUnit": "Month",
                    "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
                }
            ],
            "buttonText": "START PROJECT",
            "imgs": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030355/jammal_photos/px8o2t9qtet1pumt2yip.svg",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030465/jammal_photos/capby7kt0b8mwxgzf3hs.png"
            ]
        },
        "blogs": {
            "sectionId": "blogs",
            "title": "LATEST BLOG",
            "subtitle": "MY Articles and Advice",
            "description": generate_text(f"Generate just only one description for blogs and article section related to {user_text}"),
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030465/jammal_photos/capby7kt0b8mwxgzf3hs.png",
            "buttonText": "Read more",
            "linkText": "VIEW BLOG",
            "blogs": [
                {
                    "title": "The Main Thing For The Designer",
                    "date": "OCTOBER 31, 2022",
                    "description": generate_text(f"Generate just only one description for blogs and article section related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for blogs and article about {user_text}")
                },
                {
                    "title": "Follow Your Own Design Process",
                    "date": "OCTOBER 31, 2022",
                    "description": generate_text(f"Generate just only one description for blogs and article section related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for blogs and article about {user_text}")
                },
                {
                    "title": "Usability Secrets to Create Better Interfaces",
                    "date": "NOVEMBER 28, 2021",
                    "description": generate_text(f"Generate just only one description for blogs and article section related to {user_text}"),
                    "imgUrl": search_image(f"Generate an image URL for blogs and article about {user_text}")
                }
            ]
        },
        "contact": {
            "sectionId": "contact",
            "title": "CONTACT ME",
            "subtitle": "LET'S Talk About Ideas",
            "name": "YOUR FULL NAME *",
            "address": "YOUR EMAIL *",
            "subject": "YOUR SUBJECT *",
            "message": "YOUR MESSAGE *",
            "contacts": [
                {
                    "type": "Address",
                    "address": "North Tower, Toronto, Canada",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
                },
                {
                    "type": "Freelance",
                    "address": "Available Right Now",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
                },
                {
                    "type": "Email",
                    "address": "Zoe.miller@mydomain.com",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
                },
                {
                    "type": "Phone",
                    "address": "+1 900 - 900 - 9000",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
                }
            ],
            "buttonText": "SEND MESSAGE"
        },
        "footer": {
            "sectionId": "footer",
            "title": "Copyright Ⓒ 2022 LUIQUE. ALL RIGHTS RESERVED",
            "subtitle": "DEVELOPED BY BSLTHEMES",
            "medias": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017487/jammal_photos/dov4re8wizaegdj3jiza.svg",
                    "url": "https://x.com/?lang-en="
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017404/jammal_photos/ihzghh1idyxmj1u4vk9r.svg",
                    "url": "https://play.google.com/store/apps/details?id=xyz.be.customer&hl=en_US&pli=1"
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017568/jammal_photos/hpyyah3zyuwxvydg7dnw.png",
                    "url": "https://www.dribble.com/"
                }
            ]
        },
        "colors": {
            "templateColors": ["#1f2937", "#9b650d", "#f0ebe3", "#262626", "#29a587", "#808080"]
        }
    }












# from utils import generate_text, search_image

# def schema_15(user_text):
#     return {
#         "templateInfo": {
#             "id": 15,
#             "title": generate_text(f"Generate a unique name for a website in just 2 words about {user_text}"),
#             "description": generate_text(f"Generate just only one a short description in 10-15 words summarizing what the website about {user_text} offers"),
#             "imgUrl": search_image(f"Find a suitable logo image for a website focused on {user_text}")
#         },
        
#   "navbar": {
#     "links": [
#       {"text": "Home", "url": "#home"},
#       {"text": "About", "url": "#about"},
#       {"text": "Services", "url": "#services"},
#       {"text": "Features", "url": "#features"},
#       {"text": "Projects", "url": "#projects"},
#       {"text": "Testimonials", "url": "#testimonials"},
#       {"text": "Pricing", "url": "#pricing"},
#       {"text": "Blog", "url": "#blog"},
#       {"text": "Contact", "url": "#contact"}
#     ],
#     "logo": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708020289/jammal_photos/yd48mthnmtr9zswrqrms.png"
#   },
#   "hero": {
#     "title": generate_text(f"Generate just only one a compelling main title in 5-7 words for the hero section about {user_text}"),
#     "description": generate_text(f"Generate just only one a brief description in 20-30 words highlighting the key message for the hero section about {user_text}"),
#     "imgUrl": search_image(f"Locate a high-quality hero image related to {user_text} for the website"),
#     "buttonText": "Learn More",
#     "linkText": "About Me"
#   },
#   "services": {
#     "title": "SERVICES",
#     "subtitle": "What I Offer",
#     "services": [
#       {
#         "title":generate_text(f"generate just only title name for a service related to {user_text}"),
#         "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
#         "icon": "https://example.com/icon1.png"
#       },
#       {
#         "title": generate_text(f"Generate a service title related to {user_text}"),
#         "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
#         "icon": "https://example.com/icon2.png"
#       },
#       {
#         "title": generate_text(f"Generate a service title related to {user_text}"),
#         "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
#         "icon": "https://example.com/icon3.png"
#       }
#     ]
#   },
#   "features": {
#     "title": "PROFESSIONAL SKILLS",
#     "subtitle": "My Talent",
#     "features": [
#       {
#         "title": "PHP",
#         "number": "85",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       },
#       {
#         "title": "JavaScript",
#         "number": "65",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       },
#       {
#         "title": "WordPress",
#         "number": "60",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       },
#       {
#         "title": "Python",
#         "number": "50",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       },
#       {
#         "title": "React",
#         "number": "70",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       },
#       {
#         "title": "Adobe XD",
#         "number": "85",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
#       }
#     ]
#   },
#   "projects": {
#     "title": "PORTFOLIO",
#     "subtitle": "My Cases",
#     "buttonText": "See Pricing",
#     "linkText": "VIEW MORE",
#     "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708020289/jammal_photos/yd48mthnmtr9zswrqrms.png",
#     "categories": ["All", "VIDEO", "PHOTOGRAPHY", "BRANDING"],
#     "projects": [
#       {
#         "title": "BRANDING",
#         "subtitle": "Zorro",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       },
#       {
#         "title": "BRANDING",
#         "subtitle": "Gooir",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       },
#       {
#         "title": "VIDEO",
#         "subtitle": "Explore",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       },
#       {
#         "title": "VIDEO",
#         "subtitle": "Stay Fit",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       },
#       {
#         "title": "PHOTOGRAPHY",
#         "subtitle": "Kana",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       },
#       {
#         "title": "PHOTOGRAPHY",
#         "subtitle": "Mozar",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
#       }
#     ]
#   },
#   "cta": {
#     "title": "RESUME",
#     "subtitle": "My Story",
#     "imgs": [
#       "https://res.cloudinary.com/duc04fwdb/image/upload/v1708028064/jammal_photos/dxfncgzlnm5uoeyhugkf.svg",
#       "https://res.cloudinary.com/duc04fwdb/image/upload/v1708027950/jammal_photos/suloncptxwohoete98cr.png"
#     ],
#     "educations": [
#       {
#         "title": "CoderHouse Courses",
#         "subtitle": "Backend Programming",
#         "year": "2014 - 2016",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "education"
#       },
#       {
#         "title": "Lviv National Academy of Arts",
#         "subtitle": "Faculty of Design",
#         "year": "2012 - 2014",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "education"
#       },
#       {
#         "title": "IT Future",
#         "subtitle": "High School",
#         "year": "2010 - 2012",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "education"
#       }
#     ],
#     "experiences": [
#       {
#         "title": "UI Head & Manager",
#         "subtitle": "Soft Tech Inc.",
#         "year": "2020 - 2022",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "experience"
#       },
#       {
#         "title": "UI / UX Specialist",
#         "subtitle": "Kana Design Studio",
#         "year": "2018 - 2020",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "experience"
#       },
#       {
#         "title": "Plugins Developer",
#         "subtitle": "Fiverr.com",
#         "year": "2016 - 2018",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "category": "experience"
#       }
#     ]
#   },
#   "testimonials": {
#     "title": "Testimonials",
#     "subtitle": "WHAT Customers Say",
#     "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#     "testimonials": [
#       {
#         "name": "Barbara Wilson",
#         "subtitle": "CEO Company",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
#       },
#       {
#         "name": "Charlie Smith",
#         "subtitle": "Designer",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
#       },
#       {
#         "name": "Roy Wang",
#         "subtitle": "Manager GYM",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
#       },
#       {
#         "name": "Jennifer Smith",
#         "subtitle": "CEO & Founder",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
#       },
#       {
#         "name": "Paul Freeman",
#         "subtitle": "Photographer",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
#       }
#     ]
#   },
#   "pricing": {
#     "title": "PRICING",
#     "subtitle": "MY Price Board",
#     "plans": [
#       {
#         "title": "HOURLY BASIS",
#         "price": "39",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
#         "timeUnit": "hour",
#         "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
#       },
#       {
#         "title": "FREELANCING",
#         "price": "259",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
#         "timeUnit": "Week",
#         "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
#       },
#       {
#         "title": "FULL TIME",
#         "price": "1.249",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
#         "timeUnit": "Month",
#         "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
#       }
#     ],
#     "buttonText": "START PROJECT",
#     "imgs": [
#       "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030355/jammal_photos/px8o2t9qtet1pumt2yip.svg",
#       "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030465/jammal_photos/capby7kt0b8mwxgzf3hs.png"
#     ]
#   },
#   "blogs": {
#     "title": "LATEST BLOG",
#     "subtitle": "MY Articles and Advice",
#     "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
#     "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030465/jammal_photos/capby7kt0b8mwxgzf3hs.png",
#     "buttonText": "Read more",
#     "linkText": "VIEW BLOG",
#     "blogs": [
#       {
#         "title": "The Main Thing For The Designer",
#         "date": "OCTOBER 31, 2022",
#         "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942658/jammal_photos/lyixvtrnvyazsfa5yuje.jpg"
#       },
#       {
#         "title": "Follow Your Own Design Process",
#         "date": "OCTOBER 31, 2022",
#         "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942696/jammal_photos/yjikp3c1msirossmsu3d.jpg"
#       },
#       {
#         "title": "Usability Secrets to Create Better Interfaces",
#         "date": "NOVEMBER 28, 2021",
#         "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942724/jammal_photos/fiysz2n20varciifews5.jpg"
#       }
#     ]
#   },
#   "contact": {
#     "title": "CONTACT ME",
#     "subtitle": "LET'S Talk About Ideas",
#     "name": "YOUR FULL NAME *",
#     "address": "YOUR EMAIL *",
#     "subject": "YOUR SUBJECT *",
#     "message": "YOUR MESSAGE *",
#     "contacts": [
#       {
#         "type": "Address",
#         "address": "North Tower, Toronto, Canada",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
#       },
#       {
#         "type": "Freelance",
#         "address": "Available Right Now",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
#       },
#       {
#         "type": "Email",
#         "address": "Zoe.miller@mydomain.com",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
#       },
#       {
#         "type": "Phone",
#         "address": "+1 900 - 900 - 9000",
#         "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707946243/jammal_photos/mc5lc3k5hntokrcqgvgq.png"
#       }
#     ],
#     "buttonText": "SEND MESSAGE"
#   },
#   "footer": {
#     "title": "Copyright Ⓒ 2022 LUIQUE . ALL RIGHTS RESERVED",
#     "subtitle": "DEVELOPED BY BSLTHEMES",
#     "medias": [
#       {
#         "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017487/jammal_photos/dov4re8wizaegdj3jiza.svg",
#         "url": "https://x.com/?lang-en="
#       },
#       {
#         "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017404/jammal_photos/ihzghh1idyxmj1u4vk9r.svg",
#         "url": "https://x.com/?lang-en="
#       },
#       {
#         "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017568/jammal_photos/hpyyah3zyuwxvydg7dnw.png",
#         "url": "https://x.com/?lang-en="
#       }
#     ]
#   },
#   "colors": {
#     "templateColors": ["#1f2937", "#9b650d", "#f0ebe3", "#262626", "#29a587","#808080"]
#   }
# }
