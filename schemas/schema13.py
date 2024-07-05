from utils import generate_text, search_image

def schema_13(user_text):
    return {
        "templateInfo": {
            "id": 13,
            "title": generate_text(f"Generate a website name in 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707951170/lighting_o2dsku.png",
            "title": "Soliii",
            "subtitle": "Contact us",
            "links": [
                {"title": "Design", "url": "#about13"},
                {"title": "About us", "url": "#"},
                {"title": "Projects", "url": "#"},
                {"title": "Contact team", "url": "#"},
                {"title": "Reviews", "url": "#testimonials13"}
            ],
            "icons": [
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707951170/menu-bar_q4qwbp.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707346109/realestate/next_2989988_stvovd.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707347076/icons8-close_ozpkst.svg"
            ]
        },
        "hero": {
            "title": "Architects with different approach",
            "description":  "Architecture is the art & technique of designing and building, as distinguished from the skills",
            "buttons": [
                {"buttonText": "View projects", "url": "#projects13"},
                {"buttonText": "Our Services", "url": "#services13"}
            ],
            "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707937284/3_tx6g05.jpg",
            "imageUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707937130/4_rjddpl.jpg",
            "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707952901/right-arrow_1_y7iz2i.png"
        },
        "feature": {
            "title": "welcome to lighting",
            "subtitle": "The Art Of ARCHITECTURE ",
            "description": "you will meet your taste",
            "features": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707959654/tree_qh0bvu.png",
                    "title": generate_text(f"Generate a feature title for an icon about {user_text}"),
                    "description": generate_text(f"Generate a feature description for an icon about {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707959653/holding-hand_1_ip0t5r.png",
                    "title": generate_text(f"Generate a feature title for an icon about {user_text}"),
                    "description": generate_text(f"Generate a feature description for an icon about {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707601512/star_qhtqlz.png",
                    "title": generate_text(f"Generate a feature title for an icon about {user_text}"),
                    "description": generate_text(f"Generate a feature description for an icon about {user_text}")
                }
            ]
        },
        "about": {
            "title":"Welcome to our company",
            "subtitle": "our JOURNEY",
            "text": "since 2010",
            "description": generate_text(f"Generate a description for 'About Us' in 20 words about {user_text}"),
            "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707937162/5_ookc7e.jpg",
            "abouts": [
                {"title": "Years of experience", "value": 10},
                {"title": "Projects done", "value": 50},
                {"title": "Awards gained", "value": 20}
            ],
            "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707959810/up-arrow_dfq1o8.png",
            "buttons": [
                {"buttonText": "Get started", "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707952901/right-arrow_1_y7iz2i.png", "url": "#contact13"},
                {"buttonText": "Learn more", "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707952901/right-arrow_1_y7iz2i.png", "url": "#feature13"}
            ]
        },
        "projects": {
            "title": "Our recent works",
            "subtitle": "Our completed projects",
            "description":"Our completed projects",
            "buttonText": "Load more",
            "linkText": "#",
            "projects": [
                {
                    "imgUrl": search_image(f"I need an image for a project about {user_text}"),
                    "title": generate_text(f"Generate a title for a project about {user_text}"),
                    "description": "New Cairo",
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707553370/klipartz.com_z2zhsv.png"
                },
                {
                    "imgUrl": search_image(f"I need another image for a project about {user_text}"),
                    "title": generate_text(f"Generate another title for a project about {user_text}"),
                    "description": "Luxor",
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707553370/klipartz.com_z2zhsv.png"
                }
            ],
            "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707553370/klipartz.com_z2zhsv.png"
        },
        "contact": {
            "title": "Subscribe to our newsletter",
            "subtitle": "Get our e-mail updates about our latest shops and special offers.",
            "description": "Newsletter",
            "buttonText": "Register now",
            "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707952901/right-arrow_1_y7iz2i.png"
        },
        "logos": {
            "companies": [
                {"imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707329688/realestate/logo6_ddaq6y.png", "title":"lighting"},
                {"imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707329687/realestate/logo3_fzmko0.png", "title":"lighting"},
                {"imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707975425/icons8-bird-64_kofuu5.png", "title": "lighting"},
                {"imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707329685/realestate/logo2_z1jb8d.png", "title":"lighting"},
                {"imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703129091/icons8-stars-50_o1lg9s.png", "title": "lighting"}
            ]
        },
        "testimonials": {
            "title": "What our  ",
            "subtitle":"Clients",
            "description":"say's",
            "testimonials": [
                {
                    "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134020/avatar3_pbztwn.jpg",
                    "name": "ahmed",
                    "location": "CEO at AST",
                    "opinion": "We would like to take the opportunity to express our delights with the ways things are progressing."
                },
                {
                    "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134020/avatar3_pbztwn.jpg",
                    "name": "ahmed",
                    "location": "CEO at AST",
                    "opinion": "We would like to take the opportunity to express our delights with the ways things are progressing."
                }
            ],
            "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707952901/right-arrow_1_y7iz2i.png"
        },
        "footer": {
            "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707938679/lightning_h1zfze.png",
            "description": "Architecture with understanding people minds",
            "medias": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134255/meta-logo-facebook-svgrepo-com_zom99z.svg",
                    "url": "https://facebook.com"
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707987495/icons8-twitterx-50_1_ggrau2.png",
                    "url": "https://twitter.com"
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134254/linkedin-svgrepo-com_dpxquk.svg",
                    "url": "https://linkedin.com"
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134255/socialmedia-svgrepo-com_na36wp.svg",
                    "url": "https://instagram.com"
                }
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
                        {"title": "Home", "url": "#"},
                        {"title": "Projects", "url": "#"},
                        {"title": "Design", "url": "#"},
                        {"title": "Follow", "url": "#"},
                        {"title": "Award", "url": "#"}
                    ]
                }
            ],
            "contacts": [
                {"value": 55},
                {"value": 14},
                {"value": 141}
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }
