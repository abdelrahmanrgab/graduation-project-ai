from utils import generate_text, search_image

def schema_18(user_text):
    return {
        "templateInfo": {
            "id": 18,
            "title": generate_text(f"Generate a two-word name for a website about {user_text}"),
            "description": "",
            "imgUrl": ""
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
            ],
            "icons": [
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708092466/icons8-sun-24_oonunj.png",
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708092459/icons8-moon-symbol-30_chxqrj.png",
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708092472/icons8-menu-32_ixhdzw.png"
            ]
        },
        "hero": {
            "title": generate_text(f"Generate a five-word title for a website about {user_text}"),
            "description": generate_text(f"Create a brief description (up to 20 words) for a website about {user_text}"),
            "buttonText": "Get Started",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"Image for the homepage of a website about {user_text}")
        },
        "features": {
            "title": "About us",
            "subtitle": generate_text(f"Generate a subtitle (up to 25 words) for a website about {user_text}"),
            "description": generate_text(f"Create a brief description (up to 30 words) for the features of a website about {user_text}"),
            "buttonText": "Get Started",
            "imgUrl": search_image(f"Image to represent features of a website about {user_text}")
        },
        "services": {
            "title": "Why Choose Us",
            "services": [
                {
                    "title": generate_text(f"Generate a service title related to {user_text}"),
                    "description": generate_text(f"Create a brief description (up to 15 words) for a service related to {user_text}"),
                    "buttonText": "Learn more",
                    "linkText": "#",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708095320/icons8-compact-camera-24_sbvw3e.png"
                },
                {
                    "title": generate_text(f"Generate a service title related to {user_text}"),
                    "description": generate_text(f"Create a brief description (up to 15 words) for a service related to {user_text}"),
                    "buttonText": "Learn more",
                    "linkText": "#",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708095302/icons8-notebook-32_wp5emo.png"
                },
                {
                    "title": generate_text(f"Generate a service title related to {user_text}"),
                    "description": generate_text(f"Create a brief description (up to 15 words) for a service related to {user_text}"),
                    "buttonText": "Learn more",
                    "linkText": "#",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708095310/icons8-microsoft-onenote-24_jrkmre.png"
                }
            ]
        },
        "projects": {
            "title": generate_text(f"Generate a project title for a website about {user_text}"),
            "description": generate_text(f"Create a brief description (up to 25 words) for the projects section of a website about {user_text}"),
            "projects": [
                {
                    "title": "BMW UX",
                    "price": "$100/Day",
                    "space": "12Km",
                    "buttonText": "Details",
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708097455/white-car_vfl2mw.png"
                },
                {
                    "title": "KIA UX",
                    "price": "$140/Day",
                    "space": "12Km",
                    "buttonText": "Details",
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708097459/car5_gini6n.png"
                },
                {
                    "title": "BMW UX",
                    "price": "$100/Day",
                    "space": "12Km",
                    "buttonText": "Details",
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708097461/car6_ohp1ia.png"
                }
            ],
            "buttonText": "Get Started"
        },
        "testimonials": {
            "title": "What Our Clients Say About Us",
            "description": generate_text(f"Generate a brief description (up to 20 words) for the testimonials section of a website about {user_text}"),
            "testimonials": [
                {
                    "name": "Dilshad",
                    "star": "⭐⭐⭐⭐⭐",
                    "description": generate_text(f"Generate a brief testimonial (10-15 words) from a client who used our services for {user_text}"),
                    "imgUrl": "https://picsum.photos/200.jpg"
                },
                {
                    "name": "Satya",
                    "star": "⭐⭐⭐⭐⭐",
                    "description": generate_text(f"Generate a brief testimonial (10-15 words) from a client who used our services for {user_text}"),
                    "imgUrl": "https://picsum.photos/200.jpg"
                },
                {
                    "name": "Sabir",
                    "star": "⭐⭐⭐⭐⭐",
                    "description": generate_text(f"Generate a brief testimonial (10-15 words) from a client who used our services for {user_text}"),
                    "imgUrl": "https://picsum.photos/200.jpg"
                }
            ]
        },
        "cta": {
            "title": "Get Started with our app",
            "description": generate_text(f"Generate a brief description (up to 30 words) for a call-to-action related to {user_text}"),
            "imgs": [
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1708098410/pattern_t0naia.jpg",
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707090485/app_store_s6wzhh.png",
                "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707090481/play_store_nmzfln.png"
            ]
        },
        "contact": {
            "title": "Let's collaborate on your upcoming car rental venture",
            "description": generate_text(f"Generate a brief description (up to 20 words) for a contact section about {user_text}"),
            "buttonText": "Contact",
            "linkText": "#"
        },
        "footer": {
            "title": "Car Rental",
            "description": generate_text(f"Generate a brief description (up to 30 words) for the footer section of a website about {user_text}"),
            "contacts": [
                {
                    "value": "55 East Birchwood Ave. Brooklyn, New York 11201",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707781362/icons8-location-arrow-24_mwjabu.png"
                },
                {
                    "value": "(123) 125-858",
                    "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707781365/icons8-mobile-navigator-50_xvqski.png"
                }
            ],
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
                }
            ],
            "footerSections": [
                {
                    "title": "Important Links",
                    "links": [
                        {"title": "Home", "url": "#"},
                        {"title": "About", "url": "#"},
                        {"title": "Contact", "url": "#"},
                        {"title": "Blog", "url": "#"}
                    ]
                },
                {
                    "title": "Links",
                    "links": [
                        {"title": "Home", "url": "#"},
                        {"title": "About", "url": "#"},
                        {"title": "Contact", "url": "#"},
                        {"title": "Blog", "url": "#"}
                    ]
                },
                {
                    "title": "location",
                    "links": [
                        {"title": "Home", "url": "#"},
                        {"title": "About", "url": "#"},
                        {"title": "Contact", "url": "#"},
                        {"title": "Blog", "url": "#"}
                    ]
                }
            ]
        },
        "colors": {
            "templateColors": ["#ffc727", "#fad46d", "#E2E2D5", "#888883", "#111111"]
        }
    }
