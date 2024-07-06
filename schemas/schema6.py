from utils import generate_text, search_image

def schema_6(user_text):
    return {
       "templateInfo": {
            "id": 6,
            "title": generate_text(f"generate just only one  name for a website in just 2 words about {user_text}"),
            "description": generate_text(f"generate just only one a description for a website in just 10 words about {user_text}"),
            "imgUrl": search_image(f"generate an image URL for a website about {user_text}")
        },
        "navbar": {
               "title": generate_text(f"generate just only one  name for a website in just 2 words about {user_text}"),
               "searchIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095771/jammal_photos/kedw9coptwqkovrsssd1.svg",
               "shoppingIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
               "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095877/jammal_photos/rwbeynsg3bftgrjqaqnf.svg",
            "links": [
                {"title": "Home", "url": "#"},
                {"title": "About", "url": "#"},
                {"title": "Menu", "url": "#"},
                {"title": "Recipes", "url": "#"},
                {"title": "Contact", "url": "#"}
            ]
        },
         "hero": {
         "buttonText": "Explore Food",
         "heros": [
           {
        "title": "Experience the Authentic Flavors",
        "description": "Indulge in our simple and delicious dishes crafted with the finest ingredients. Your taste buds will thank you!",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703096681/jammal_photos/eukd4unr2l7mwyllvmi9.png"
      },
      {
        "title": "Bring Joy to Your Taste Buds",
        "description": "At our restaurant, we believe good food leads to great smiles. Explore our menu and discover a world of culinary delight.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703096719/jammal_photos/j7y2zx8aolnucnu25dl4.png"
      },
      {
        "title": "Savor Every Bite, Create Memories",
        "description": "Meet, eat, and enjoy the true taste of happiness. Our diverse menu ensures there's something for everyone to relish and remember.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703096745/jammal_photos/j97dbol3pzuleeccxwdt.png"
      }
    ]
  },

       "menu": {
    "Title": "Popular food menu",
    "subtitle": "Price: $",
    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
    "rateIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1706352872/jammal_photos/v02eynmgkqv3wkrbhnda.svg",

        "services": [
        {
            "title": "Vegetable",
            "price": 25,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098596/jammal_photos/n4r8kzctvhbymxmmydhq.png"
        },
        {
            "title": "Chicken",
            "price": 250,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098694/jammal_photos/rbtige8oucnpqluq3b5j.png"
        },
        {
            "title": "Whipped Cream",
            "price": 45,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098853/jammal_photos/zuclkds0uufzktzfeien.png"
        },
        {
            "title": "Pizza",
            "price": 75,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
        }
        ]
    },

    "products": {
    "title": "Our Menu Pack",
    "subtitle": "Price: $",
    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095842/jammal_photos/gehvutbyftfxemvoqmu8.svg",
    "rateIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1706352872/jammal_photos/v02eynmgkqv3wkrbhnda.svg",

    "products": [
      {
        "title": "FAST FOOD",
        "items": [
          {
            "itemId": "05",
            "title": "Burger",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "06",
            "title": "Chicken",
            "price": 250,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "07",
            "title": "Grill Chicken",
            "price": 195,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "08",
            "title": "Barbeque",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "09",
            "title": "Pizza",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "10",
            "title": "Burger",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "11",
            "title": "Chicken",
            "price": 250,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          },
          {
            "itemId": "12",
            "title": "Grill Chicken",
            "price": 195,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099049/jammal_photos/nw1126s6ntsb3o2ohs3s.png"
          }
        ]
      },
      {
        "title": "RICE MENU",
        "items": [
          {
            "itemId": "12",
            "title": "Fried Rice",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "14",
            "title": "Vegetable",
            "price": 250,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "15",
            "title": "Vegetable",
            "price": 195,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "16",
            "title": "Meal",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "17",
            "title": "Fried Rice",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "18",
            "title": "Vegetable",
            "price": 250,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "19",
            "title": "Vegetable",
            "price": 195,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          },
          {
            "itemId": "20",
            "title": "Meal",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099126/jammal_photos/t6olygisps4ufz02fezk.png"
          }
        ]
      },
      {
        "title": "DESSERT",
        "items": [
          {
            "itemId": "21",
            "title": "Whipped Cream",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099235/jammal_photos/mwphxi7ujoec1c2krana.png"
          },
          {
            "itemId": "22",
            "title": "Cake Cream",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098853/jammal_photos/zuclkds0uufzktzfeien.png"
          },
          {
            "itemId": "23",
            "title": "Cake",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099235/jammal_photos/mwphxi7ujoec1c2krana.png"
          },
          {
            "itemId": "24",
            "title": "Cup Cake",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099335/jammal_photos/why415hwonyxffn1cyon.png"
          },
          {
            "itemId": "25",
            "title": "Whipped Cream",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099235/jammal_photos/mwphxi7ujoec1c2krana.png"
          },
          {
            "itemId": "26",
            "title": "Cake Cream",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098853/jammal_photos/zuclkds0uufzktzfeien.png"
          },
          {
            "itemId": "27",
            "title": "Cake",
            "price": 50,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099235/jammal_photos/mwphxi7ujoec1c2krana.png"
          },
          {
            "itemId": "28",
            "title": "Cup Cake",
            "price": 275,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099335/jammal_photos/why415hwonyxffn1cyon.png"
          }
        ]
      },
      {
        "title": "PIZZA",
        "items": [
          {
            "itemId": "29",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "30",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "31",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "32",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "33",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "34",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "35",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          },
          {
            "itemId": "36",
            "title": "Pizza",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703098919/jammal_photos/bvipjezk42alazv5roew.png"
          }
        ]
      },
      {
        "title": "COFFEE",
        "items": [
          {
            "itemId": "37",
            "title": "Hot Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "38",
            "title": "Cold Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "39",
            "title": "Black Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "40",
            "title": "White Coffee",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "41",
            "title": "Hot Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "42",
            "title": "Cold Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "43",
            "title": "Black Coffee",
            "price": 20,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          },
          {
            "itemId": "44",
            "title": "White Coffee",
            "price": 95,
            "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703099401/jammal_photos/tb2lmnbq0imabiyxzsub.png"
          }
        ]
      }
    ]
    },
            "features": {
                "title": "Who we are?",
                "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103180/jammal_photos/afcfogeancctcy4nhsfn.png",
                "description": "Take a look at the benefits we offer you",
                "text": "we prioritize your satisfaction. Our commitment to excellence is evitemIdent in the benefits we offer. ",
                "features": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103379/jammal_photos/wvvtn9lgn5k84md2jhtm.svg",
                    "title": "Free Home Delivery",
                    "description": "Enjoy free and timely home delivery. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103489/jammal_photos/rihmvtglekzcmjdavtbm.svg",
                    "title": "Return & Refund",
                    "description": "We guarantee a hassle-free return and refund process. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103560/jammal_photos/k3irnc1fhkmugeekjbol.svg",
                    "title": "Secure Payment",
                    "description": "Your transactions are securely processed. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103423/jammal_photos/legalyoxmyba3arp5n3p.svg",
                    "title": "24/7 Hours Support",
                    "description": "We are here for you round the clock. "
                }
                ]
            },
        "features": {
                "title": "Who we are?",
                "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103180/jammal_photos/afcfogeancctcy4nhsfn.png",
                "description": "Take a look at the benefits we offer you",
                "text": "we prioritize your satisfaction. Our commitment to excellence is evitemIdent in the benefits we offer. ",
                "features": [
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103379/jammal_photos/wvvtn9lgn5k84md2jhtm.svg",
                    "title": "Free Home Delivery",
                    "description": "Enjoy free and timely home delivery. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103489/jammal_photos/rihmvtglekzcmjdavtbm.svg",
                    "title": "Return & Refund",
                    "description": "We guarantee a hassle-free return and refund process. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103560/jammal_photos/k3irnc1fhkmugeekjbol.svg",
                    "title": "Secure Payment",
                    "description": "Your transactions are securely processed. "
                },
                {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703103423/jammal_photos/legalyoxmyba3arp5n3p.svg",
                    "title": "24/7 Hours Support",
                    "description": "We are here for you round the clock. "
                }
                ]
            },
                "cta": {
                    "title": "Download our app",
                    "description": " Never Feel Hungry! Download Our Mobile App Order Delicious Food",
                    "info": "Experience the convenience of our mobile app, ensuring you never go hungry, Download now to order delicious food anytime, anywhere. ",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703105732/jammal_photos/lldrbchcloecmarn2bep.png",
                    "googleButton": {
                    "buttonText": "Google Play",
                    "buttonIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703106187/jammal_photos/bm7fqpnzrwtkawffbci3.svg"
                    },
                    "appleButton": {
                    "buttonText": "Apple Store",
                    "buttonIcon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703106097/jammal_photos/gmyir4uguaz6ejvw3s3t.svg"
                    }
                },
            "footer": {
                    "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1706351943/jammal_photos/jicfizb2xdqr8hcgkmc4.png",
                    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703095423/jammal_photos/x22ihnvjg9i0i40xtbo5.svg",
                    "description": "It is a long established fact that a reader will be distracted lookings.",
                    "title": "copyright 2022, developed by ana. All rights reserved",
                    "footerSections": [
                    {
                        "title": "Info Links",
                        "links": [
                        {
                            "title": "Terms & Conditions",
                            "url": "#"
                        },
                        {
                            "title": "Privacy Policy",
                            "url": "#"
                        },
                        {
                            "title": "Return & Refund",
                            "url": "#"
                        },
                        {
                            "title": "Payment Method",
                            "url": "#"
                        }
                        ]
                    },
                    {
                        "title": "Quick Links",
                        "links": [
                        {
                            "title": "About Us",
                            "url": "#"
                        },
                        {
                            "title": "Menu",
                            "url": "#"
                        },
                        {
                            "title": "Recipes",
                            "url": "#"
                        },
                        {
                            "title": "Contact",
                            "url": "#"
                        }
                        ]
                    }
                    ],
                    "contacts": [
                    {
                        "value": "Sylhet, Bangladesh",
                        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108316/jammal_photos/oe8rjvrg0ckgohix2b6v.svg"
                    },
                    {
                        "value": "example@gmail.com",
                        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108228/jammal_photos/opdhewds9do1znaaj5li.svg"
                    },
                    {
                        "value": "+880 123 456 7890",
                        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1703108367/jammal_photos/y2583eh76th902gnzlje.svg"
                    }
                    ]
                },
                "colors": {
                    "templateColors": ["#0a071a", "#141124", "#f76e11", "#f5b70a", "#fff", "#c4c4c4b5"]
                }
                }
