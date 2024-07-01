from utils import generate_text, search_image

def schema_2(user_text):
    return {
        "templateInfo": {
            "id": 2,
            "title": generate_text(f"Generate a name for a website about {user_text}"),
            "description": generate_text(f"Generate a brief description for a website about {user_text}"),
            "imgUrl": search_image(f"Generate an image for the main theme of {user_text}")
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
            "title": generate_text(f"Generate a title for the hero section related to {user_text}"),
            "subtitle": generate_text(f"Generate a subtitle for the hero section related to {user_text}"),
            "image": search_image(f"Generate an image for the hero section about {user_text}"),
            "cards": [
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134251/book-svgrepo-com_f62qre.svg",
                    "title": generate_text(f"Generate a title for the first hero card related to {user_text}"),
                    "content": generate_text(f"Generate content for the first hero card related to {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/users-svgrepo-com_acna7b.svg",
                    "title": generate_text(f"Generate a title for the second hero card related to {user_text}"),
                    "content": generate_text(f"Generate content for the second hero card related to {user_text}")
                },
                {
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134396/project-svgrepo-com_qjvqow.svg",
                    "title": generate_text(f"Generate a title for the third hero card related to {user_text}"),
                    "content": generate_text(f"Generate content for the third hero card related to {user_text}")
                }
            ],
            "description": generate_text(f"Generate a brief description for the hero section about {user_text}")
        },
        "testimonials": {
            "title": "What the People Think About Us",
            "subtitle": generate_text(f"Generate a subtitle for the testimonials section related to {user_text}"),
            "cards": [
                {
                    "avatar": search_image(f"Generate a portrait image for the first client testimonial related to {user_text}"),
                    "name": generate_text(f"Generate a name for the first client testimonial related to {user_text}"),
                    "review": generate_text(f"Generate a review for the first client testimonial related to {user_text}")
                },
                {
                    "avatar": search_image(f"Generate a portrait image for the second client testimonial related to {user_text}"),
                    "name": generate_text(f"Generate a name for the second client testimonial related to {user_text}"),
                    "review": generate_text(f"Generate a review for the second client testimonial related to {user_text}")
                },
                {
                    "avatar": search_image(f"Generate a portrait image for the third client testimonial related to {user_text}"),
                    "name": generate_text(f"Generate a name for the third client testimonial related to {user_text}"),
                    "review": generate_text(f"Generate a review for the third client testimonial related to {user_text}")
                },
                {
                    "avatar": search_image(f"Generate a portrait image for the fourth client testimonial related to {user_text}"),
                    "name": generate_text(f"Generate a name for the fourth client testimonial related to {user_text}"),
                    "review": generate_text(f"Generate a review for the fourth client testimonial related to {user_text}")
                }
            ]
        },
        "projects": {
            "cards": [
                {
                    "image": search_image(f"Generate an image for the first project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the first project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Generate an image for the second project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the second project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Generate an image for the third project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the third project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Generate an image for the fourth project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the fourth project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Generate an image for the fifth project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the fifth project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                },
                {
                    "image": search_image(f"Generate an image for the sixth project related to {user_text}"),
                    "title": generate_text(f"Generate a title for the sixth project related to {user_text}"),
                    "githubLink": "https://github.com",
                    "demoLink": "https://dribbble.com/Alien_pixels"
                }
            ]
        },
        "contact": {
            "title": generate_text(f"Generate a title for the contact section related to {user_text}"),
            "subtitle": generate_text(f"Generate a subtitle for the contact section related to {user_text}"),
            "options": [
                {
                    "title": "Email",
                    "subtitle": generate_text(f"Generate a brief email subtitle related to {user_text}"),
                    "link": "mailto:ahmed.solimanth57@gmail.com",
                    "logo": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/gmail-svgrepo-com_xppy7f.svg"
                },
                {
                    "title": "Messenger",
                    "subtitle": generate_text(f"Generate a brief Messenger subtitle related to {user_text}"),
                    "link": "https://m.me/ahmed.soliman.3591267",
                    "logo": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703134252/facebook-svgrepo-com_lmghnk.svg"
                },
                {
                    "title": "WhatsApp",
                    "subtitle": generate_text(f"Generate a brief WhatsApp subtitle related to {user_text}"),
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
            "title": generate_text(f"Generate a title for the services section related to {user_text}"),
            "subtitle": generate_text(f"Generate a subtitle for the services section related to {user_text}"),
            "services": [
                {
                    "title": generate_text(f"Generate a title for the first service related to {user_text}"),
                    "description": generate_text(f"Generate a description for the first service related to {user_text}")
                },
                {
                    "title": generate_text(f"Generate a title for the second service related to {user_text}"),
                    "description": generate_text(f"Generate a description for the second service related to {user_text}")
                },
                {
                    "title": generate_text(f"Generate a title for the third service related to {user_text}"),
                    "description": generate_text(f"Generate a description for the third service related to {user_text}")
                }
            ]
        }
    }
