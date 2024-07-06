from utils import generate_text, search_image

def schema_14(user_text):
    return {
        "templateInfo": {
            "id": 14,
            "title": generate_text(f"generate only name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"generate just only one a description for a website in just 10 words about {user_text}"),
            "imgUrl": search_image(f"generate an image URL for a website about {user_text}")
        },
        "navbar": {
            "title": generate_text(f"generate title for the navbar of a website about {user_text}"),
            "links": [
              {
                    "title": "Home",
                    "url": "#"
                },
                {
                    "title": "Shop",
                    "url": "#"
                },
                {
                    "title": "About",
                    "url": "#"
                },
                {
                    "title": "Blogs",
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
                    "imgUrl": search_image(f"generate an image URL for a website hero section about {user_text}"),
                    "subtitle": "Beats Solo",
                    "title":generate_text(f"generate just only one  name for a website hero title in just 2 words about {user_text}"),
                    "description": generate_text(f"generate just only one a description for a website hero section in just 10 words about {user_text}")
                },
                {
                    "imgUrl": search_image(f"generate an image URL for a website hero section about {user_text}"),
                    "subtitle": "Beats Solo",
                    "title": generate_text(f"generate just only one  name for a website hero title in just 2 words about {user_text}"),
                    "description": generate_text(f"generate just only one a description for a website hero section in just 10 words about {user_text}")
                },
                {
                    "imgUrl": search_image(f"generate an image URL for a website hero section about {user_text}"),
                    "subtitle": "Beats Solo",
                    "title": generate_text(f"generate just only one  name for a website hero title in just 2 words about {user_text}"),
                    "description": generate_text(f"generate just only one a description for a website hero section in just 10 words about {user_text}")
                }
                ],
                "buttonText": "Shop By Category"
        },
        "items": {
            "title": "Enjoy",
            "subtitle": "With",
            "items": [
           {
                "title": "Earph",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777277/earphone_pgistv.png"
            },
            {
                "title": "Gadget",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777305/watch_dn63md.png"
            },
            {
                "title": "Laptop",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602295/macbook_dxcdn8.png"
            },
            {
                "title": "Laptop",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777316/gaming_zceuxk.png"
            },
            {
                "title": "Gadget",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602303/vr_zzinjy.png"
            },
            {
                "title": "Earph",
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707777323/speaker_wqwmry.png"
            }
            ],
            "buttonText": "Browse"
        },
        "services": {
            "services": [
             {
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602721/icons8-sedan-30_zecew1.png",
                "title": "Free Shipping",
                "description": "Free Shipping On All Order"
            },
            {
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602913/icons8-checkmark-64_kxv4x8.png",
                "title": "Safe Money ",
                "description": "30 Days Money Back"
            },
            {
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707602989/icons8-wallet-30_prjgk8.png",
                "title": "Secure Payment",
                "description": "All Payment Secure"
            },
            {
                "icon": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707603085/icons8-headphones-30_xandnm.png",
                "title": "Online Supoort 24/7",
                "description": "Technical Support 24/7"
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
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604741/p-3_gfoj4a.jpg",
                "title": "Goggles",
                "price": "320"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604745/p-4_hkawqn.jpg",
                "title": "Printed ",
                "price": "220"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604748/p-5_lbyuxu.jpg",
                "title": "Boat Headphone",
                "price": "120"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604761/p-7_fkl1tb.jpg",
                "title": "Rocky Mountain",
                "price": "420"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604765/p-9_bypahb.jpg",
                "title": "Goggles",
                "price": "320"
            },
            {
                "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604748/p-5_lbyuxu.jpg",
                "title": "Printed ",
                "price": "220"
            }
            ],
            "buttonText": "Add to cart"
        },
        "blogs": {
            "title": "Recent News",
            "description": "Explore Our Blogs",
            "blogs": [
               {
            "title": "How to choose perfect smartwatch",
            "subtitle": "minima facere deserunt vero illo beatae deleniti eius dolores consequuntur, eligendi corporis maiores molestiae Porro?",
            "description": "Jan 20, 2024 by Dilshad",
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604612/blog-1_n5jvci.jpg"
        },
        {
            "title": "How to choose perfect gadget",
            "subtitle": "minima facere deserunt vero illo beatae deleniti eius dolores consequuntur, eligendi corporis maiores molestiae Porro?",
            "description": "Jan 20, 2024 by Satya",
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604616/blog-2_nmxkbb.jpg"
        },
        {
            "title": "How to choose perfect VR headset",
            "subtitle": "minima facere deserunt vero illo beatae deleniti eius dolores consequuntur, eligendi corporis maiores molestiae Porro?",
            "description": "Jan 20, 2024 by Sabir",
            "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707604621/blog-3_ko9kq9.jpg"
        }
        ]
    },
        "logos": {
            "companies": [
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707780037/br-1_hqubpv.png",
                    "url": "https://examble.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707780041/br-2_tlsefn.png",
                    "url": "https://examble.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707780045/br-3_tjyara.png",
                    "url": "https://examble.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707780049/br-4_zf3evw.png",
                    "url": "https://examble.com"
                },
                {
                    "imgUrl": "https://res.cloudinary.com/dmcdea0b9/image/upload/v1707780053/br-5_tczupi.png",
                    "url": "https://examble.com"
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
                    },
                    {
                        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809142/templates/template_one/linkedin_itbvp5.svg",
                        "url": "https://linkedin.com"
                    },
                    {
                        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701809141/templates/template_one/instagram_dlrab9.svg",
                        "url": "https://instagram.com"
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
                        },
                        {
                            "title": "Contact",
                            "url": "#contact"
                        },
                        {
                            "title": "Blog",
                            "url": "#blog"
                        }
                        ]
                    },
                {
                    "title": "Quick Links",
                    "links": [
                        {
                            "title": "Home",
                            "url": "#home"
                        },
                        {
                            "title": "About",
                            "url": "#about"
                        },
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
