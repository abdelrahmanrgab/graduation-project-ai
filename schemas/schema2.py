from utils import generate_text, search_image

def schema_2(user_text):
    return {
        "templateInfo": {
            "id": 2,
            "title": generate_text(f"Generate a short name for a website about {user_text}"),
            "description": generate_text(f"Provide a brief description for a website about {user_text} in 15 words"),
            "imgUrl": search_image(f"Main theme image for {user_text}")
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
            "title": generate_text(f"Hero section title about {user_text} in 5 words"),
            "subtitle": generate_text(f"Subtitle for the hero section about {user_text} in 10 words"),
            "image": search_image(f"Hero section image for {user_text}"),
            "cards": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/book-svgrepo-com_f62qre.svg",
                    "title": generate_text(f"First hero card title about {user_text} in 3 words"),
                    "content": generate_text(f"First hero card content about {user_text} in 10 words")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/users-svgrepo-com_acna7b.svg",
                    "title": generate_text(f"Second hero card title about {user_text} in 3 words"),
                    "content": generate_text(f"Second hero card content about {user_text} in 10 words")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/project-svgrepo-com_qjvqow.svg",
                    "title": generate_text(f"Third hero card title about {user_text} in 3 words"),
                    "content": generate_text(f"Third hero card content about {user_text} in 10 words")
                }
            ],
            "description": generate_text(f"Brief description for the hero section about {user_text} in 20 words")
        },
        "testimonials": {
            "title": "What the People Think About Us",
            "subtitle": generate_text(f"Subtitle for the testimonials section about {user_text} in 10 words"),
            "cards": [
                {
                    "avatar": search_image(f"First client testimonial portrait for {user_text}"),
                    "name": generate_text(f"First client testimonial name for {user_text}"),
                    "review": generate_text(f"First client testimonial review for {user_text} in 20 words")
                },
                {
                    "avatar": search_image(f"Second client testimonial portrait for {user_text}"),
                    "name": generate_text(f"Second client testimonial name for {user_text}"),
                    "review": generate_text(f"Second client testimonial review for {user_text} in 20 words")
                },
                {
                    "avatar": search_image(f"Third client testimonial portrait for {user_text}"),
                    "name": generate_text(f"Third client testimonial name for {user_text}"),
                    "review": generate_text(f"Third client testimonial review for {user_text} in 20 words")
                },
                {
                    "avatar": search_image(f"Fourth client testimonial portrait for {user_text}"),
                    "name": generate_text(f"Fourth client testimonial name for {user_text}"),
                    "review": generate_text(f"Fourth client testimonial review for {user_text} in 20 words")
                }
            ]
        },
        "projects": {
            "cards": [
                {
                    "image": search_image(f"First project image for {user_text}"),
                    "title": generate_text(f"First project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Second project image for {user_text}"),
                    "title": generate_text(f"Second project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Third project image for {user_text}"),
                    "title": generate_text(f"Third project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Fourth project image for {user_text}"),
                    "title": generate_text(f"Fourth project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Fifth project image for {user_text}"),
                    "title": generate_text(f"Fifth project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Sixth project image for {user_text}"),
                    "title": generate_text(f"Sixth project title for {user_text} in 5 words"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                }
            ]
        },
        "contact": {
            "title": generate_text(f"Contact section title for {user_text} in 5 words"),
            "subtitle": generate_text(f"Contact section subtitle for {user_text} in 10 words"),
            "options": [
                {
                    "title": "Email",
                    "subtitle": generate_text(f"Brief email subtitle for {user_text} in 10 words"),
                    "link": "mailto:ahmed.solimanth57@gmail.com",
                    "logo": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/gmail-svgrepo-com_xppy7f.svg"
                },
                {
                    "title": "Messenger",
                    "subtitle": generate_text(f"Brief Messenger subtitle for {user_text} in 10 words"),
                    "link": "https://m.me/ahmed.soliman.3591267",
                    "logo": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/facebook-svgrepo-com_lmghnk.svg"
                },
                {
                    "title": "WhatsApp",
                    "subtitle": generate_text(f"Brief WhatsApp subtitle for {user_text} in 10 words"),
                    "link": "https://wa.me/1234567890",
                    "logo": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134203/whatsapp-whats-app-svgrepo-com_ug4dbt.svg"
                }
            ],
            "send": {
                "title": "Send",
                "action": "sendEmail"
            },
            "sendMessage": {
                "title": "Send a message",
                "action": "sendWhatsAppMessage"
            }
        },
        "services": {
            "title": generate_text(f"Services section title for {user_text} in 5 words"),
            "subtitle": generate_text(f"Services section subtitle for {user_text} in 10 words"),
            "services": [
                {
                    "title": generate_text(f"First service title for {user_text} in 5 words"),
                    "description": generate_text(f"First service description for {user_text} in 15 words")
                },
                {
                    "title": generate_text(f"Second service title for {user_text} in 5 words"),
                    "description": generate_text(f"Second service description for {user_text} in 15 words")
                },
                {
                    "title": generate_text(f"Third service title for {user_text} in 5 words"),
                    "description": generate_text(f"Third service description for {user_text} in 15 words")
                }
            ]
        }
    }

