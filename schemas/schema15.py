from utils import generate_text, search_image

def schema_15(user_text):
    return {
        "templateInfo": {
            "id": 15,
            "title": generate_text(f"Generate a unique name for a website in just 2 words about {user_text}"),
            "description": "",
            "imgUrl": ""
        },
        
  "navbar": {
    "links": [
      {"text": "Home", "url": "#home"},
      {"text": "About", "url": "#about"},
      {"text": "Services", "url": "#services"},
      {"text": "Features", "url": "#features"},
      {"text": "Projects", "url": "#projects"},
      {"text": "Testimonials", "url": "#testimonials"},
      {"text": "Pricing", "url": "#pricing"},
      {"text": "Blog", "url": "#blog"},
      {"text": "Contact", "url": "#contact"}
    ],
    "logo": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708020289/jammal_photos/yd48mthnmtr9zswrqrms.png"
  },
  "hero": {
    "title": "Welcome to My Personal Website",
    "description": "I am a web developer and designer with a passion for creating beautiful and functional websites.",
    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708020289/jammal_photos/yd48mthnmtr9zswrqrms.png",
    "buttonText": "Learn More",
    "linkText": "About Me"
  },
  "services": {
    "title": "SERVICES",
    "subtitle": "What I Offer",
    "services": [
      {
        "title":generate_text(f"generate just only title name for a service related to {user_text}"),
        "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
        "icon": "https://example.com/icon1.png"
      },
      {
        "title": generate_text(f"Generate a service title related to {user_text}"),
        "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
        "icon": "https://example.com/icon2.png"
      },
      {
        "title": generate_text(f"Generate a service title related to {user_text}"),
        "description": generate_text("Write a brief description of a service in 20 words or less related to {user_text}"),
        "icon": "https://example.com/icon3.png"
      }
    ]
  },
  "features": {
    "title": "PROFESSIONAL SKILLS",
    "subtitle": "My Talent",
    "features": [
      {
        "title": "PHP",
        "number": "85",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        "title": "JavaScript",
        "number": "65",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        "title": "WordPress",
        "number": "60",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        "title": "Python",
        "number": "50",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        "title": "React",
        "number": "70",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        "title": "Adobe XD",
        "number": "85",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      }
    ]
  },
  "projects": {
    "title": "PORTFOLIO",
    "subtitle": "My Cases",
    "buttonText": "See Pricing",
    "linkText": "VIEW MORE",
    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708020289/jammal_photos/yd48mthnmtr9zswrqrms.png",
    "categories": ["All", "VIDEO", "PHOTOGRAPHY", "BRANDING"],
    "projects": [
      {
        "title": "BRANDING",
        "subtitle": "Zorro",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      },
      {
        "title": "BRANDING",
        "subtitle": "Gooir",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      },
      {
        "title": "VIDEO",
        "subtitle": "Explore",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      },
      {
        "title": "VIDEO",
        "subtitle": "Stay Fit",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      },
      {
        "title": "PHOTOGRAPHY",
        "subtitle": "Kana",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      },
      {
        "title": "PHOTOGRAPHY",
        "subtitle": "Mozar",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707863903/jammal_photos/rnu0jaturksoviadcjr6.jpg"
      }
    ]
  },
  "cta": {
    "title": "RESUME",
    "subtitle": "My Story",
    "imgs": [
      "https://res.cloudinary.com/duc04fwdb/image/upload/v1708028064/jammal_photos/dxfncgzlnm5uoeyhugkf.svg",
      "https://res.cloudinary.com/duc04fwdb/image/upload/v1708027950/jammal_photos/suloncptxwohoete98cr.png"
    ],
    "educations": [
      {
        "title": "CoderHouse Courses",
        "subtitle": "Backend Programming",
        "year": "2014 - 2016",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "education"
      },
      {
        "title": "Lviv National Academy of Arts",
        "subtitle": "Faculty of Design",
        "year": "2012 - 2014",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "education"
      },
      {
        "title": "IT Future",
        "subtitle": "High School",
        "year": "2010 - 2012",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "education"
      }
    ],
    "experiences": [
      {
        "title": "UI Head & Manager",
        "subtitle": "Soft Tech Inc.",
        "year": "2020 - 2022",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "experience"
      },
      {
        "title": "UI / UX Specialist",
        "subtitle": "Kana Design Studio",
        "year": "2018 - 2020",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "experience"
      },
      {
        "title": "Plugins Developer",
        "subtitle": "Fiverr.com",
        "year": "2016 - 2018",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "category": "experience"
      }
    ]
  },
  "testimonials": {
    "title": "Testimonials",
    "subtitle": "WHAT Customers Say",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "testimonials": [
      {
        "name": "Barbara Wilson",
        "subtitle": "CEO Company",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
      },
      {
        "name": "Charlie Smith",
        "subtitle": "Designer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
      },
      {
        "name": "Roy Wang",
        "subtitle": "Manager GYM",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
      },
      {
        "name": "Jennifer Smith",
        "subtitle": "CEO & Founder",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
      },
      {
        "name": "Paul Freeman",
        "subtitle": "Photographer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707919266/jammal_photos/sq5wudx05l26l781sjgf.jpg"
      }
    ]
  },
  "pricing": {
    "title": "PRICING",
    "subtitle": "MY Price Board",
    "plans": [
      {
        "title": "HOURLY BASIS",
        "price": "39",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
        "timeUnit": "hour",
        "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
      },
      {
        "title": "FREELANCING",
        "price": "259",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
        "timeUnit": "Week",
        "features": ["Brand Design", "Web Development", "Advertising", "Photography"]
      },
      {
        "title": "FULL TIME",
        "price": "1.249",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum suspendisse ultrices gravida.",
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
    "title": "LATEST BLOG",
    "subtitle": "MY Articles and Advice",
    "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
    "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708030465/jammal_photos/capby7kt0b8mwxgzf3hs.png",
    "buttonText": "Read more",
    "linkText": "VIEW BLOG",
    "blogs": [
      {
        "title": "The Main Thing For The Designer",
        "date": "OCTOBER 31, 2022",
        "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942658/jammal_photos/lyixvtrnvyazsfa5yuje.jpg"
      },
      {
        "title": "Follow Your Own Design Process",
        "date": "OCTOBER 31, 2022",
        "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942696/jammal_photos/yjikp3c1msirossmsu3d.jpg"
      },
      {
        "title": "Usability Secrets to Create Better Interfaces",
        "date": "NOVEMBER 28, 2021",
        "description": "Vivamus interdum suscipit lacus. Nunc ultrices accumsan matties. Aliguam vel sem vel velit efficer malesuda. Donec arcu lacus, ornare rget...",
        "imgUrl": "https://res.cloudinary.com/duc04fwdb/image/upload/v1707942724/jammal_photos/fiysz2n20varciifews5.jpg"
      }
    ]
  },
  "contact": {
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
    "title": "Copyright Ⓒ 2022 LUIQUE . ALL RIGHTS RESERVED",
    "subtitle": "DEVELOPED BY BSLTHEMES",
    "medias": [
      {
        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017487/jammal_photos/dov4re8wizaegdj3jiza.svg",
        "url": "https://x.com/?lang-en="
      },
      {
        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017404/jammal_photos/ihzghh1idyxmj1u4vk9r.svg",
        "url": "https://x.com/?lang-en="
      },
      {
        "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1708017568/jammal_photos/hpyyah3zyuwxvydg7dnw.png",
        "url": "https://x.com/?lang-en="
      }
    ]
  },
  "colors": {
    "templateColors": ["red", "red", "red", "red", "red"]
  }
}
