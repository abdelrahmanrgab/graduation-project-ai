from utils import generate_text, search_image

def schema_17(user_text):
    return {
        "templateInfo": {
            "id": 17,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
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
        "about": {
            "title": "About Us",
            "subtitle": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi itaque aperiam in doloribus corporis quasi quia praesentium deserunt dolor at ducimus accusamus alias magnam tenetur voluptatem, atque qui iusto nesciunt?",
            "imgs": [
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989609/polygon_yiwc6q.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989607/vector-wave_gperhf.png"
            ],
            "buttonText": "My Account",
            "buttonIcon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1707347076/icons8-person-64_ppr9e8.png"
        },
        "features": {
            "title": "Tastes difference and healthy.",
            "subtitle": "That time is the greatest value in the modern world . our healthy meal plan delivery service good food in cairo is the answer for those who want to eat healthy and save time and money .",
            "description": "We Know That time is the greatest value in the modern world . our healthy meal plan delivery service good food in cairo is the answer for those who want to eat healthy and save time and money .",
            "imgs": [
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989602/apple_cyue6o.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989602/kiwi_oenfrv.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989612/lemon_xp4xcd.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989612/leaf_ik3yan.png",
                "https://res.cloudinary.com/dowtlcpxj/image/upload/v1710989607/tomato_wxdrmr.png"
            ]
        },
        "footer": {
            "title": "Contact Us",
            "description": "Copyright © 2024 slolGoodFood. All Rights Reserved.",
            "contacts": [
                {
                    "title": "20, Al-Mahalla Street",
                    "value": 53456789,
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1711080161/location_535239_clqbiz.png"
                },
                {
                    "title": "mkmk@goodFood.com",
                    "value": 2123456789,
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703129088/icons8-gmail-50_u4sqv0.png"
                },
                {
                    "title": "+20123456789 - Sales and Services",
                    "value": 123456789,
                    "icon": "https://res.cloudinary.com/dowtlcpxj/image/upload/v1703129088/icons8-whatsapp-50_knru7l.png"
                }
            ]
        },
        "colors": {
            "templateColors": ["#fff", "#cda274", "#292f36", "#f4f0ec", "#777777"]
        }
    }
