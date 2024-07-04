from utils import generate_text, search_image

def schema_14(user_text):
    return {
        "templateInfo": {
            "id": 14,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        "navbar": {
            "title": generate_text(f"generate title for the navbar of a website about {user_text}"),
            "links": [
                {
                    "title": "Home",
                    "url": "#"
                },
                {
                    "title": "Pages",
                    "url": "#"
                },
                {
                    "title": "Services",
                    "url": "#"
                },
                {
                    "title": "Projects",
                    "url": "#"
                },
                {
                    "title": "Blog",
                    "url": "#"
                },
                {
                    "title": "Contact",
                    "url": "#"
                }
            ],
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701811960/templates/template_one/Logo_mj7rvw.png",
            "icons": [
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
                "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg"
            ]
        },
        "hero": {
            "heros": [
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602286/headphone_qbcak3.png",
                    "subtitle": "Beats Solo",
                    "title": "Wireless",
                    "description": "Headphone"
                }
            ],
            "buttonText": "Get Started"
        },
        "items": {
            "title": "Enjoy",
            "subtitle": "With",
            "items": [
                {
                    "title":"Earph",
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777277/earphone_pgistv.png"
                },
                {
                    "title": "Gadget",
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777305/watch_dn63md.png"
                }
            ],
            "buttonText": "Browse"
        },
        "services": {
            "services": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_one_xvd7d6.svg",
                    "title": "Free Shipping",
                    "description": "Free Shipping On All Order"
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808099/templates/template_one/icon_two_dptua1.svg",
                    "title":  "Safe Money ",
                    "description":  "30 Days Money Back"
                }
            ]
        },
        "features": {
            "discount": "30% OFF",
            "title": "Fine Smile",
            "date": "10 Jan to 28 Jan",
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707603385/headphone_pkjxnj.png",
            "subtitle": "Air Solo Bass",
            "text": "Winter Sale",
            "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque reiciendis",
            "buttonText": "Shop Now"
        },
        "projects": {
            "title": "Our Projects",
            "description": "Explore Our Projects",
            "projects": [
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604733/p-1_mqzmix.jpg",
                    "title": "Boat Headphone",
                    "price": "120"
                },
                {
                       "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604737/p-2_qc3prb.jpg",
                       "title": "Rocky Mountain",
                       "price": "420"
                               }
            ],
            "buttonText": "Add to cart"
        },
        "blogs": {
            "title": "Recent News",
            "description": "Explore Our Blogs",
            "blogs": [
                {
                    "title": "Recent News",
                    "subtitle": generate_text(f"Generate a blog subtitle related to {user_text}"),
                    "description": "Jan 20, 2024",
                    "imgUrl": search_image(f"I need an image for a blog related to {user_text}")
                },
                {
                    "title": "How to choose perfect smartwatch",
                    "subtitle": generate_text(f"Generate another blog subtitle related to {user_text}"),
                    "description": "Jan 22, 2024",
                    "imgUrl": search_image(f"I need another image for a blog related to {user_text}")
                }
            ]
        },
        "logos": {
            "companies": [
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/01_p78hjd.svg",
                    "url": "https://example.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808448/templates/template_one/02_mnw1ps.svg",
                    "url": "https://example.com"
                }
            ]
        },
        "footer": {
            "title":"Eshop",
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701808855/templates/template_one/Photo_fz8cuc.jpg",
            "description": generate_text(f"Generate a brief description for the footer about {user_text}"),
            "medias": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/facebook_td263x.svg",
                    "url": "https://facebook.com"
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/x_yp3y5n.svg",
                    "url": "https://x.com"
                }
            ],
            "footerSections": [
                {
                    "title": "Important Links",
                    "links": [
                        {
                            "title": "Home",
                            "url": "#home"
                        },
                        {
                            "title": "About",
                            "url": "#about"
                        }
                    ]
                },
                {
                    "title": "Quick Links",
                    "links": [
                        {
                            "title": "Contact",
                            "url": "#contact"
                        },
                        {
                            "title": "Blog",
                            "url": "#blog"
                        }
                    ]
                }
            ]
        },
         "contacts": [
            {
                "value": "Noida, Uttar Pradesh",
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1709831446/icons8-location-24_qiw7so.png"
            },
            {
                "value": "+20 123456789",
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707781365/icons8-mobile-navigator-50_xvqski.png"
            }
        ],
        "colors": {
            "templateColors": ["#f42c37", "#fdc62e", "#34cc73", "#1376f4", "#acabab9c", "#eeeeee"]
        }
    }
