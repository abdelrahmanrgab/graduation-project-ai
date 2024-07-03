from utils import generate_text, search_image  

def schema_2(user_text):
    return {
        "templateInfo": {
            "id": 2,
            "title": generate_text(f"Generate a name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"Create a brief description for a website in just 20 words about {user_text}"),
            "imgUrl": search_image(f"Find an image link to be used as a logo for a website about {user_text}"),
            "ahmed": "ahmed"
        },
        "navbar": [
            {
                "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/home-1-svgrepo-com_axgckp.svg",
                "url": "hero2"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134253/info-circle-svgrepo-com_a6q6z3.svg",
                "url": "services2"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/project-svgrepo-com_qjvqow.svg",
                "url": "projects2"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/customer-testimonial-svgrepo-com_vdnnre.svg",
                "url": "testimonials2"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134254/message-circle-lines-alt-svgrepo-com_iotcwk.svg",
                "url": "contactUs2"
            }
        ],
        "hero": {
            "title": generate_text(f"Generate a title for this website in just 5 words about {user_text}"),
            "subtitle": generate_text(f"Generate a subtitle for this website in just 5 words about {user_text}"),
            "imgUrl": search_image(f"Find an image link to be used as wallpaper for a website about {user_text}"),
            "heros": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/book-svgrepo-com_f62qre.svg",
                    "title": generate_text(f"Generate a title name for a card related to {user_text}"),
                    "description": generate_text(f"Create a brief description in 15 words for a card related to {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/users-svgrepo-com_acna7b.svg",
                    "title": generate_text(f"Generate a title name for a card related to {user_text}"),
                    "description": generate_text(f"Create a brief description in 15 words for a card related to {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/project-svgrepo-com_qjvqow.svg",
                    "title": generate_text(f"Generate a title name for a card related to {user_text}"),
                    "description": generate_text(f"Create a brief description in 15 words for a card related to {user_text}")
                }
            ]
        },
        "testimonials": {
            "title": "What the People Think About Us",
            "subtitle": generate_text(f"Generate a subtitle in 5 words for testimonials related to {user_text}"),
            "testimonials": [
                {
                    "imgUrl": search_image("Portrait of a client"),
                    "name": generate_text(f"Generate a name in 2 words"),
                    "opinion": generate_text(f"Generate a brief description in 10 to 15 words for a client who used our services about {user_text}")
                },
                {
                    "imgUrl": search_image("Portrait of a client"),
                    "name": generate_text(f"Generate a name in 2 words"),
                    "opinion": generate_text(f"Generate a brief description in 10 to 15 words for a client who used our services about {user_text}")
                },
                {
                    "imgUrl": search_image("Portrait of a client"),
                    "name": generate_text(f"Generate a name in 2 words"),
                    "opinion": generate_text(f"Generate a brief description in 10 to 15 words for a client who used our services about {user_text}")
                },
                {
                    "imgUrl": search_image("Portrait of a client"),
                    "name": generate_text(f"Generate a name in 2 words"),
                    "opinion": generate_text(f"Generate a brief description in 10 to 15 words for a client who used our services about {user_text}")
                }
            ]
        },
        "projects": {
            "title": "My Recent Work",
            "description": "Projects",
            "projects": [
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                },
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                },
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                },
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                },
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                },
                {
                    "imgUrl": search_image(f"Find an image to describe {user_text} as a project"),
                    "title": generate_text(f"Generate a title name for a project related to {user_text}"),
                    "url": "https://github.com",
                    "link": "https://dribbble.com/Alien_pixels"
                }
            ]
        },
        "contact": {
            "title": generate_text(f"Generate a title in 5 words for contact section related to {user_text}"),
            "description": generate_text(f"Generate a subtitle in 10 words for contact section related to {user_text}"),
            "contacts": [
                {
                    "type": "email",
                    "title": generate_text(f"Generate a subtitle in 5 words for email contact related to {user_text}"),
                    "email": "mailto:ahmed.solimanth57@gmail.com",
                    "buttonText": "Connect",
                    "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/gmail-svgrepo-com_xppy7f.svg"
                },
                {
                    "type": "facebook",
                    "title": generate_text(f"Generate a subtitle in 5 words for Messenger contact related to {user_text}"),
                    "email": "mailto:ahmed.solimanth57@gmail.com",
                    "buttonText": "Connect",
                    "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/facebook-svgrepo-com_lmghnk.svg"
                },
                {
                    "type": "whatsapp",
                    "title": generate_text(f"Generate a subtitle in 5 words for WhatsApp contact related to {user_text}"),
                    "email": "mailto:ahmed.solimanth57@gmail.com",
                    "buttonText": "Connect",
                    "imgUrl": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134203/whatsapp-whats-app-svgrepo-com_ug4dbt.svg"
                }
            ],
            "buttonText": "Send",
            "linkText": "Send Message"
        },
        "services": {
            "title": "What We Offer",
            "description": "Services",
            "services": [
                {
                    "title": "UI/UX Design",
                    "items": ["lorem ipsum,", "Llorem ipsuma,", "Blorem ipsumm,", "Dilorem ipsumll,", "lorem ipsum"],
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/correct-signal-svgrepo-com_vvf3sw.svg"
                },
                {
                    "title": "Web Development",
                    "items": ["lorem ipsum,", "Llorem ipsuma,", "Blorem ipsumm,", "Dilorem ipsumll,", "lorem ipsum"],
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/correct-signal-svgrepo-com_vvf3sw.svg"
                },
                {
                    "title": "Content Creation",
                    "items": ["lorem ipsum,", "Llorem ipsuma,", "Blorem ipsumm,", "Dilorem ipsumll,", "lorem ipsum"],
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/correct-signal-svgrepo-com_vvf3sw.svg"
                }
            ]
        },
        "footer": {
            "title": "CSE",
            "description": "ssssssssssssssssssssss all rights reserved.",
            "footerSections": [
                { "title": "Home", "url": "#hero2" },
                { "title": "Services", "url": "#services2" },
                { "title": "Testimonials", "url": "#testimonials2" },
                { "title": "Contact", "url": "#contactUs2" }
            ],
            "medias": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703129090/icons8-facebook-50_xfbimo.png",
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
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703129090/icons8-facebook-50_xfbimo.png",
                    "url": "https://facebook.com"
                }
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }

